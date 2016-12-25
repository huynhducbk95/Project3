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


class PluginExercise:
    def __init__(self, name, description, content, test_case_list, solution):
        self.name = name
        self.description = description
        self.content = content
        self.test_case_list = test_case_list
        self.solution = solution


class ExerciseDetailViewModel:
    def __init__(self, exercise_id, name, description, content, contributor, solve_number, view_number, create_date,
                 test_case_list, tag):
        self.exercise_id = exercise_id
        self.name = name
        self.description = description
        self.content = content
        self.contributor = contributor
        self.solve_number = solve_number
        self.view_number = view_number
        self.create_date = create_date
        self.test_case_list = test_case_list
        self.tag = tag
