from django.shortcuts import render


def index(request):
    print('x')
    return render(request, 'elearning_system/user/index.html', {'title': 'registry'})

def list_ex_of_topic(request):
    print('x')
    return render(request, 'elearning_system/user/list_ex_of_topic.html', {'title': 'registry'})

def contact(request):
    print('x')
    return render(request, 'elearning_system/user/contact.html', {'title': 'registry'})