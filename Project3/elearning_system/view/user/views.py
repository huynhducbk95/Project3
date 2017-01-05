# coding=utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from elearning_system.view.user import database_services, plugin_services
from elearning_system.models import User, Role


def index(request):
    top_new_list = database_services.get_lastest_exercise_list()
    top_view_exercise_list = database_services.get_top_view_exercise_list()
    tag_list = database_services.get_tag_list()
    result = {
        'title': 'Coding School',
        'topic_list': tag_list,
        'top_view_exercise': top_view_exercise_list,
        'top_new_exercise': top_new_list,
        'length_view_exercise_list': len(top_view_exercise_list),
        'length_new_exercise_list': len(top_new_list),
    }
    check_role(result, request)
    return render(request, 'elearning_system/user/index.html', result)


def check_role(result, request):
    if 'user_name' in request.session:
        result['user_name'] = request.session['user_name']
        user = User.objects.get(user_name=request.session['user_name'])
        role_list_db = user.role_set.all()
        role_list = []
        for role in role_list_db:
            role_list.append(role.role_name)
        result['role_list'] = role_list
    return result


def list_ex_of_topic(request):
    if request.method == 'GET':
        tag = request.GET.get('tag', None)
        exercise_list = database_services.get_exercise_by_tag(int(tag))
        tag_list = database_services.get_tag_list()
        tag_db = database_services.get_tag_detail(int(tag))
        result = {
            'exercise_number': len(exercise_list),
            'exercise_list': exercise_list,
            'topic_list': tag_list,
            'tag_name': tag_db.tag_name
        }
        check_role(result, request)
        return render(request, 'elearning_system/user/list_ex_of_topic.html', result)


def ranking(request):
    if request.method == 'GET':
        user_contribute_list = database_services.get_top_user_contribute_list()
        user_solve_list = database_services.get_top_user_solve_list()
        tag_list = database_services.get_tag_list()
        result = {
            'contributor_list': user_contribute_list,
            'solve_list': user_solve_list,
            'topic_list': tag_list,
        }
        check_role(result, request)
        return render(request, 'elearning_system/user/ranking.html', result)


def quick_search(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword', None)
        response = plugin_services.search_exercise(keyword)
        if response['status'] == 'error_request' or response['status'] == 'no':
            exercise_list_result = []
            result = {
                'exercise_list': exercise_list_result,
            }
            return HttpResponse(json.dumps(result), content_type='application/json')
        exercise_list_result = []
        exercise_list = response['exercise_list']
        for exercise in exercise_list:
            exercise_info = {
                'name': exercise['name'],
                'description': exercise['description']
            }
            exercise_list_result.append(exercise_info)
        result = {
            'exercise_list': exercise_list_result,
        }
        return HttpResponse(json.dumps(result), content_type='application/json')


def search(request):
    if (request.method == "GET"):
        search_keyword = request.GET.get('search', None)
        search_option = request.GET.get('search_option', None)
        search_keyword = search_keyword.lower()
        tag_list = database_services.get_tag_list()
        response = plugin_services.search_exercise(search_keyword)
        if response['status'] != 'yes':
            exercise_list_plugin_response = []
        else:
            exercise_list_plugin_response = response['exercise_list']
        exercise_list_result = database_services.get_exercise_list_info(exercise_list_plugin_response, search_option)
        result = {
            'exercise_number': len(exercise_list_result),
            'title': 'Search',
            'keyword': search_keyword,
            'exercise_list': exercise_list_result,
            'topic_list': tag_list,
        }
        check_role(result, request)
        return render(request, 'elearning_system/user/search.html', result)


def get_exercise_pagination(request):
    result = {}
    if request.method == 'GET':
        page_compare_option = request.GET.get('page_compare', None)
        page_exercise_option = request.GET.get('page_option', None)
        page_name = request.GET.get('page_name', None)
        page_number = request.GET.get('pagination_number', None)
        exercise_list_result = database_services.sort_by_option(page_compare_option, page_exercise_option, page_name,
                                                                page_number)
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
                is_block = False
                if user.block_status == 'Block':
                    is_block = True
                is_valid = True
                break
        if is_valid:
            if is_block:
                result = {
                    'result': 'error',
                    'message': 'This account was blocked'
                }
                return render(request, 'elearning_system/user/login.html', result)
            else:
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
        user = database_services.get_user_detail(user_name)
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
        database_services.change_password_user(user_name, new_password)
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
        check_role(result, request)
        return render(request, 'elearning_system/user/user_information.html', result)

    if request.method == 'GET':
        user_name = request.GET.get('user_name', None)
        user = database_services.get_user_detail(user_name)
        result = {
            'user_name': user.user_name,
            'full_name': user.full_name,
            'email': user.email_address,
            'solved_number': user.solve_number,
            'contributed_number': user.contribute_number,
            'active_profile': 'active',
        }
        check_role(result, request)
        return render(request, 'elearning_system/user/user_information.html', result)


def registry(request):
    if request.method == 'GET':
        return render(request, 'elearning_system/user/registry.html', {})
    if request.method == 'POST':
        user_name = request.POST.get('user_name', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        full_name = request.POST.get('full_name', None)
        result = database_services.check_user_name_exist(user_name, email)
        if result['result'] == 'error':
            return HttpResponse(json.dumps(result), content_type='application/json')
        add_action = database_services.add_new_user(user_name, password, email, full_name)
        if add_action['result'] == 'success':
            result = {
                'result': 'successful',
            }
        else:
            result = {
                'result': 'error'
            }
        return HttpResponse(json.dumps(result), content_type='application/json')
