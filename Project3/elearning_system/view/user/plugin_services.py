import requests
import json

PLUGIN_URL = 'http://45.63.50.197/plugin/'


def exercise_detail(exercise_id):
    try:
        response = requests.get(url=PLUGIN_URL + 'detail?exid=' + str(exercise_id))
        response_data = json.loads(response.content)
        if response_data['status'] == 'fail':
            result = {
                'status': 'error'
            }
        else:
            result = {
                'status': 'success',
                'exercise': response_data
            }
    except Exception as e:
        result = {
            'status': 'error_request'
        }
    return result

def search_exercise(search_keyword):
    try:
        response = requests.get(url=PLUGIN_URL + 'search?keyword=' + search_keyword)
        response_data = response.json()
        if 'status' in response_data:
            result = {
                'status': 'no',
            }
        else:
            result = {
                'status': 'yes',
                'exercise_list': response_data
            }
    except Exception as e:
        result = {
            'status': 'error_request',
        }
    return result

def remove_exercise(exercise_id):
    try:
        response = requests.get(url=PLUGIN_URL + 'remove?exid=' + str(exercise_id))
        response_data = response.json()
        result = {
            'status': 'success',
            'result': response_data
        }
    except Exception as e:
        result = {
            'status': 'error_request'
        }
    return result

# exercise_detail(2)
# search_exercise('java%20programming')
# remove_exercise(1)
