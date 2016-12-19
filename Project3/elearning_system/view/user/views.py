# coding=utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json

from elearning_system.models import User, ExerciseWebServer, Tag


def index(request):
    # role_admin = Role.objects.get(pk=1)
    # role_moderator = Role.objects.get(pk=2)
    # role_user = Role.objects.get(pk=3)
    #
    # for user in User.objects.all():
    #     role_user.user_list.add(user)
    # user1 = User.objects.get(pk=1)
    # role_admin.user_list.add(user1)
    # role_moderator.user_list.add(user1)
    # user2 = User.objects.get(pk=2)
    # role_moderator.user_list.add(user2)
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
        if count == 10:
            break
        else:
            exercise_top = {
                'name': 'exercise x',
                'description': 'description for exercise x',
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


    if 'full_name' in request.session:
        result['full_name'] = request.session['full_name']
        user = User.objects.get(full_name=request.session['full_name'])
        role_list_db = user.role_set.all()
        role_list = []
        for role in role_list_db:
            role_list.append(role.role_name)
        result['role_list'] = role_list
    return render(request, 'elearning_system/user/index.html', result)


def list_ex_of_topic(request):
    if request.method == 'GET':
        tag = request.GET.get('tag', None)
        exercises = ExerciseWebServer.objects.all()
        exercise_list = []
        for exercise in exercises:
            if exercise.tag_id.id == int(tag):
                exercise_info = {
                    'name': 'exercise x',
                    'description': 'description for exercise xx',
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
        return render(request, 'elearning_system/user/list_ex_of_topic.html', result)


def contact(request):

    print('x')
    return render(request, 'elearning_system/user/contact.html', {'title': 'registry'})


def typeahead_search(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword', None)
        exercise_list = ExerciseWebServer.objects.all()
        exercise_list_result = []
        exercise_list_db_result = []
        for exercise in exercise_list:
            # exercise_name = exercise.exercise_name.lower()
            if 'exercise xx'.__contains__(keyword):
                exercise_info = {
                    'name': 'exercise xx',
                    'description': 'description for exercise xx',
                    'passed': exercise.solve_number,
                    'contributor': exercise.contributer_id.user_name,
                    'view': exercise.view_number,
                }
                exercise_list_result.append(exercise_info)
                exercise_list_db_result.append(exercise)
        for exercise in exercise_list:
            if not exercise in exercise_list_db_result:
                # description = exercise.exercise_description.lower()
                if 'description for exercise'.__contains__(keyword):
                    exercise_info = {
                        'name': 'exercise',
                        'description': 'description for exercise ',
                        'passed': exercise.solve_number,
                        'contributor': exercise.contributer_id.user_name,
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
        exercise_list_result = []

        exercise_list_db_result = []
        for exercise in exercise_list:
            exercise_name = exercise.exercise_name.lower()
            if exercise_name.__contains__(search_keyword):
                exercise_info = {
                    'name': 'exercise xx',
                    'description': 'description for exercise xx',
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
                        'name': 'exercise',
                        'description': 'description for exercise ',
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
        return render(request, 'elearning_system/user/search.html', result)


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
                'name': 'exercise',
                'description': 'description for exercise ',
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
    context={}
    if request.method == 'GET':
        if 'next_page' in request.GET:
            context['redirect_message'] = 'Please login to access!'
        return render(request, 'elearning_system/user/login.html',context)
    if request.method == 'POST':
        user_name = request.POST.get('user_name', None)
        password = request.POST.get('password', None)
        user_list = User.objects.all()
        is_valid = False

        user_obj = None
        for user in user_list:
            if user.user_name == user_name and user.password == password:
                is_valid = True
                user_obj = user
                break
        if is_valid:
            if 'full_name' in request.session:
                del request.session['full_name']
            request.session['full_name'] = user_obj.full_name
            return redirect(to=index)
        else:
            result = {
                'result': 'error',
                'message': 'Username or password is wrong'
            }
            return render(request, 'elearning_system/user/login.html', result)



def logout(request):
    if request.method == 'GET':
        if 'full_name' in request.session:
            del request.session['full_name']
        return redirect(to='index')


def registry(request):
    if request.method == 'GET':
        return render(request, 'elearning_system/user/registry.html', {})
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_list = User.objects.all()
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        for user in user_list:
            if user.user_name == user_name:
                result = {
                    'result': 'error',
                    'message': 'Username is already exist'
                }
                return render(request, 'elearning_system/user/registry.html', result)
            if user.email_address == email:
                result = {
                    'result': 'error',
                    'message': 'Email is already exist'
                }
                return render(request, 'elearning_system/user/registry.html', result)

        if password != repassword:
            result = {
                'result': 'error',
                'message': 'Repassword is wrong'
            }
            return render(request, 'elearning_system/user/registry.html', result)

        block_status = 'Active'
        user = User(user_name=user_name,
                    password=password,
                    email_address=email,
                    full_name=full_name,
                    block_status=block_status)
        user.save()
        return redirect(to=index)
