from django.shortcuts import render


def test_code(request):
    print ('y')
    return render(request, 'elearning_system/exercise/test_code.html',
                  {'title': 'registry'})


def exercise_detail_without_login(request):
    print ('y')
    return render(request, 'elearning_system/exercise/exercise_detail_without_login.html',
                  {'title': 'registry'})


def exercise_detail(request):
    print ('x')
    return render(request, 'elearning_system/exercise/exercise_detail.html',
                  {'title': 'registry'})


def contribute_exercise(request):
    return render(request, 'elearning_system/exercise/contribute_exercise.html',
                  {'title': 'registry'})
