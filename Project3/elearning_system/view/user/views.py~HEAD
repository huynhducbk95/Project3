# coding=utf-8
from django.shortcuts import render
import django
from django.http import HttpResponse
import json
# from elearning_system.model import User

def index(request):
    topic = ['Lập trình hướng đối tượng', 'Tin học đại cương', 'Lập trình java', 'Kỹ thuật lập trình',
             'Lập trình song song', ]
    top_user = [{
        'username': 'Username 1',
        'passed': 15,
        'message': 18,
        'contributed': 35,
    }, {
        'username': 'Username 2',
        'passed': 15,
        'message': 18,
        'contributed': 35,
    }, {
        'username': 'Username 3',
        'passed': 15,
        'message': 18,
        'contributed': 35,
    }, {
        'username': 'Username 4',
        'passed': 15,
        'message': 18,
        'contributed': 35,
    }, {
        'username': 'Username 5',
        'passed': 15,
        'message': 18,
        'contributed': 35,
    }, {
        'username': 'Username 6',
        'passed': 15,
        'message': 18,
        'contributed': 35,
    }, {
        'username': 'Username 7',
        'passed': 15,
        'message': 18,
        'contributed': 35,
    }, {
        'username': 'Username 8',
        'passed': 15,
        'message': 18,
        'contributed': 35,
    }]
    top_exercise = [{
        'name': 'Exercise 1',
        'description': 'Description for exercise is a short sentence .... ',
        'viewed': 10,
        'passed': 25,
        'messaged': 14,
    }, {
        'name': 'Exercise 2',
        'description': 'Description for exercise is a short sentence .... ',
        'viewed': 10,
        'passed': 25,
        'messaged': 14,
    }, {
        'name': 'Exercise 3',
        'description': 'Description for exercise is a short sentence .... ',
        'viewed': 10,
        'passed': 25,
        'messaged': 14,
    }, {
        'name': 'Exercise 4',
        'description': 'Description for exercise is a short sentence .... ',
        'viewed': 10,
        'passed': 25,
        'messaged': 14,
    }, ]
    result = {
        'title': 'Coding School',
        'topic_list': topic,
        'top_exercise': top_exercise,
        'top_user': top_user,
    }
    return render(request, 'elearning_system/user/index.html', {'result': result})


def list_ex_of_topic(request):
    print('x')
    return render(request, 'elearning_system/user/list_ex_of_topic.html', {'title': 'registry'})


def contact(request):
    print('x')
    return render(request, 'base.html', {'title': 'registry'})


def search(request):
    result = {

    }
    if (request.method == "GET"):
        search = request.GET.get('search', None)
        result['search'] = search

    return render(request, 'elearning_system/user/search.html', result)


class getSearchSuggestion(django.views.generic.TemplateView):
    def get(self, request, *args, **kwargs):
        key = request.GET.get('key_search',None)
        result = {
            'name':'ex 1',
            'description':'descript 1'
        }
        return HttpResponse(json.dumps(request),content_type='application/json')