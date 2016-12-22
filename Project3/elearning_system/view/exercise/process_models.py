class TestCase:
    def __init__(self, param_arr, value):
        self.param_arr = param_arr
        self.value = value


class Solution:
    def __init__(self, solution_code, solution_language):
        self.solution_code = solution_code
        self.solution_language = solution_language


class CheckCodeData:
    def __init__(self, test_case, solution):
        self.test_case = test_case
        self.solution = solution
