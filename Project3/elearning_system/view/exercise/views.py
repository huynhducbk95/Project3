import string
from django.shortcuts import render
from django.http.response import HttpResponse
import json
from elearning_system.central_control import check_role, render_template, check_user_is_login
from elearning_system.view.exercise import plugin_api
from elearning_system.view.exercise.process_models import TestCase, CheckCodeData, Solution
from elearning_system.models import User, ErrorMessage


@check_role('admin')
def test_code(request):
    if request.method == "GET":
        return render_template(request, 'elearning_system/exercise/test_code.html',
                               {'title': 'Test Code'})
    if request.method == "POST":
        return_result = {}
        try:
            source_code = request.POST['source_code']
        except Exception as e:
            return_result = {'status': 'failed', 'message': 'invalid source code', 'test_case_list': []}

            return HttpResponse(json.dumps(return_result), content_type='application/json')
        try:
            language = request.POST['language']
        except Exception as e:
            return_result = {'status': 'failed', 'message': 'invalid language code', 'test_case_list': []}
            return HttpResponse(json.dumps(return_result), content_type='application/json')
        try:
            test_case_input_string = request.POST['test_case']
            test_case_input_list = string.split(test_case_input_string, '\n')
            test_case_list = []
            for test_case_input in test_case_input_list:
                if len(test_case_input) > 3:
                    test_case_split = string.split(test_case_input, ':')
                    test_case_input_param_list = string.split(test_case_split[0], ';')
                    test_case_input_value = test_case_split[1].replace(" ", "")
                    test_case_param_list = []
                    for test_case_input_param in test_case_input_param_list:
                        test_case_input_param = test_case_input_param.replace(" ", "")
                        test_case_param_list.append(test_case_input_param)
                    test_case = {'param': test_case_param_list, 'value': test_case_input_value}
                    test_case_list.append(test_case)
            test_code_result = plugin_api.test_code(test_case_list, language, source_code)
            if test_code_result.status == 'success':
                return_result['status'] = 'success'
                return_result['test_case_list'] = test_code_result.test_case_result_list
                return_result['message'] = 'test proccess succeed!'
            if test_code_result.status == 'failed':
                return_result['status'] = 'failed'
                return_result['test_case_list'] = []
                return_result['message'] = test_code_result.message
            return HttpResponse(json.dumps(return_result), content_type='application/json')
        except Exception as e:
            return_result = {'status': 'failed', 'message': 'invalid test case', 'test_case_list': []}
            return HttpResponse(json.dumps(return_result), content_type='application/json')


# def exercise_detail_without_login(request):
#     print ('y')
#     return render(request, 'elearning_system/exercise/exercise_detail_without_login.html',
#                   {'title': 'registry'})
@check_role('user')
def report_exercise_error(request):
    if request.method == "POST":
        return_result = {}
        try:
            user_name= request.session['user_name']
            reporter = User.objects.filter(user_name=user_name).first()
            exercise_id = request.POST['exercise_id']
            message_title = request.POST['message_title']
            message_content = request.POST['message_content']
            report_message = ErrorMessage()
            return_result = {'status': 'success'}
        except Exception:
            return_result = {'status': 'failed'}
        return HttpResponse(json.dumps(return_result), content_type='application/json')


def exercise_detail(request):
    if check_user_is_login(request) is True:
        return render_template(request, 'elearning_system/exercise/exercise_detail.html',
                      {'title': 'registry'})
    else:
        return render(request, 'elearning_system/exercise/exercise_detail_without_login.html',
                      {'title': 'registry'})


def convert_test_case_string_to_list(test_case_string):
    test_case_list = []
    try:
        test_case_input_list = string.split(test_case_string, '\n')
        for test_case_input in test_case_input_list:
            if len(test_case_input) > 3:
                test_case_split = string.split(test_case_input, ':')
                test_case_input_param_list = string.split(test_case_split[0], ';')
                test_case_input_value = test_case_split[1].replace(" ", "")
                test_case_param_list = []
                for test_case_input_param in test_case_input_param_list:
                    test_case_input_param = test_case_input_param.replace(" ", "")
                    test_case_param_list.append(test_case_input_param)

                test_case = TestCase(param_arr=test_case_param_list, value=test_case_input_value)
                test_case_list.append(test_case)
        return test_case_list
    except Exception as e:
        return 'error'


@check_role('user')
def solve_exercise(request):
    if request.method == "POST":
        return_result = {}
        try:
            source_code = request.POST['source_code']
        except Exception as e:
            return_result = {'status': 'failed', 'message': 'invalid source code', 'test_case_list': []}

            return HttpResponse(json.dumps(return_result), content_type='application/json')
        try:
            language = request.POST['language']
        except Exception as e:
            return_result = {'status': 'failed', 'message': 'invalid language code', 'test_case_list': []}
            return HttpResponse(json.dumps(return_result), content_type='application/json')
        try:
            test_case_input_string = request.POST['test_case']
            test_case_list = convert_test_case_string_to_list(test_case_input_string)
            if test_case_list != 'errror':
                if len(test_case_list) < 20:
                    return_result['status'] = 'failed'
                    return_result['test_case_list'] = []
                    return_result['message'] = 'test case file must have more than 20 test cases'
                else:
                    test_code_result = plugin_api.test_code(test_case_list, language, source_code)
                    if test_code_result.status == 'success':
                        return_result['status'] = 'success'
                        return_result['test_case_list'] = test_code_result.test_case_result_list
                        return_result['message'] = 'test proccess succeed!'
                    if test_code_result.status == 'failed':
                        return_result['status'] = 'failed'
                        return_result['test_case_list'] = []
                        return_result['message'] = test_code_result.message
            else:
                return_result['status'] = 'failed'
                return_result['test_case_list'] = []
                return_result['message'] = 'invalid_test_case'
            return HttpResponse(json.dumps(return_result), content_type='application/json')
        except Exception as e:
            return_result = {'status': 'failed', 'message': 'invalid test case', 'test_case_list': []}
            return HttpResponse(json.dumps(return_result), content_type='application/json')


def check_test_case_list_is_pass(test_case_result_list):
    test_case_list = test_case_result_list
    total_test_case = len(test_case_list)
    total_test_pass = 0
    for test_case_check in test_case_list:
        if test_case_check == 'p':
            total_test_pass += 1

    if total_test_pass < total_test_case:
        return {'test_result': False, 'total': total_test_case, 'total_pass': total_test_pass}
    else:
        return {'test_result': True}


@check_role('user')
def contribute_exercise(request):
    if request.method == "GET":
        return render(request, 'elearning_system/exercise/contribute_exercise.html',
                      {'title': 'registry'})

    if request.method == "POST":
        return_result = {}
        try:
            exercise_name_input = request.POST['exercise_name']
            exercise_description_input = request.POST['exercise_description']
            exercise_detail_input = request.POST['exercise_content']
            test_case_input_string = request.POST['test_case']
            solution_code = request.POST['solution']
            solution_language = request.POST['solution_language']
        except Exception:
            return_result = {'status': 'failed', 'message': 'invalid parameter', 'test_case_list': []}
            return HttpResponse(json.dumps(return_result), content_type='application/json')

        try:
            test_case_list = convert_test_case_string_to_list(test_case_input_string)
            if test_case_list != 'error':
                if len(test_case_list) < 1:
                    return_result['status'] = 'failed'
                    return_result['test_case_list'] = []
                    return_result['message'] = 'test case file must have more than 20 test cases'
                else:
                    solution = Solution(solution_code, solution_language)
                    check_code_data = CheckCodeData(test_case_list, solution)

                    test_code_result = plugin_api.test_code(check_code_data)
                    if test_code_result.status == 'success':
                        check_code_input = check_test_case_list_is_pass(test_code_result.test_case_result_list)
                        if check_code_input['test_result'] is True:
                            pass
                        else:
                            return_result = {
                                'status': 'failed',
                                'test_case_list': [],
                                'message': 'solution is not correct. Result ' + str(
                                    check_code_input['total_pass']) + ' / ' + str(
                                    check_code_input['total']) + ' passed!'
                            }
                        return HttpResponse(json.dumps(return_result), content_type='application/json')
                    if test_code_result.status == 'failed':
                        return_result = {
                            'status': 'failed',
                            'test_case_list': [],
                            'message': test_code_result.message
                        }
                        return HttpResponse(json.dumps(return_result), content_type='application/json')
            else:
                return_result = {
                    'status': 'failed',
                    'test_case_list': [],
                    'message': 'invalid test case'
                }
                return HttpResponse(json.dumps(return_result), content_type='application/json')
        except Exception:
            return_result = {'status': 'failed', 'message': 'invalid test case', 'test_case_list': []}
            return HttpResponse(json.dumps(return_result), content_type='application/json')
