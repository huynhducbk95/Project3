import requests
import json
from requests.adapters import ConnectionError
import datetime

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
    def __init__(self, status, test_case_result, message):
        self.status = status
        self.test_case_result_list = test_case_result
        self.message = message


def _convert_test_case_list(test_case_list_input):
    converted_test_case_list = []
    for test_case in test_case_list_input:
        param_arr = test_case.param_arr
        param_converted_string = ''
        for param in param_arr:
            param_converted_string = param_converted_string + param + '\n'
        if len(param_converted_string) > 2:
            param_converted_string = param_converted_string[:-1]
        value = test_case.value
        converted_test_case_list.append({'params': param_converted_string, 'result': value})
    return converted_test_case_list


def test_code(check_code_data):
    endpoint = u'http://' + PLUGIN_IP + '/plugin/testcode'
    source_code = check_code_data.solution.solution_code
    language = check_code_data.solution.solution_language
    test_case_list = _convert_test_case_list(check_code_data.test_case)
    api_body = {
        'language': language,
        'sourceCode': source_code,
        'testcases': test_case_list
    }
    try:
        response = requests.post(endpoint, json=api_body)
        data = response.json()

        print response

    except Exception as e:
        return TestCodeResult('success', ['p', 'p', 'f', 'f', 'f', 'f', 'p', 'f', 'f', 'p'], 'no message')





        #
        #
        # def get_container_detail(container_id, date_from=None, date_to=None):
        #     cadvisor_endpoint = u'http://' + host_ip +\
        #         ":stats/" + container_id + "?type=docker"
        #     docker_endpoint = "tcp://" + host_ip + ":2376"
        #     container_data = {"id": container_id}
        #     try:
        #         cli = Client(base_url=docker_endpoint)
        #         container_data['name'] = cli.containers(
        #             filters={"id": container_id})[0]['Names'][0]
        #         resp, reply_body = request(cadvisor_endpoint, method="GET", body={})
        #         status_code = resp.status_code
        #         if status_code in (requests.codes.ok,
        #                            requests.codes.created,
        #                            requests.codes.accepted,
        #                            requests.codes.no_content):
        #             container_data['realtime_data'] = json.loads(reply_body)
        #
        #             return container_data
        #         else:
        #             return "Error"
        #     except Exception:
        #         return "Error"
        #
        #
        # def get_container_list(host_ip):
        #     endpoint = "tcp://" + host_ip + ":2376"
        #     try:
        #         cli = Client(base_url=endpoint)
        #         return cli.containers()
        #     except Exception:
        #         return "Error"


# url = u'http://45.63.50.197/plugin/testcode'
#
# url_p = 'http://45.63.50.197/plugin/detail?exid=1'
# x = requests.get(url_p)
# y = x.json()
# pass
