from django.shortcuts import render
from elearning_system import models
from django.http import HttpResponse
import json

from elearning_system.models import User,Tag


def manageTopic(request):
    # dict = [{'STT': 1, 'topicName': 'Java1','numberOfEx':20},
    #         {'STT': 2, 'topicName': 'Java2', 'numberOfEx': 20},
    #         {'STT': 3, 'topicName': 'Java3', 'numberOfEx': 20},
    #         {'STT': 4, 'topicName': 'Java4', 'numberOfEx': 20},
    #         {'STT': 5, 'topicName': 'Java5', 'numberOfEx': 20},
    #         {'STT': 6, 'topicName': 'Java6', 'numberOfEx': 20},
    #         {'STT': 7, 'topicName': 'Java7', 'numberOfEx': 20}]

    dict_tag = []
    tag_list = Tag.objects.all()
    for tag in tag_list:
        tag_temp = {'id':tag.id,'tag_name':tag.tag_name,'numberOfEx':len(tag.exercisewebserver_set.all())}
        dict_tag.append(tag_temp)

    return render(request, 'elearning_system/admin/manageTopic.html', {'data': dict_tag})

def manageUser(request):
    demo = []
    user_list = User.objects.all()
    for user in user_list:
        temp = {'STT': user.id, 'userName': user.user_name,'fullname': user.full_name, 'email': user.email_address, 'status': user.block_status,
                'posted': user.contribute_number, 'resolved': user.solve_number}
        demo.append(temp)

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

        user = User(full_name=full_name,password=password,user_name=user_name,email_address=email_address,
                    block_status=block_status)
        user.save()
        print user
        user_temp = {'STT': user.id, 'userName': user.user_name,'fullname': user.full_name, 'email': user.email_address,
                     'status': user.block_status, 'posted': user.contribute_number, 'resolved': user.solve_number}
        demo.append(user_temp);
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

    return render(request, 'elearning_system/admin/manageUser.html', {'dataUser': demo})






def manageModerator(request):
    dict = [{'STT': 1, 'userName': 'donghm1','email': 'abc1@gmail.com','fullName':'Ha Manh Dong 1', 'ID': 20, 'status': 'Active'},
            {'STT': 2, 'userName': 'donghm2','email': 'abc2@gmail.com','fullName':'Ha Manh Dong 2', 'ID': 21, 'status': 'Block'},
            {'STT': 3, 'userName': 'donghm3','email': 'abc3@gmail.com','fullName':'Ha Manh Dong 3', 'ID': 22, 'status': 'Block'},
            {'STT': 4, 'userName': 'donghm4','email': 'abc4@gmail.com','fullName':'Ha Manh Dong 4', 'ID': 23, 'status': 'Active'},
            {'STT': 5, 'userName': 'donghm5','email': 'abc5@gmail.com','fullName':'Ha Manh Dong 5', 'ID': 24, 'status': 'Active'},
            {'STT': 6, 'userName': 'donghm6','email': 'abc6@gmail.com','fullName':'Ha Manh Dong 6', 'ID': 25, 'status': 'Block'},
            {'STT': 7, 'userName': 'donghm7','email': 'abc7@gmail.com','fullName':'Ha Manh Dong 7', 'ID': 26, 'status': 'Active'},]

    return render(request, 'elearning_system/admin/manageModerator.html', {'dataModerator': dict})

def change_status_user(request):
    context = {}
    if request.method == "GET":
        user_id = request.GET.get('user_id',None)
        user = models.User.objects.get(pk=user_id)
        if user.block_status == 'Active':
            user.block_status = 'Block'
        else:
            user.block_status = 'Active'
        user.save()
        context['status'] = 'success'
    return HttpResponse(json.dumps(context),content_type='application/json')
