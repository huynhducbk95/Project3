import string
from django.shortcuts import render
from django.http.response import HttpResponse
import json

from elearning_system.views.exercise import plugin_api


def test_code(request):
    if request.method == "GET":
        return render(request, 'elearning_system/exercise/test_code.html',
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
def report_exercise_error(request):
    if request.method == "POST":
        return_result = {}
        try:
            exercise_id = request.POST['exercise_id']
            message_title = request.POST['message_title']
            message_content = request.POST['message_content']
            return_result = {'status': 'success'}
        except Exception:
            return_result = {'status': 'failed'}
        return HttpResponse(json.dumps(return_result), content_type='application/json')


def exercise_detail(request):
    print ('x')
    return render(request, 'elearning_system/exercise/exercise_detail.html',
                  {'title': 'registry'})


def convert_test_case_string_to_list(test_case_string):
    try:
        test_case_input_list = string.split(test_case_string, '\n')
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
        return test_case_list
    except Exception as e:
        return 'error'


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


def contribute_exercise(request):
    if request.method == "GET":
        return render(request, 'elearning_system/exercise/contribute_exercise.html',
                      {'title': 'registry'})

    if request.method == "POST":
        return_result = {}
        try:
            exercise_name_input = request.POST['exercise_name']
            exercise_detail_input = request.POST['exercise_detail']
            test_case = request.POST['test_case']
            solution = request.POST['solution']
            solution_language = request.POST['solution_language']
        except Exception as e:
            return_result = {'status': 'failed', 'message': 'invalid parameter', 'test_case_list': []}
            return HttpResponse(json.dumps(return_result), content_type='application/json')

        try:
            test_case_list = convert_test_case_string_to_list(test_case)
            if test_case_list != 'error':
                if len(test_case_list) < 20:
                    return_result['status'] = 'failed'
                    return_result['test_case_list'] = []
                    return_result['message'] = 'test case file must have more than 20 test cases'
                else:
                    test_code_result = plugin_api.test_code(test_case_list, solution_language, solution)
                    if test_code_result.status == 'success':
                        return_result['status'] = 'success'
                        test_case_list = test_code_result.test_case_result_list
                        total_test_case = len(test_case_list)
                        total_test_pass = 0
                        for test_case_check in test_case_list:
                            if test_case_check == 'p':
                                total_test_pass += 1
                        if total_test_pass < total_test_case:
                            return_result['status'] = 'failed'
                            return_result['test_case_list'] = []
                            return_result['message'] = 'solution is not correct. Result ' + str(
                                total_test_pass) + ' / ' + str(total_test_case) + ' passed!'
                        else:
                            # save exercise to contribute wait accept exercise list
                            pass
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
