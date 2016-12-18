# coding=utf-8
from django.shortcuts import render, redirect
import django
from django.http import HttpResponse
import json
import datetime
from elearning_system.models import User, ExerciseWebServer, Tag, UserSolveExercise, Role, UserRole, \
    ErrorMessage


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
    # create database of tag
    # user = User.objects.get(pk=3)
    #
    # for tag in topic:
    #     tag_obj = Tag(tag_name=tag)
    #     tag_obj.save()
    # tag = Tag.objects.get(pk=2)
    #
    # for ex in top_exercise:
    #     ex1 = ExerciseWebServer(exercise_name=ex['name'],
    #                             exercise_descrip=ex['description'],
    #                             view_number=ex['viewed'],
    #                             contributer_id=user.id,
    #                             solve_number=ex['passed'],
    #                             created_date=datetime.datetime.now(),
    #                             tag_id=tag,
    #                             approver_id=user.id,
    #                             )
    #     ex1.save()
    # for user in top_user:
    #     us = User(user_name=user['username'],
    #               account_name=user['username'],
    #               password=user['username'],
    #               contribute_number=user['contributed'],
    #               email_address=user['username'],
    #               block_status='Active',
    #               solve_number=user['passed'])
    #     us.save()
    #
    # user_list = User.objects.all().order_by('contribute_number')
    #
    if 'username' in request.session:
        result['username'] = request.session['username']
    return render(request, 'elearning_system/user/index.html', {'result': []})


def list_ex_of_topic(request):
    # print('x')
    if request.method == 'GET':
        tag = request.GET.get('tag', None)
        exercises = ExerciseWebServer.objects.all()
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


def compare_exercise(request):
    result = {}
    if request.method == 'GET':
        option = request.GET.get('option', None)
        if option == 'View':
            value = 'view_number'
        elif option == 'Passed':
            value = 'solve_number'
        else:
            value = 'created_date'
        exercise_list = ExerciseWebServer.objects.all().order_by(value)
        print exercise_list
    return HttpResponse(json.dumps(result), content_type='application/json')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user_list = User.objects.all()
        error = False
        for user in user_list:
            if user.user_name == username and user.password == password:
                error = True
                break
        if error:
            if 'username' in request.session:
                del request.session['username']
            request.session['username'] = username
            result = {
                'result': 'successful',
            }
        else:
            result = {
                'result': 'error'
            }
        return HttpResponse(json.dumps(result), content_type='application/json')


def logout(request):
    if request.method == 'GET':
        if 'username' in request.session:
            del request.session['username']
        result = {
            'result': 'successful'
        }
        return redirect(to='index')


def registry(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user_list = User.objects.all()
        for user in user_list:
            if user.user_name == username:
                result = {
                    'result': 'error'
                }
                return HttpResponse(json.dumps(result), content_type='application')
        password = request.POST.get('password')
        email = request.POST.get('email')
        account_name = request.POST.get('account_name')
        block_status = 'Active'
        user = User(user_name=username,
                    password=password,
                    email_address=email,
                    account_name=account_name,
                    block_status=block_status)
        user.save()
        if 'username' in request.session:
            del request.session['username']
        request.session['username'] = username
        result = {
            'result': 'successful'
        }
        return HttpResponse(json.dumps(result), content_type='application/json')
