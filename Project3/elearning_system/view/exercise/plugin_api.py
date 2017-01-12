import requests
# import json
from requests.adapters import ConnectionError
import datetime
from elearning_system.view.exercise.process_models import PluginExercise, TestCase

MAX_URI_LEN = 8192
USER_AGENT = 'exercise_web_server'

PLUGIN_IP = u'45.63.50.197'


def request(url, method, body=None, headers=None, **kwargs):
    """Request without authentication."""

    content_type = kwargs.pop('content_type', None) or 'application/json'
    headers = headers or {}
    headers.setdefault('Accept', content_type)

    if body:
        headers.setdefault('Content-Type', content_type)

    headers['User-Agent'] = USER_AGENT
    try:
        resp = requests.request(
            method,
            url,
            data=body,
            headers=headers,
            **kwargs)
    except:
        raise ConnectionError
    return resp, resp.text


def get_date_from_input(date_input):
    if date_input is None:
        return None
    elif not date_input:
        return "none"
    else:
        try:
            return datetime.datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            return None


class InputError(Exception):
    pass


class TestCodeResult:
    def __init__(self, status, test_case_result, message, error_output=None,execute_output=None):
        self.status = status
        self.test_case_result_list = test_case_result
        self.message = message
        self.error_output = error_output


def _convert_test_case_list(test_case_list_input):
    converted_test_case_list = []
    for test_case in test_case_list_input:
        param_arr = test_case.param_arr
        param_converted_string = ''
        for param in param_arr:
            param_converted_string = param_converted_string + str(param) + '\n'
        if len(param_converted_string) > 2:
            param_converted_string = param_converted_string[:-1]
        value = test_case.value
        converted_test_case_list.append({'params': param_converted_string, 'result': value})
    return converted_test_case_list


def _convert_test_case_plugin_to_standard_test_case(plugin_test_case_list):
    converted_test_case_list = []
    for test_case in plugin_test_case_list:
        param_string_input = test_case['params']
        param_arr_input = param_string_input.split("\n")
        param_arr = []
        for param_input in param_arr_input:
            param_arr.append(param_input)
        value = test_case['result']
        converted_test_case_list.append(TestCase(param_arr=param_arr, value=value))
    return converted_test_case_list


def test_code(check_code_data):
    try:
        endpoint = u'http://' + PLUGIN_IP + '/plugin/testcode'
        source_code = check_code_data.solution.solution_code
        language = check_code_data.solution.solution_language
        test_case_list = _convert_test_case_list(check_code_data.test_case)
        api_body = {
            'language': language,
            'sourceCode': source_code,
            'testcases': test_case_list
        }
    except Exception:
        return TestCodeResult('failed', [], 'Input format is not valid')
    try:
        response = requests.post(endpoint, json=api_body)
        data = response.json()
        compile_error = data['compileErr']
        execute_error = data['executeErr']
        test_code_error = data['testCodeErr']
        if compile_error == 'null' and execute_error == 'null' and test_code_error == 'null':
            test_case_result_list = []
            for test_case in data['result']:
                if test_case == 'pass':
                    test_case_result_list.append('p')
                elif test_case == 'fail':
                    test_case_result_list.append('f')
            return TestCodeResult('success', test_case_result_list, 'no error')
        else:
            error_message = ''
            error_output = ''
            if compile_error != 'null':
                error_output = compile_error + '\n'
                error_message += ' Failed to compile solution code. Check your solution again.'
            if execute_error != 'null':
                error_output = execute_error + '\n'
                error_message += ' Failed to execute solution code. Check your solution again.'
            if test_code_error != 'null':
                error_output = test_code_error + '\n'
                error_message += ' Failed to excute solution code. Test code is not valid.'
            return TestCodeResult('failed', [], error_message,error_output=error_output)

    except Exception as e:
        return TestCodeResult('failed', [], 'Failed to execute solution code. Please try again later')


def save_plugin_exercise(plugin_exercise):
    try:
        endpoint = u'http://' + PLUGIN_IP + '/plugin/add'

        name = plugin_exercise.name
        description = plugin_exercise.description
        content = plugin_exercise.content
        test_case_list = _convert_test_case_list(plugin_exercise.test_case_list)
        solution = plugin_exercise.solution
        api_body = {
            'name': name,
            'description': description,
            'content': content,
            'testcases': test_case_list,
            'solution': {
                'code': solution.solution_code,
                'language': solution.solution_language
            }
        }
    except Exception:
        return {'status': 'failed', 'message': 'Input format is not valid'}

    try:
        response = requests.post(endpoint, json=api_body)
        data = response.json()
        if data['status'] == 'success':
            return {
                'status': 'success', 'message': 'Add exercise to plugin successful',
                'exercise_plugin_id': data['exid']
            }
        else:
            return {
                'status': 'failed', 'message': 'Failed to add exercise',
            }
    except Exception:
        return {'status': 'failed', 'message': 'Failed to add exercise. Try again later'}


def get_exercise_plugin_detail(exercise_plugin_id):
    endpoint = u'http://' + PLUGIN_IP + '/plugin/detail?exid=' + str(exercise_plugin_id)

    try:
        response = requests.get(endpoint)
        data = response.json()

        if data['status'] == 'success':
            plugin_exercise_response = PluginExercise(
                name=data['name'],
                description=data['description'],
                content=data['content'],
                test_case_list=_convert_test_case_plugin_to_standard_test_case(data['testcases']),
                solution='solution'
            )
            return {
                'status': 'success',
                'plugin_exercise': plugin_exercise_response
            }
        else:
            return {
                'status': 'failed', 'message': 'Failed get exercise detail from plugin',
            }
    except Exception as e:
        return {'status': 'failed', 'message': 'Failed get exercise detail. Try again later'}


def solve_exercise(exercise_id, solution):
    try:
        endpoint = u'http://' + PLUGIN_IP + '/plugin/solve'
        api_body = {
            'exid': exercise_id,
            'language': solution.solution_language,
            'sourceCode': solution.solution_code,
        }
    except Exception:
        return {'status': 'failed', 'message': 'Input format is not valid'}

    try:
        response = requests.post(endpoint, json=api_body)
        data = response.json()
        if data['solveStatus'] == 'success':
            test_case_result_list = []
            for test_case in data['result']:
                if test_case == 'pass':
                    test_case_result_list.append('p')
                elif test_case == 'fail':
                    test_case_result_list.append('f')

            return {
                'status': 'success', 'message': 'Solve exercise successful',
                'test_case_result': test_case_result_list
            }
        else:
            compile_error = data['compileErr']
            execute_error = data['executeErr']
            test_code_error = data['testcaseErr']
            error_message = ''
            error_output = ''
            if compile_error != 'null':
                error_output = compile_error + '\n'
                error_message += ' Failed to compile solution code. Check your solution again.'
            if execute_error != 'null':
                error_output = execute_error + '\n'
                error_message += ' Failed to execute solution code. Check your solution again.'
            if test_code_error != 'null':
                error_output = test_code_error + '\n'
                error_message += ' Failed to excute solution code. Test code is not valid.'
            return {
                'status': 'failed', 'message': 'Failed to solve Exercise. ' + data['message'],
                'error_output':error_output
            }
    except Exception as e:
        return {'status': 'failed', 'message': 'Failed to solve Exercise. Try again later'}


def update_exercise(plugin_exercise_id, plugin_exercise):
    try:
        endpoint = u'http://' + PLUGIN_IP + '/plugin/update'
        api_body = {
            'id': plugin_exercise_id,
            'name': plugin_exercise.name,
            'description': plugin_exercise.description,
            'content': plugin_exercise.content,
            'testcases': _convert_test_case_list(plugin_exercise.test_case_list)
        }
    except Exception as e:
        return {'status': 'failed', 'message': 'Input format is not valid'}

    try:
        response = requests.post(endpoint, json=api_body)
        data = response.json()
        if data['status'] == 'success':
            return {
                'status': 'success', 'message': 'Add exercise to plugin successful',
                'exercise_plugin_id': data['exid']
            }
        else:
            return {
                'status': 'failed', 'message': 'Failed to add exercise',
            }
    except Exception:
        return {'status': 'failed', 'message': 'Failed to add exercise. Try again later'}
