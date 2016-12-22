from django.shortcuts import render
from elearning_system.models import Tag
from elearning_system.models import ExerciseWebServer, User, ErrorMessage
from django.http import HttpResponse
import json


def errorMessage(request):
    message_dict = []
    message_list = ErrorMessage.objects.all()
    for message in message_list:
        message_dict.append({
            'id': message.id,
            'title': message.title,
            'content': message.content,
            'reporter': message.reporter.user_name,
            'exercise_name': 'name of exercise',
        })
    result = {
        'messages': message_dict,
    }
    infor_menu_moderator(result, request)
    return render(request, 'elearning_system/moderator/errorMessage.html', result)


def infor_menu_moderator(result, request):
    role_list = []
    if 'user_name' in request.session:
        result['user_name'] = request.session['user_name']
        user = User.objects.get(user_name=request.session['user_name'])
        roles = user.role_set.all()
        for role in roles:
            role_list.append(role.role_name)
        result['role_list'] = role_list
    error_message_list = ErrorMessage.objects.all()
    exercise_notag_number = 0
    exercise_list = ExerciseWebServer.objects.all()
    for exercise in exercise_list:
        if exercise.approver != None and exercise.tag == None:
            exercise_notag_number += 1
    exercise_approved_number = 0
    for ex in exercise_list:
        if ex.approver != None:
            exercise_approved_number += 1
    exercise_unapprove_number = 0
    for ex in exercise_list:
        if ex.approver == None:
            exercise_unapprove_number += 1
    result['exercise_notag_number'] = exercise_notag_number
    result['exercise_unapprove_number'] = exercise_unapprove_number
    result['exercise_approved_number'] = exercise_approved_number
    result['error_message_number'] = len(error_message_list)
    return result


def messageDetail(request):
    if request.method == 'GET':
        message_id = request.GET.get('message_id', None)
        errorMessage = ErrorMessage.objects.get(pk=int(message_id))
        result = {
            'exercise_id': errorMessage.exercise_report.id,
            'exercise_name': 'Exercise name',
            'title': errorMessage.title,
            'content': errorMessage.content,
        }
        infor_menu_moderator(result, request)
        return render(request, 'elearning_system/moderator/messageDetail.html', result)


def exApproved(request):
    dict_exApproved = []

    exercise_list = ExerciseWebServer.objects.all()
    for ex in exercise_list:
        if ex.approver != None:
            if ex.tag == None:
                tag = 'No tag'
            else:
                tag = ex.tag.tag_name
            dict_exApproved.append({
                'id': ex.id,
                'approver': ex.approver.user_name,
                'exercise_name': 'exercise name',
                'exercise_description': 'description of exercise',
                'tag_name': tag,
                'contributor': ex.contributor.user_name
            })
    result = {
        'exApproved': dict_exApproved,
    }
    infor_menu_moderator(result, request)
    return render(request, 'elearning_system/moderator/exApproved.html', result)


def exUnapprove(request):
    dict_exUnApproved = []

    exercise_list = ExerciseWebServer.objects.all()
    for ex in exercise_list:
        if ex.approver == None:
            dict_exUnApproved.append({
                'id': ex.id,
                'exercise_name': 'exercise name',
                'exercise_description': ' description for exercise',
                'contributor': ex.contributor.user_name
            })
    result = {
        'exUnapprove': dict_exUnApproved,
    }
    infor_menu_moderator(result, request)
    return render(request, 'elearning_system/moderator/exUnapprove.html', result)


def exNoTopic(request):
    dict_exApproved_noTopic = []
    exercise_list = ExerciseWebServer.objects.all()
    for exercise in exercise_list:
        if exercise.approver != None and exercise.tag == None:
            dict_exApproved_noTopic.append({
                'id': exercise.id,
                'exercise_name': 'exercise name',
                'exercise_content': 'content of exercise',
                'exercise_description': 'description of exercise',
                'contributor': exercise.contributor.user_name,
            })
    tags = Tag.objects.all()
    tag_list = []
    for tag in tags:
        tag_list.append({
            'id': tag.id,
            'tag_name': tag.tag_name
        })
    result = {
        'exNoTopic': dict_exApproved_noTopic,
        'tags': tag_list
    }
    infor_menu_moderator(result, request)
    return render(request, 'elearning_system/moderator/exNoTopic.html', result)


def detail_exUnapprove(request):
    user_name = request.session['user_name']
    moderator = User.objects.get(user_name=user_name)
    exUnapproveID = request.GET.get('exid', None)
    exUnapprove = ExerciseWebServer.objects.get(pk=exUnapproveID)

    result = {
        'exercise_id': exUnapprove.id,
        'exercise_name': 'exercise_name',
        'exercise_content': 'content of exercise has id ' + str(exUnapprove.id),
        'exercise_testcase': ['testcase 1 of exercise', 'testcase 2 of exercise', 'testcase 3 of exercise',
                              'testcase 4 of exercise'],
        'moderator_id': moderator.id,
    }
    infor_menu_moderator(result, request)
    return render(request, 'elearning_system/moderator/Exercise_Unapprove_Detail.html', result)


def upprove_exercise_status(request):
    if request.method == 'GET':
        moderator_id = request.GET.get('moderator_id', None)
        exercise_id = request.GET.get('exercise_id', None)
        exercise = ExerciseWebServer.objects.get(pk=int(exercise_id))
        moderator = User.objects.get(pk=int(moderator_id))
        exercise.approver = moderator
        exercise.save()
        result = {
            'result': 'successful',
            'moderator_name': moderator.user_name,
            'exercise_name': 'exercise name',
        }
        infor_menu_moderator(result, request)
        return render(request, 'elearning_system/moderator/upprove_exercise_status.html', result)


def detail_exApproved(request):
    user_name = request.session['user_name']
    moderator = User.objects.get(user_name=user_name)
    exapproveID = request.GET.get('exApproved_id', None)
    exapprove = ExerciseWebServer.objects.get(pk=exapproveID)
    tag_list = []
    for tag in Tag.objects.all():
        tag_list.append({
            'id': tag.id,
            'tag_name': tag.tag_name
        })
    result = {
        'id': exapprove.id,
        'exercise_name': 'exercise_name',
        'exercise_content': 'content of exercise has id ' + str(exapprove.id),
        'exercise_testcase': ['testcase 1 of exercise', 'testcase 2 of exercise', 'testcase 3 of exercise',
                              'testcase 4 of exercise'],
        'moderator_id': moderator.id,
        'tag_list': tag_list,
    }
    infor_menu_moderator(result, request)
    return render(request, 'elearning_system/moderator/Exercise_Approved_Detail.html', result)


def add_tag(request):
    if request.method == 'POST':
        tag_id = request.POST.get('tag_id', None)
        exercise_id = request.POST.get('exercise_id', None)
        exercise = ExerciseWebServer.objects.get(pk=int(exercise_id))
        tag = Tag.objects.get(pk=int(tag_id))
        exercise.tag = tag
        exercise.save()
        result = {
            'result_add': 'sucessful',
            'message': 'Add ' + 'exercise name' + ' to ' + tag.tag_name + ' is successful'
        }
        return HttpResponse(json.dumps(result), content_type='application/json')
