import string
from django.shortcuts import render
from django.http.response import HttpResponse
import json
import datetime
from elearning_system.central_control import check_role, render_template, check_user_is_login, check_user_is_block, \
    get_user_name
from elearning_system.view.exercise import plugin_api
from elearning_system.view.exercise.process_models import TestCase, CheckCodeData, Solution, PluginExercise, \
    ExerciseDetailViewModel
from elearning_system.models import User, ErrorMessage, ExerciseWebServer
from elearning_system.view.exercise.database_service import DatabaseService


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


def convert_test_case_to_view_mode(test_case):
    test_case_view_mode = ''
    for i in range(0, len(test_case.param_arr)):
        test_case_view_mode += 'x' + str(i + 1) + '=' + str(test_case.param_arr[i]) + '; '
    test_case_view_mode = test_case_view_mode[:-2]
    test_case_view_mode += ' => ' + str(test_case.value)
    return test_case_view_mode


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


def test_code(request):
    if request.method == "GET":
        return render_template(request, 'elearning_system/exercise/test_code.html',
                               {'title': 'Test Code'})
    if request.method == "POST":
        return_result = {}
        try:
            solution_code = request.POST['source_code']
            solution_language = request.POST['language']
            test_case_input_string = request.POST['test_case']
        except Exception:
            return_result = {'status': 'failed', 'message': 'invalid parameter', 'test_case_list': []}
            return HttpResponse(json.dumps(return_result), content_type='application/json')
        try:
            test_case_list = convert_test_case_string_to_list(test_case_input_string)
            if test_case_list != 'error':
                if len(test_case_list) < 1:
                    return_result['status'] = 'failed'
                    return_result['test_case_list'] = []
                    return_result['message'] = 'test case file must have more than 1 test cases'
                else:
                    solution = Solution(solution_code, solution_language)
                    check_code_data = CheckCodeData(test_case_list, solution)
                    test_code_result = plugin_api.test_code(check_code_data)
                    if test_code_result.status == 'success':
                        return_result = {
                            'status': 'success',
                            'test_case_list': test_code_result.test_case_result_list,
                            'message': 'test proccess succeed!'
                        }
                    if test_code_result.status == 'failed':
                        return_result = {
                            'status': 'failed',
                            'test_case_list': [],
                            'message': test_code_result.message
                        }
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


# def exercise_detail_without_login(request):
#     print ('y')
#     return render(request, 'elearning_system/exercise/exercise_detail_without_login.html',
#                   {'title': 'registry'})
@check_role('user')
def report_exercise_error(request):
    if request.method == "POST":
        return_result = {}
        try:
            user_name = request.session['user_name']
            reporter = User.objects.filter(user_name=user_name).first()
            exercise_id = request.POST['exercise_id']
            exercise_reported = DatabaseService.get_exercise_web_server_detail(exercise_id)
            message_title = request.POST['message_title']
            message_content = request.POST['message_content']
            report_message = ErrorMessage(title=message_title, content=message_content, reporter=reporter,
                                          exercise_reported=exercise_reported)
            DatabaseService.add_error_message(report_message)
            return_result = {'status': 'success'}
        except Exception:
            return_result = {'status': 'failed'}
        return HttpResponse(json.dumps(return_result), content_type='application/json')


def exercise_detail(request, exercise_id):
    exercise_plugin_input = plugin_api.get_exercise_plugin_detail(exercise_id)
    exercise_web_server_detail = DatabaseService.get_exercise_web_server_detail(exercise_id)
    exercise_plugin = exercise_plugin_input['plugin_exercise']
    if exercise_web_server_detail == 'not_found' or exercise_web_server_detail == 'error' \
            or exercise_plugin_input['status'] == 'failed' or exercise_web_server_detail.approver is None:
        return render_template(request, 'elearning_system/exercise/exercise_detail_not_found.html',
                               {'title': 'Access Denied'})
    else:
        exercise_test_case_list_view = []
        for i in range(0, 3):
            exercise_test_case_list_view.append(
                convert_test_case_to_view_mode(exercise_plugin.test_case_list[i])
            )
        create_date = exercise_web_server_detail.date_created
        create_date_view_format = str(create_date.day) + ' - ' + \
                                  str(create_date.month) + ' - ' + str(create_date.year)
        exercise_web_server_detail.view_number += 1
        exercise_web_server_detail.save()
        contributor = {
            'full_name': exercise_web_server_detail.contributor.full_name,
            'user_name': exercise_web_server_detail.contributor.user_name,
            'id': exercise_web_server_detail.contributor.id
        }
        exercise_detail_view_model = ExerciseDetailViewModel(
            exercise_id=exercise_id,
            name=exercise_plugin.name,
            description=exercise_plugin.description,
            content=exercise_plugin.content.replace('<br/>', '\n'),
            test_case_list=exercise_test_case_list_view,
            contributor=contributor,
            solve_number=exercise_web_server_detail.solve_number,
            view_number=exercise_web_server_detail.view_number,
            create_date=create_date_view_format,
            tag=exercise_web_server_detail.tag
        )

        if check_user_is_login(request) is True:
            if not check_user_is_block(get_user_name(request)):
                return render_template(request, 'elearning_system/exercise/exercise_detail.html',
                                       {'exercise_detail': exercise_detail_view_model})
            else:
                return render_template(request, 'elearning_system/central_control/http_403_user_block.html',
                                       {'title': 'Access Denied'})

        else:
            return render_template(request, 'elearning_system/exercise/exercise_detail_without_login.html',
                                   {'exercise_detail': exercise_detail_view_model})


@check_role('user')
def solve_exercise(request):
    if request.method == "POST":
        return_result = {}
        try:
            solution_code = request.POST['source_code']
            language = request.POST['language']
            exercise_id = request.POST['exercise_id']
        except Exception as e:
            return_result = {'status': 'failed', 'message': 'invalid parameter', 'test_case_list': []}
            return HttpResponse(json.dumps(return_result), content_type='application/json')
        try:
            exercise_solve = plugin_api.solve_exercise(
                exercise_id,
                Solution(solution_code=solution_code, solution_language=language)
            )
            return_result = {'status': 'success', 'message': 'You solve this exercise successful', 'test_case_list': []}
            return HttpResponse(json.dumps(return_result), content_type='application/json')
        except Exception as e:
            return_result = {'status': 'failed', 'message': 'Failed to solve exercise', 'test_case_list': []}
            return HttpResponse(json.dumps(return_result), content_type='application/json')


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
            exercise_detail_input = request.POST['exercise_content'].replace('\n', '<br/>')
            test_case_input_string = request.POST['test_case']
            solution_code = request.POST['solution']
            solution_language = request.POST['solution_language']
        except Exception:
            return_result = {'status': 'failed', 'message': 'invalid parameter', 'test_case_list': []}
            return HttpResponse(json.dumps(return_result), content_type='application/json')

        try:
            test_case_list = convert_test_case_string_to_list(test_case_input_string)
            if test_case_list != 'error':
                if len(test_case_list) < 20 or len(test_case_list) > 60:
                    return_result['status'] = 'failed'
                    return_result['test_case_list'] = []
                    return_result['message'] = 'test case file must have test case number between 20 and 60'
                else:
                    solution = Solution(solution_code, solution_language)
                    check_code_data = CheckCodeData(test_case_list, solution)
                    test_code_result = plugin_api.test_code(check_code_data)
                    if test_code_result.status == 'success':
                        check_code_input = check_test_case_list_is_pass(test_code_result.test_case_result_list)
                        if check_code_input['test_result'] is True:

                            contributor = User.objects.filter(user_name=request.session['user_name']).first()
                            plugin_exercise = PluginExercise(
                                exercise_name_input,
                                exercise_description_input,
                                exercise_detail_input,
                                test_case_list,
                                solution
                            )
                            submit_result = plugin_api.save_plugin_exercise(plugin_exercise)
                            if submit_result['status'] == 'success':
                                exercise_plugin_id = submit_result['exercise_plugin_id']
                                new_server_exercise = ExerciseWebServer(
                                    contributor=contributor,
                                    date_created=datetime.datetime.now()
                                )
                                new_server_exercise.id = exercise_plugin_id
                                new_server_exercise.save()
                                return_result = {
                                    'status': 'success',
                                    'test_case_list': [],
                                    'message': 'Contribute process successful'
                                }
                            else:
                                return_result = {
                                    'status': 'failed',
                                    'test_case_list': [],
                                    'message': 'Failed to save contribute exercise to sever. Please try again later.'
                                }

                        else:
                            return_result = {
                                'status': 'failed',
                                'test_case_list': [],
                                'message': 'Solution is not correct. Result ' + str(
                                    check_code_input['total_pass']) + ' / ' + str(
                                    check_code_input['total']) + ' passed!'
                            }
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


@check_role('moderator')
def edit_exercise(request):
    if request.method == "POST":
        return_result = {}
        try:
            exercise_id = request.POST['exercise_id']
            name = request.POST['name']
            description = request.POST['description']
            content = request.POST['content'].replace('\n', '<br/>')
            current_exercise_plugin_input = plugin_api.get_exercise_plugin_detail(exercise_id)
            plugin_exercise = PluginExercise(
                name,
                description,
                content,
                test_case_list=current_exercise_plugin_input['plugin_exercise'].test_case_list,
                solution=''
            )
            exercise_plugin_update_result = plugin_api.update_exercise(exercise_id, plugin_exercise)
            if exercise_plugin_update_result['status'] == 'success':
                return_result = {'status': 'success'}
            else:
                return_result = {'status': 'failed'}

        except Exception:
            return_result = {'status': 'failed'}
        return HttpResponse(json.dumps(return_result), content_type='application/json')


@check_role('moderator')
def exercise_detail_data(request, exercise_id):
    exercise_plugin_input = plugin_api.get_exercise_plugin_detail(exercise_id)
    exercise_web_server_detail = DatabaseService.get_exercise_web_server_detail(exercise_id)
    exercise_plugin = exercise_plugin_input['plugin_exercise']
    if exercise_web_server_detail == 'not_found' or exercise_web_server_detail == 'error' \
            or exercise_plugin_input['status'] == 'failed' or exercise_web_server_detail.approver is None:
        return HttpResponse(json.dumps({'status': 'failed',
                                        'message': 'exercise data cannot retrieve'}), content_type='application/json')
    else:
        exercise_test_case_list_view = []
        for i in range(0, 3):
            exercise_test_case_list_view.append(
                convert_test_case_to_view_mode(exercise_plugin.test_case_list[i])
            )
        create_date = exercise_web_server_detail.date_created
        create_date_view_format = str(create_date.day) + ' - ' + \
                                  str(create_date.month) + ' - ' + str(create_date.year)
        exercise_web_server_detail.view_number += 1
        exercise_web_server_detail.save()
        contributor = {
            'full_name': exercise_web_server_detail.contributor.full_name,
            'user_name': exercise_web_server_detail.contributor.user_name,
            'id': exercise_web_server_detail.contributor.id
        }
        exercise_detail_view_model = ExerciseDetailViewModel(
            exercise_id=exercise_id,
            name=exercise_plugin.name,
            description=exercise_plugin.description,
            content=exercise_plugin.content.replace('<br/>', '\n'),
            test_case_list=exercise_test_case_list_view,
            contributor=contributor,
            solve_number=exercise_web_server_detail.solve_number,
            view_number=exercise_web_server_detail.view_number,
            create_date=create_date_view_format,
            tag=exercise_web_server_detail.tag
        )
        return HttpResponse(json.dumps({'status': 'success',
                                        'message': 'exercise data retrieve success',
                                        'exercise_detail': exercise_detail_view_model.__dict__
                                        }), content_type='application/json')
