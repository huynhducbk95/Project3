# coding=utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from elearning_system.models import User, ExerciseWebServer, Tag, Role
import re


def index(request):

    user_list = User.objects.all().order_by('-contribute_number')
    count = 1
    top_user_list = []
    for user in user_list:
        if count == 9:
            break
        else:
            user_top = {
                'user_name': user.user_name,
                'passed': user.solve_number,
                'contributed': user.contribute_number,
            }
            top_user_list.append(user_top)
            count += 1
    exercise_list = ExerciseWebServer.objects.all().order_by('-solve_number')
    count = 1
    top_exercise_list = []
    for exercise in exercise_list:
        if count == 18:
            break
        else:
            exercise_top = {
                'name': 'exercise x',
                'description': 'description for exercise x',
                'passed': exercise.solve_number,
                'contributor': exercise.contributor.user_name,
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
    if 'user_name' in request.session:
        result['user_name'] = request.session['user_name']
        user = User.objects.get(user_name=request.session['user_name'])
        role_list_db = user.role_set.all()
        role_list = []
        for role in role_list_db:
            role_list.append(role.role_name)
        result['role_list'] = role_list
    return render(request, 'elearning_system/user/index.html', result)


def list_ex_of_topic(request):
    if request.method == 'GET':
        tag = request.GET.get('tag', None)
        tag_db = Tag.objects.get(pk=int(tag))
        exercises = tag_db.exercisewebserver_set.all()
        exercise_list = []
        for exercise in exercises:
            exercise_info = {
                'name': 'exercise x',
                'description': 'description for exercise xx',
                'passed': exercise.solve_number,
                'contributor': exercise.contributor.user_name,
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
        if 'user_name' in request.session:
            result['user_name'] = request.session['user_name']
            user = User.objects.get(user_name=request.session['user_name'])
            role_list_db = user.role_set.all()
            role_list = []
            for role in role_list_db:
                role_list.append(role.role_name)
            result['role_list'] = role_list
        return render(request, 'elearning_system/user/list_ex_of_topic.html', result)


def ranking(request):
    if request.method == 'GET':
        user_contribute_list_db = User.objects.all().order_by('-contribute_number')
        user_solve_list_db = User.objects.all().order_by('-solve_number')
        user_contribute_list = []
        user_solve_list = []
        for user in user_contribute_list_db:
            user_infor = {
                'user_name': user.user_name,
                'contribute_number': user.contribute_number,
                'solve_number': user.solve_number,
            }
            user_contribute_list.append(user_infor)
        for user in user_solve_list_db:
            user_infor = {
                'user_name': user.user_name,
                'contribute_number': user.contribute_number,
                'solve_number': user.solve_number,
            }
            user_solve_list.append(user_infor)
        tag_list_db = Tag.objects.all()
        tag_list = []
        for tag in tag_list_db:
            tag_info = {
                'name': tag.tag_name,
                'id': tag.id
            }
            tag_list.append(tag_info)
        result = {
            'contributor_list': user_contribute_list,
            'solve_list': user_solve_list,
            'topic_list': tag_list,
        }
        if 'user_name' in request.session:
            result['user_name'] = request.session['user_name']
            user = User.objects.get(user_name=request.session['user_name'])
            role_list_db = user.role_set.all()
            role_list = []
            for role in role_list_db:
                role_list.append(role.role_name)
            result['role_list'] = role_list
        return render(request, 'elearning_system/user/ranking.html', result)


def typeahead_search(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword', None)
        exercise_list = ExerciseWebServer.objects.all()
        exercise_list_result = []
        exercise_list_db_result = []
        for exercise in exercise_list:
            if 'exercise xx'.__contains__(keyword):
                exercise_info = {
                    'name': 'exercise xx',
                    'description': 'description for exercise xx',
                    'passed': exercise.solve_number,
                    'contributor': exercise.contributor.user_name,
                    'view': exercise.view_number,
                }
                exercise_list_result.append(exercise_info)
                exercise_list_db_result.append(exercise)
        for exercise in exercise_list:
            if not exercise in exercise_list_db_result:
                if 'description for exercise'.__contains__(keyword):
                    exercise_info = {
                        'name': 'exercise',
                        'description': 'description for exercise ',
                        'passed': exercise.solve_number,
                        'contributor': exercise.contributor.user_name,
                        'view': exercise.view_number,
                    }
                    exercise_list_result.append(exercise_info)
                    exercise_list_db_result.append(exercise)
        result = {
            'exercise_list': exercise_list_result,
        }
        return HttpResponse(json.dumps(result), content_type='application/json')


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
        exercise_list = ExerciseWebServer.objects.all()
        exercise_list_result = search_action(exercise_list, search_keyword, 'search')
        result = {
            'exercise_number': len(exercise_list_result),
            'title': 'Search',
            'keyword': search_keyword,
            'exercise_list': exercise_list_result,
            'topic_list': tag_list,
        }
        if 'user_name' in request.session:
            result['user_name'] = request.session['user_name']
            user = User.objects.get(user_name=request.session['user_name'])
            role_list_db = user.role_set.all()
            role_list = []
            for role in role_list_db:
                role_list.append(role.role_name)
            result['role_list'] = role_list
        return render(request, 'elearning_system/user/search.html', result)


def search_action(exercise_list, search_keyword, option):
    exercise_list_result = []

    exercise_list_db_result = []
    for exercise in exercise_list:
        # exercise_name = exercise.exercise_name.lower()
        # if 'exercise_name'.__contains__(search_keyword):
        exercise_info = {
            'name': 'exercise xx',
            'description': 'description for exercise xx',
            'passed': exercise.solve_number,
            'contributor': exercise.contributor.user_name,
            'view': exercise.view_number,
        }
        exercise_list_result.append(exercise_info)
        exercise_list_db_result.append(exercise)
    for exercise in exercise_list:
        if not exercise in exercise_list_db_result:
            # description = exercise.exercise_description.lower()
            # if 'description'.__contains__(search_keyword):
            exercise_info = {
                'name': 'exercise',
                'description': 'description for exercise ',
                'passed': exercise.solve_number,
                'contributor': exercise.contributor.user_name,
                'view': exercise.view_number,
            }
            exercise_list_result.append(exercise_info)
            exercise_list_db_result.append(exercise)
    if option == 'search':
        return exercise_list_result
    else:
        return exercise_list_db_result


def get_exercise_pagination(request):
    result = {}
    if request.method == 'GET':
        page_compare_option = request.GET.get('page_compare', None)
        page_exercise_option = request.GET.get('page_option', None)
        page_name = request.GET.get('page_name', None)
        page_number = request.GET.get('pagination_number', None)

        if page_compare_option == 'view':
            compare_value = 'view_number'
        elif page_compare_option == 'passed':
            compare_value = 'solve_number'
        else:
            compare_value = 'created_date'

        if page_name == 'index':
            if page_compare_option == 'compare':
                compare_value = 'solve_number'
            exercise_list = ExerciseWebServer.objects.all().order_by('-' + compare_value)
        elif page_name == 'tag':
            tag = Tag.objects.get(pk=int(page_exercise_option))
            if page_compare_option == 'compare':
                exercise_list = tag.exercisewebserver_set.all()
            else:
                exercise_list = tag.exercisewebserver_set.all().order_by('-' + compare_value)
        else:  # page_name = 'search'
            if page_compare_option == 'compare':
                exercise_list_db = ExerciseWebServer.objects.all()
            else:
                exercise_list_db = ExerciseWebServer.objects.all().order_by('-' + compare_value)
            exercise_list = search_action(exercise_list_db, page_exercise_option, 'pagination')
        start_index = (int(page_number) - 1) * 5
        exercise_list_result = []
        for i in range(5):
            if start_index + i > len(exercise_list) - 1:
                break
            else:
                exercise_info = {
                    'name': 'exercise',
                    'description': 'description for exercise ',
                    'passed': exercise_list[start_index + i].solve_number,
                    'contributor': exercise_list[start_index + i].contributor.user_name,
                    'view': exercise_list[start_index + i].view_number,
                }
                exercise_list_result.append(exercise_info)
        result = {
            'exercise_list': exercise_list_result,
        }
    return HttpResponse(json.dumps(result), content_type='application/json')


def login(request):
    context = {}
    if request.method == 'GET':
        if 'next_page' in request.GET:
            context['redirect_message'] = 'Please login to access!'
        return render(request, 'elearning_system/user/login.html', context)
    if request.method == 'POST':
        user_name = request.POST.get('user_name', None)
        password = request.POST.get('password', None)
        user_list = User.objects.all()
        is_valid = False
        for user in user_list:
            if user.user_name == user_name and user.password == password:
                is_valid = True
                break
        if is_valid:
            if 'user_name' in request.session:
                del request.session['user_name']
            request.session['user_name'] = user_name
            if 'next_page' in request.GET:
                next_page = request.GET['next_page']
                return redirect(to=next_page)
            return redirect(to=index)
        else:
            result = {
                'result': 'error',
                'message': 'Username or password is wrong'
            }
            return render(request, 'elearning_system/user/login.html', result)


def logout(request):
    if request.method == 'GET':
        if 'user_name' in request.session:
            del request.session['user_name']
        return redirect(to='index')


def user_infor(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_pass', None)
        new_password = request.POST.get('new_pass', None)
        repeat_new_password = request.POST.get('re_new_pass', None)
        user_name = request.session['user_name']
        user = User.objects.get(user_name=user_name)
        if old_password != user.password:
            result = {
                'result': 'error',
                'active_profile': '',
                'active_change_pass': 'active',
                'message': 'Password is wrong'
            }
            return render(request, 'elearning_system/user/user_information.html', result)
        if new_password != repeat_new_password:
            result = {
                'result': 'error',
                'active_profile': '',
                'active_change_pass': 'active',
                'message': 'Repeat password is wrong'
            }
            return render(request, 'elearning_system/user/user_information.html', result)
        user.password = new_password
        user.save()
        result = {
            'result': 'successful', 'user_name': user.user_name,
            'full_name': user.full_name,
            'email': user.email_address,
            'solved_number': user.solve_number,
            'contributed_number': user.contribute_number,
            'active_profile': 'active',
            'active_change_pass': '',
            'message': 'Change password is successful'
        }
        if 'user_name' in request.session:
            result['user_name'] = request.session['user_name']
            user = User.objects.get(user_name=request.session['user_name'])
            role_list_db = user.role_set.all()
            role_list = []
            for role in role_list_db:
                role_list.append(role.role_name)
            result['role_list'] = role_list
        return render(request, 'elearning_system/user/user_information.html', result)

    if request.method == 'GET':
        user_name = request.GET.get('user_name', None)
        user = User.objects.get(user_name=user_name)
        result = {
            'user_name': user.user_name,
            'full_name': user.full_name,
            'email': user.email_address,
            'solved_number': user.solve_number,
            'contributed_number': user.contribute_number,
            'active_profile': 'active',
        }
        if 'user_name' in request.session:
            result['user_name'] = request.session['user_name']
            user = User.objects.get(user_name=request.session['user_name'])
            role_list_db = user.role_set.all()
            role_list = []
            for role in role_list_db:
                role_list.append(role.role_name)
            result['role_list'] = role_list
        return render(request, 'elearning_system/user/user_information.html', result)


def registry(request):
    if request.method == 'GET':
        return render(request, 'elearning_system/user/registry.html', {})
    if request.method == 'POST':
        user_name = request.POST.get('user_name', None)
        user_list = User.objects.all()
        password = request.POST.get('password',None)
        email = request.POST.get('email',None)
        full_name = request.POST.get('full_name',None)
        for user in user_list:
            if user.user_name == user_name:
                result = {
                    'result': 'error',
                    'message': 'Username is already exist'
                }
                return HttpResponse(json.dumps(result),content_type='application/json')
            if user.email_address == email:
                result = {
                    'result': 'error',
                    'message': 'Email address is already exist'
                }
                return HttpResponse(json.dumps(result), content_type='application/json')
        block_status = 'Active'
        user = User(user_name=user_name,
                    password=password,
                    email_address=email,
                    full_name=full_name,
                    block_status=block_status)

        user.save()
        role_user = Role.objects.get(pk=3)
        role_user.user_list.add(user)
        result = {
            'result': 'successful',
        }
        return HttpResponse(json.dumps(result), content_type='application/json')
