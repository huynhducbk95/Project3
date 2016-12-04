from django.shortcuts import render


def index(request):
    print('x')
    return render(request, 'elearning_system/user/index.html', {'title': 'registry'})
