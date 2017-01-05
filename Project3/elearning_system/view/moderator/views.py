from django.shortcuts import render
from elearning_system.models import Tag
from elearning_system.models import ExerciseWebServer, User, ErrorMessage
from elearning_system.central_control import check_role, render_template, check_user_is_login
from django.http import HttpResponse
import json
import databaseService as db
import plugin_api


@check_role('moderator')
def errorMessage(request):
    message_dict = []
    message_list = db.get_message_list()
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
    return render_template(request, 'elearning_system/moderator/errorMessage.html', result)


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
        if ex.approver != None and ex.tag != None:
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


@check_role('moderator')
def messageDetail(request):
    if request.method == 'GET':
        message_id = request.GET.get('message_id', None)
        errorMessage = ErrorMessage.objects.get(pk=int(message_id))
        result = {
            'exercise_id': errorMessage.exercise_reported.id,
            'exercise_name': 'Exercise name',
            'title': errorMessage.title,
            'content': errorMessage.content,
        }
        infor_menu_moderator(result, request)
        return render_template(request, 'elearning_system/moderator/messageDetail.html', result)


@check_role('moderator')
def exApproved(request):
    dict_exApproved = []

    exercise_list = ExerciseWebServer.objects.all()
    for ex in exercise_list:
        if ex.approver != None and ex.tag != None:

            result_from_plugin = plugin_api.get_exercise_plugin_detail(ex.id)
            if (result_from_plugin['status'] == 'success'):
                exercise_plugin_respone = result_from_plugin['plugin_exercise']

                dict_exApproved.append({
                    'id': ex.id,
                    'approver': ex.approver.user_name,
                    'exercise_name': exercise_plugin_respone.name,
                    'exercise_description': exercise_plugin_respone.description,
                    'tag_name': ex.tag.tag_name,
                    'contributor': ex.contributor.user_name
                })
            else :
                print "Can't get exercise detail"

    result = {
        'exApproved': dict_exApproved,
    }
    infor_menu_moderator(result, request)
    return render_template(request, 'elearning_system/moderator/exApproved.html', result)


@check_role('moderator')
def exUnapprove(request):
    dict_exUnApproved = []

    exercise_list = ExerciseWebServer.objects.all()
    for ex in exercise_list:
        if ex.approver == None:

            result_from_plugin = plugin_api.get_exercise_plugin_detail(ex.id)
            if (result_from_plugin['status'] == 'success'):
                exercise_plugin_respone = result_from_plugin['plugin_exercise']
                dict_exUnApproved.append({
                    'id': ex.id,
                    'exercise_name': exercise_plugin_respone.name,
                    'exercise_description': exercise_plugin_respone.description,
                    'contributor': ex.contributor.user_name
                })
            else:
                print "Can't get exercise detail"
    result = {
        'exUnapprove': dict_exUnApproved,
    }
    infor_menu_moderator(result, request)
    return render_template(request, 'elearning_system/moderator/exUnapprove.html', result)


@check_role('moderator')
def exNoTopic(request):
    dict_exApproved_noTopic = []
    exercise_list = ExerciseWebServer.objects.all()
    for exercise in exercise_list:
        if exercise.approver != None and exercise.tag == None:

            result_from_plugin = plugin_api.get_exercise_plugin_detail(exercise.id)
            if (result_from_plugin['status'] == 'success'):
                exercise_plugin_respone = result_from_plugin['plugin_exercise']
                dict_exApproved_noTopic.append({
                    'id': exercise.id,
                    'exercise_name': exercise_plugin_respone.name,
                    'exercise_description': exercise_plugin_respone.description,
                    'contributor': exercise.contributor.user_name,
                })
            else:
                print "Can't get exercise detail"

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
    return render_template(request, 'elearning_system/moderator/exNoTopic.html', result)


@check_role('moderator')
def detail_exUnapprove(request):
    user_name = request.session['user_name']
    moderator = User.objects.get(user_name=user_name)
    exUnapproveID = request.GET.get('exid', None)

    result_from_plugin = plugin_api.get_exercise_plugin_detail(exUnapproveID)
    if (result_from_plugin['status'] == 'success'):
        exercise_plugin_respone = result_from_plugin['plugin_exercise']
    else:
        print "Can't get exercise detail"

    tag_dict = []
    for tag in Tag.objects.all():
        tag_dict.append(tag)
    result = {
        'exercise_id': exUnapproveID,
        'exercise_name': exercise_plugin_respone.name,
        'exercise_content': exercise_plugin_respone.content,
        'exercise_testcase': 'test case list',
        'exercise_solution': exercise_plugin_respone.solution,
        'moderator_id': moderator.id,
        'tagList': tag_dict
    }
    infor_menu_moderator(result, request)
    return render_template(request, 'elearning_system/moderator/Exercise_Unapprove_Detail.html', result)


@check_role('moderator')
def upprove_exercise_status(request):
    if request.method == 'GET':
        moderator_id = request.GET.get('moderator_id', None)
        exercise_id = request.GET.get('exercise_id', None)
        tag_id = request.GET.get('tag_id', None)
        exercise = ExerciseWebServer.objects.get(pk=int(exercise_id))
        moderator = User.objects.get(pk=int(moderator_id))
        tag = Tag.objects.get(pk=int(tag_id))
        exercise.approver = moderator
        exercise.tag = tag
        exercise.contributor.contribute_number += 1
        exercise.save()
        result = {
            'result': 'successful',
            'moderator_name': moderator.user_name,
            'exercise_name': 'exercise name',
        }
        infor_menu_moderator(result, request)
        return render_template(request, 'elearning_system/moderator/upprove_exercise_status.html', result)


@check_role('moderator')
def cancel_exercise_status(request):
    if request.method == 'GET':
        moderator_id = request.GET.get('moderator_id', None)
        exercise_id = request.GET.get('exercise_id', None)
        exercise = ExerciseWebServer.objects.get(pk=int(exercise_id))
        moderator = User.objects.get(pk=int(moderator_id))
        # request to delete exercise at plugin here ...
        #
        exercise.delete()
        result = {
            'result': 'successful',
            'moderator_name': moderator.user_name,
            'exercise_name': 'exercise name',
        }
        infor_menu_moderator(result, request)
        return render_template(request, 'elearning_system/moderator/cancel_exercise_status.html', result)


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
