# coding=utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json

from elearning_system.models import User, ExerciseWebServer, Tag, Role


def index(request):
    role_moderator = Role.objects.get(pk=2)
    user_test = User.objects.get(pk=1)
    role_moderator.user_list.add(user_test)

    user_list = User.objects.all().order_by('-contribute_number')
    count = 1
    top_user_list = []
    for user in user_list:
        if count == 9:
            break
        else:
            user_top = {
                'username': user.user_name,
                'passed': user.solve_number,
                'contributed': user.contribute_number,
            }
            top_user_list.append(user_top)
            count += 1
    exercise_list = ExerciseWebServer.objects.all().order_by('-solve_number')
    count = 1
    top_exercise_list = []
    for exercise in exercise_list:
        if count == 5:
            break
        else:
            exercise_top = {
                'name': exercise.exercise_name,
                'description': exercise.exercise_description,
                'passed': exercise.solve_number,
                'contributor': exercise.contributer_id.user_name,
                'view': exercise.view_number,
            }
            top_exercise_list.append(exercise_top)
            count += 1
    tag_list_db = Tag.objects.all()
    tag_list = []
    for tag in tag_list_db:
        tag_info = {
            'name': tag.tag_name,
            'id': tag.id
        }
        tag_list.append(tag_info)
    result = {
        'title': 'Coding School',
        'topic_list': tag_list,
        'top_exercise': top_exercise_list,
        'top_user': top_user_list,
        'length': len(top_exercise_list),
    }
    context = {
        'account_name': 'account_name',
        'is_login': 'true',
        'user_role_list': [
            'admin',
            'moderator',
            'user'
        ]
    }
    role_list = []
    if 'is_login' in context:
        for role in context['user_role_list']:
            role_list.append(role)
        result['username'] = context['account_name']
        result['role_list'] = role_list
    return render(request, 'elearning_system/user/index.html', {'result': result})


def list_ex_of_topic(request):
    if request.method == 'GET':
        tag = request.GET.get('tag', None)
        exercises = ExerciseWebServer.objects.all()
        exercise_list = []
        for exercise in exercises:
            if exercise.tag_id.id == int(tag):
                exercise_info = {
                    'name': exercise.exercise_name,
                    'description': exercise.exercise_description,
                    'passed': exercise.solve_number,
                    'contributor': exercise.contributer_id.user_name,
                    'view': exercise.view_number,
                }
                exercise_list.append(exercise_info)
        tag_list_db = Tag.objects.all()
        tag_list = []
        tag_db = Tag.objects.get(pk=tag)
        for tag in tag_list_db:
            tag_info = {
                'name': tag.tag_name,
                'id': tag.id
            }
            tag_list.append(tag_info)
        result = {
            'exercise_number': len(exercise_list),
            'exercise_list': exercise_list,
            'topic_list': tag_list,
            'tag_name': tag_db.tag_name
        }
        return render(request, 'elearning_system/user/list_ex_of_topic.html', {'result': result})


def contact(request):
    print('x')
    return render(request, 'base.html', {'title': 'registry'})


def search(request):
    if (request.method == "GET"):
        search_keyword = request.GET.get('search', None)
        search_keyword = search_keyword.lower()
        tag_list_db = Tag.objects.all()
        tag_list = []
        for tag in tag_list_db:
            tag_info = {
                'name': tag.tag_name,
                'id': tag.id
            }
            tag_list.append(tag_info)

            #     search by keyword
        exercise_list = ExerciseWebServer.objects.all()
        exercise_list_result = []
        exercise_list_db_result = []
        for exercise in exercise_list:
            exercise_name = exercise.exercise_name.lower()
            if exercise_name.__contains__(search_keyword):
                exercise_info = {
                    'name': exercise.exercise_name,
                    'description': exercise.exercise_description,
                    'passed': exercise.solve_number,
                    'contributor': exercise.contributer_id.user_name,
                    'view': exercise.view_number,
                }
                exercise_list_result.append(exercise_info)
                exercise_list_db_result.append(exercise)
        for exercise in exercise_list:
            if not exercise in exercise_list_db_result:
                description = exercise.exercise_description.lower()
                if description.__contains__(search_keyword):
                    exercise_info = {
                        'name': exercise.exercise_name,
                        'description': exercise.exercise_description,
                        'passed': exercise.solve_number,
                        'contributor': exercise.contributer_id.user_name,
                        'view': exercise.view_number,
                    }
                    exercise_list_result.append(exercise_info)
                    exercise_list_db_result.append(exercise)
        result = {
            'exercise_number': len(exercise_list_result),
            'title': 'Search',
            'keyword': search_keyword,
            'exercise_list': exercise_list_result,
            'topic_list': tag_list,
        }
        return render(request, 'elearning_system/user/search.html', {'result': result})


def compare_exercise(request):
    result = {}
    if request.method == 'GET':
        option = request.GET.get('option', None)
        page = request.GET.get('page', None)
        if option == 'view':
            value = 'view_number'
        elif option == 'passed':
            value = 'solve_number'
        else:
            value = 'created_date'
        if page == 'index':
            exercise_list = ExerciseWebServer.objects.all().order_by('-' + value)
        else:
            exercise_list = []
        exercise_list_result = []
        for exercise in exercise_list:
            exercise_info = {
                'name': exercise.exercise_name,
                'description': exercise.exercise_description,
                'passed': exercise.solve_number,
                'contributor': exercise.contributer_id.user_name,
                'view': exercise.view_number,
            }
            exercise_list_result.append(exercise_info)
        result = {
            'exercise_list': exercise_list_result,
        }
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
            user_obj = User.objects.get(user_name=username)
            result = {
                'result': 'successful',
                'account_name': user_obj.account_name,
            }
        else:
            result = {
                'result': 'error'
            }
        return HttpResponse(json.dumps(result), content_type='application/json')


def logout(request):
    if request.method == 'GET':
        user = None
        if 'user_name' in request.session:
            user = request.session['user_name']
            del request.session['user_name']
        user_obj = User.objects.get(account_name=user)
        result = {
            'result': 'successful',
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
        if 'user_name' in request.session:
            del request.session['user_name']
        request.session['user_name'] = username
        result = {
            'result': 'successful',
            'account_name': account_name,
        }
        return HttpResponse(json.dumps(result), content_type='application/json')
