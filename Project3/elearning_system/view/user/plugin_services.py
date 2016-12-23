import requests
import json

PLUGIN_URL = 'http://45.63.50.197/plugin/'


def exercise_detail(exercise_id):
    # try:
    #     response = requests.get(url=PLUGIN_URL + 'detail?exid=' + str(exercise_id))
    #     response_data = json.loads(response.content)
    #     if 'status' in response_data:
    #         result = {
    #             'status': 'error'
    #         }
    #     else:
    #         result = {
    #             'status': 'success',
    #             'exercise': response
    #         }
    # except Exception as e:
    #     result = {
    #         'status': 'error_request'
    #     }
    # return result
    result = {
        'status': 'success',
        'exercise': {
            'id': exercise_id,
            'name': 'exercise name',
            'description': 'description for exercise'
        }
    }
    return result


def search_exercise(search_keyword):
    # try:
    #     response = requests.get(url=PLUGIN_URL + 'search?keyword=' + search_keyword)
    #     response_data = json.loads(response.content)
    #     if 'status' in response_data:
    #         result = {
    #             'status': 'no',
    #         }
    #     else:
    #         result = {
    #             'status': 'yes',
    #             'exercise_list': response_data
    #         }
    # except Exception as e:
    #     result = {
    #         'status': 'error_request',
    #     }
    # return result
    result = {
        'status':'yes',
        'exercise_list':[{"id":3,"name":"java programming language","description":"balsl","content":"ahaha"},
                         {"id":2,"name":"test code","description":"multiple java programming thread","content":"nothing"}]
    }
    return result

def remove_exercise(exercise_id):
    try:
        response = requests.get(url=PLUGIN_URL + 'remove?exid=' + str(exercise_id))
        response_data = json.loads(response.content)
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
