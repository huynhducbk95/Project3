import requests
# import json
from requests.adapters import ConnectionError
import datetime
from elearning_system.view.exercise.process_models import PluginExercise, TestCase

MAX_URI_LEN = 8192
USER_AGENT = 'exercise_web_server'

PLUGIN_IP = u'45.63.50.197'


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
                'plugin_exercise':plugin_exercise_response
            }
        else:
            return {
                'status': 'failed', 'message': 'Failed get exercise detail from plugin',
            }
    except Exception as e:
        return {'status': 'failed', 'message': 'Failed get exercise detail. Try again later'}


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

# def _convert_exercise_solution(solution):
