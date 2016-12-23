from django.shortcuts import render
from elearning_system import models
from django.http import HttpResponse
import json
from elearning_system.central_control import check_role, render_template, check_user_is_login

from elearning_system.models import User,Tag,Role
import admin_databaseService as db

@check_role('admin')
def manageTopic(request):
    dict_tag = []
    tag_list = db.get_tag_list()
    for tag in tag_list:
        tag_temp = {'id': tag.id, 'tag_name': tag.tag_name, 'numberOfEx': len(tag.exercisewebserver_set.all())}
        dict_tag.append(tag_temp)

    context = {}
    if request.method == "POST":

        if 'action' in request.POST:
            topicName = request.POST.get('topicName', None)
            tag = Tag.objects.get(tag_name=topicName)
            tag.delete()
            context['status'] = 'success'
            return HttpResponse(json.dumps(context), content_type='application/json')

        else:
            topicName = request.POST.get('topicName', None)
            topic_list = db.get_tag_list()
            for tag in topic_list:
                if tag.tag_name.lower() == topicName.lower():
                    context['status'] = 'error'
                    context['message'] = 'Topic name already existed!'
                    return HttpResponse(json.dumps(context), content_type='application/json')

            # tag = Tag(tag_name=topicName)
            # tag.save()
            tagID = db.create_tag(topicName)
            context['tagID'] = tagID
            context['status'] = 'success'
            return HttpResponse(json.dumps(context), content_type='application/json')



    if request.method == "GET":
        new_tagName = request.GET.get('topicName', None)
        if new_tagName != None:
            tagID = request.GET.get('tagID', None)
            topic_list = db.get_tag_list()
            for tag in topic_list:
                if tag.tag_name.lower() == new_tagName.lower():
                    context['status'] = 'error'
                    context['message'] = 'Topic name already existed. Update fail!'
                    return HttpResponse(json.dumps(context), content_type='application/json')

            # tag_change = Tag.objects.get(pk=tagID)
            # tag_change.tag_name = new_tagName
            # tag_change.save()
            db.update_tag_name(tagID,new_tagName)
            # context['tagID'] = '9'
            context['status'] = 'success'
            return HttpResponse(json.dumps(context), content_type='application/json')

    return render_template(request, 'elearning_system/admin/manageTopic.html', {'data_tag': dict_tag})

@check_role('admin')
def manageUser(request):
    user_list = db.get_all_user_list()
    user_dict = []
    normal_user_list = db.get_normal_user_list()

    for user in normal_user_list:
        temp = {'STT': user.id, 'userName': user.user_name,'fullname': user.full_name, 'email': user.email_address, 'status': user.block_status,
                'posted': user.contribute_number, 'resolved': user.solve_number}
        user_dict.append(temp)

    if request.method == "POST":
        user_name = request.POST.get('user_name',None)
        full_name = request.POST.get('full_name',None)
        password = request.POST.get('password',None)
        email_address = request.POST.get('email_address',None)
        block_status = request.POST.get('block_status',None)

        context = {}

        for user in user_list:
            if user.user_name == user_name:
                context['status'] = 'error'
                context['message'] = 'Username is already exist'
                return HttpResponse(json.dumps(context), content_type='application/json')
            if user.email_address == email_address:
                context['status'] = 'error'
                context['message'] = 'Email is already exist'
                return HttpResponse(json.dumps(context), content_type='application/json')

        # user = User(full_name=full_name,password=password,user_name=user_name,email_address=email_address,
        #             block_status=block_status)
        # user.save()
        user = db.create_user(user_name,full_name,password,email_address,block_status)
        print user
        user_temp = {'STT': user.id, 'userName': user.user_name,'fullname': user.full_name, 'email': user.email_address,
                     'status': user.block_status, 'posted': user.contribute_number, 'resolved': user.solve_number}
        user_dict.append(user_temp)
        context['newUserID'] = user.id
        context['status'] = 'success'
        return HttpResponse(json.dumps(context), content_type='application/json')

    # dict = [{'STT': 1, 'userName': 'donghm1','email': 'abc1@gmail.com', 'ID': 20, 'status': 'Active', 'posted':  15,'resolved': 30},
    #         {'STT': 2, 'userName': 'donghm2','email': 'abc2@gmail.com', 'ID': 21, 'status': 'Block', 'posted': 15, 'resolved': 30},
    #         {'STT': 3, 'userName': 'donghm3','email': 'abc3@gmail.com', 'ID': 22, 'status': 'Block', 'posted': 15, 'resolved': 30},
    #         {'STT': 4, 'userName': 'donghm4','email': 'abc4@gmail.com', 'ID': 23, 'status': 'Active', 'posted': 15, 'resolved': 30},
    #         {'STT': 5, 'userName': 'donghm5','email': 'abc5@gmail.com', 'ID': 24, 'status': 'Active', 'posted': 15, 'resolved': 30},
    #         {'STT': 6, 'userName': 'donghm6','email': 'abc6@gmail.com', 'ID': 25, 'status': 'Block', 'posted': 15, 'resolved': 30},
    #         {'STT': 7, 'userName': 'donghm7','email': 'abc7@gmail.com', 'ID': 26, 'status': 'Active', 'posted': 15, 'resolved': 30},]

    return render_template(request, 'elearning_system/admin/manageUser.html', {'dataUser': user_dict})

@check_role('admin')
def manageModerator(request):
    user_list = db.get_all_user_list()
    moderator_dict = []
    moderator_list = db.get_moderator_list()
    for moderator in moderator_list:
        moderator_dict.append(moderator)

    if request.method == "POST":
        user_name = request.POST.get('user_name',None)
        full_name = request.POST.get('full_name',None)
        password = request.POST.get('password',None)
        email_address = request.POST.get('email_address',None)
        block_status = request.POST.get('block_status',None)

        context = {}

        for user in user_list:
            if user.user_name == user_name:
                context['status'] = 'error'
                context['message'] = 'Username is already exist'
                return HttpResponse(json.dumps(context), content_type='application/json')
            if user.email_address == email_address:
                context['status'] = 'error'
                context['message'] = 'Email is already exist'
                return HttpResponse(json.dumps(context), content_type='application/json')

        # moderator = User(full_name=full_name,password=password,user_name=user_name,email_address=email_address,
        #             block_status=block_status)
        # moderator.save()
        moderator = db.create_user(user_name,full_name,password,email_address,block_status)
        # role = Role.objects.get(pk=2)
        # role.user_list.add(moderator)
        # role.save()
        db.add_moderator(moderator)
        moderator_dict.append(moderator);
        context['newModaretorID'] = moderator.id
        context['status'] = 'success'
        return HttpResponse(json.dumps(context), content_type='application/json')

    return render_template(request, 'elearning_system/admin/manageModerator.html', {'dataModerator': moderator_dict})

def change_status_user(request):
    context = {}
    if request.method == "GET":
        user_id = request.GET.get('user_id',None)
        # user = models.User.objects.get(pk=user_id)
        # if user.block_status == 'Active':
        #     user.block_status = 'Block'
        # else:
        #     user.block_status = 'Active'
        # user.save()
        db.change_user_status(user_id)
        context['status'] = 'success'
    return HttpResponse(json.dumps(context),content_type='application/json')
