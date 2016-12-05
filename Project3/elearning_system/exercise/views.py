from django.shortcuts import render


def test_code(request):
    return render(request, 'elearning_system/exercise/test_code.html',
                  {'title': 'registry'})


def slove_exercise(request):
    return render(request, 'elearning_system/exercise/solve_exercise.html',
                  {'title': 'registry'})
