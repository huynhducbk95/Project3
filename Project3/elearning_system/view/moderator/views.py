from django.shortcuts import render
from elearning_system.models import Tag
from elearning_system.models import ExerciseWebServer,User,ErrorMessage


# ExerciseWebServer_list = ExerciseWebServer.objects.all()
# for ex in ExerciseWebServer_list:
#     print  ex.approver_id.account_name

from random import randint
#
# for i in range(20):
#     eror = ErrorMessage(title='title '+str(i+1),
#                         content='content for message '+ str(i+1),
#                         reporter_id=User.objects.get(pk=randint(1,6)),
#                         reported_exercise_id=ExerciseWebServer.objects.get(pk=randint(1,10)))
#     eror.save()

# exApproved_list = ExerciseWebServer.objects.all()
# for ex in exApproved_list:
#     if hasattr(ex.approver_id, 'user_name'):
#
#         ex.tag_id = Tag.objects.get(pk=randint(1,6))
#         ex.save()
        # print ex.tag_id.tag_name

def errorMessage(request):

    message_dict = []
    message_list = ErrorMessage.objects.all()
    for message in message_list:
        message_dict.append(message)

    messages = [
        {'STT': 1, 'id': 122, 'title': 'Loi logic bai tap 1', 'userSend': 'donghm1', 'exName': 'Tim so hoan hao1',
         'idEx': 30},
        {'STT': 2, 'id': 123, 'title': 'Loi logic bai tap 2', 'userSend': 'donghm2', 'exName': 'Tim so hoan hao2',
         'idEx': 31},
        {'STT': 3, 'id': 124, 'title': 'Loi logic bai tap 3', 'userSend': 'donghm3', 'exName': 'Tim so hoan hao3',
         'idEx': 32},
        {'STT': 4, 'id': 125, 'title': 'Loi logic bai tap 4', 'userSend': 'donghm4', 'exName': 'Tim so hoan hao4',
         'idEx': 33},
        {'STT': 5, 'id': 126, 'title': 'Loi logic bai tap 5', 'userSend': 'donghm5', 'exName': 'Tim so hoan hao5',
         'idEx': 34},
        {'STT': 6, 'id': 127, 'title': 'Loi logic bai tap 6', 'userSend': 'donghm6', 'exName': 'Tim so hoan hao6',
         'idEx': 35},
        {'STT': 7, 'id': 128, 'title': 'Loi logic bai tap 7', 'userSend': 'donghm7', 'exName': 'Tim so hoan hao7',
         'idEx': 36},
        {'STT': 8, 'id': 129, 'title': 'Loi logic bai tap 8', 'userSend': 'donghm8', 'exName': 'Tim so hoan hao8',
         'idEx': 37}]

    return render(request, 'elearning_system/moderator/errorMessage.html', {'messages': message_dict})


def messageDetail(request):
    if request.method == 'GET':
        message_id = request.GET.get('message_id',None)
        # errorMessage = ErrorMessage.objects.get(pk=int(message_id))
        result ={
            'exercise_name': 'Exercise name',
            'title': 'Title message',
            'content': 'This is content for message'
        }
        return render(request, 'elearning_system/moderator/messageDetail.html',result)


def exApproved(request):

    dict_exApproved = []

    exApproved_list = ExerciseWebServer.objects.all()
    for ex in exApproved_list:
        if ex.approver_id != None:
        # if hasattr(ex.approver_id, 'user_name'):
            # temp = {'STT': ex.id, 'exName': ex.exercise_name, 'exAuthor': ex.contributer_id.account_name}
            dict_exApproved.append(ex)

    exApproved = [
        {'STT': 1, 'id': 122, 'exName': 'Tim so hoan hao1', 'exTopic': 'Java1', 'exAuthor': 'donghm1', 'exViews': 30},
        {'STT': 2, 'id': 123, 'exName': 'Tim so hoan hao2', 'exTopic': 'Java2', 'exAuthor': 'donghm2', 'exViews': 31},
        {'STT': 3, 'id': 124, 'exName': 'Tim so hoan hao3', 'exTopic': 'Java3', 'exAuthor': 'donghm3', 'exViews': 32},
        {'STT': 4, 'id': 125, 'exName': 'Tim so hoan hao4', 'exTopic': 'Java4', 'exAuthor': 'donghm4', 'exViews': 33},
        {'STT': 5, 'id': 126, 'exName': 'Tim so hoan hao5', 'exTopic': 'Java5', 'exAuthor': 'donghm5', 'exViews': 34},
        {'STT': 6, 'id': 127, 'exName': 'Tim so hoan hao6', 'exTopic': 'Java6', 'exAuthor': 'donghm6', 'exViews': 35},
        {'STT': 7, 'id': 128, 'exName': 'Tim so hoan hao7', 'exTopic': 'Java7', 'exAuthor': 'donghm7', 'exViews': 36},
        {'STT': 8, 'id': 129, 'exName': 'Tim so hoan hao8', 'exTopic': 'Java8', 'exAuthor': 'donghm8', 'exViews': 37},
        {'STT': 9, 'id': 130, 'exName': 'Tim so hoan hao9', 'exTopic': 'Java9', 'exAuthor': 'donghm9', 'exViews': 38},
    ]

    return render(request, 'elearning_system/moderator/exApproved.html', {'exApproved': dict_exApproved})


def exUnapprove(request):
    dict_exUnapprove = []

    exUnapprove_list = ExerciseWebServer.objects.all()
    for ex in exUnapprove_list:
        if hasattr(ex.approver_id,'user_name') is False:
            temp = {'STT': ex.id, 'exName': 'Fake exercise name', 'exAuthor': ex.contributer_id.user_name}
            dict_exUnapprove.append(temp)

    exUnapprove = [
        {'STT': 1, 'id': 122, 'exName': 'Tim so hoan hao1', 'exTopic': 'Java1', 'exAuthor': 'donghm1'},
        {'STT': 2, 'id': 123, 'exName': 'Tim so hoan hao2', 'exTopic': 'Java2', 'exAuthor': 'donghm2'},
        {'STT': 3, 'id': 124, 'exName': 'Tim so hoan hao3', 'exTopic': 'Java3', 'exAuthor': 'donghm3'},
        {'STT': 4, 'id': 125, 'exName': 'Tim so hoan hao4', 'exTopic': 'Java4', 'exAuthor': 'donghm4'},
        {'STT': 5, 'id': 126, 'exName': 'Tim so hoan hao5', 'exTopic': 'Java5', 'exAuthor': 'donghm5'},
        {'STT': 6, 'id': 127, 'exName': 'Tim so hoan hao6', 'exTopic': 'Java6', 'exAuthor': 'donghm6'},
        {'STT': 7, 'id': 128, 'exName': 'Tim so hoan hao7', 'exTopic': 'Java7', 'exAuthor': 'donghm7'},
        {'STT': 8, 'id': 129, 'exName': 'Tim so hoan hao8', 'exTopic': 'Java8', 'exAuthor': 'donghm8'},
        {'STT': 9, 'id': 130, 'exName': 'Tim so hoan hao9', 'exTopic': 'Java9', 'exAuthor': 'donghm9'},
    ]

    return render(request, 'elearning_system/moderator/exUnapprove.html', {'exUnapprove': dict_exUnapprove})


def exNoTopic(request):
    dict_exApproved_noTopic = []
    exApproved_noTopic_list = ExerciseWebServer.objects.all()
    for ex in exApproved_noTopic_list:
        if ex.approver_id != None:
            if ex.tag_id != None:
                dict_exApproved_noTopic.append(ex)

    tag_dict = []
    tag_list = Tag.objects.all()
    for tag in tag_list:
        tag_dict.append(tag)

    result = {'exNoTopic': dict_exApproved_noTopic,
              'tags': tag_dict}

    exNoTopic = [
        {'STT': 1, 'id': 122, 'exName': 'Tim so hoan hao1', 'exAuthor': 'donghm1', 'exViews': 30},
        {'STT': 2, 'id': 123, 'exName': 'Tim so hoan hao2', 'exAuthor': 'donghm2', 'exViews': 31},
        {'STT': 3, 'id': 124, 'exName': 'Tim so hoan hao3', 'exAuthor': 'donghm3', 'exViews': 32},
        {'STT': 4, 'id': 125, 'exName': 'Tim so hoan hao4', 'exAuthor': 'donghm4', 'exViews': 33},
        {'STT': 5, 'id': 126, 'exName': 'Tim so hoan hao5', 'exAuthor': 'donghm5', 'exViews': 34},
        {'STT': 6, 'id': 127, 'exName': 'Tim so hoan hao6', 'exAuthor': 'donghm6', 'exViews': 35},
        {'STT': 7, 'id': 128, 'exName': 'Tim so hoan hao7', 'exAuthor': 'donghm7', 'exViews': 36},
        {'STT': 8, 'id': 129, 'exName': 'Tim so hoan hao8', 'exAuthor': 'donghm8', 'exViews': 37},
        {'STT': 9, 'id': 130, 'exName': 'Tim so hoan hao9', 'exAuthor': 'donghm9', 'exViews': 38},
    ]

    return render(request, 'elearning_system/moderator/exNoTopic.html', result)


# def exerciseUnapproveDetail(request):
#     return render(request, 'elearning_system/moderator/Exercise_Unapprove_Detail.html')

def detail_exUnapprove(request):
    context = {}
    # if request.method == "GET":
    exUnapproveID = request.GET.get('exid', None)
    # exUnapproveID = exUnapproveID - 20
    exUnapprove = ExerciseWebServer.objects.get(pk=exUnapproveID)

    dict_exUnapprove = []
    dict_exUnapprove.append(exUnapprove)

    dict_tag = []
    tag_list = Tag.objects.all()
    for tag in tag_list:
        dict_tag.append(tag);

        # context['status'] = 'success'
    # return HttpResponse(json.dumps(context), content_type='application/json')
    return render(request, 'elearning_system/moderator/Exercise_Unapprove_Detail.html',
                  {'exUnapprove': dict_exUnapprove,'tagList':dict_tag})

def detail_exApproved(request):
    context = {}
    exUnapproveID = request.GET.get('exApproved_id', None)
    exUnapprove = ExerciseWebServer.objects.get(pk=exUnapproveID)

    dict_exApproved = []
    dict_exApproved.append(exUnapprove)

    dict_tag = []
    tag_list = Tag.objects.all()
    for tag in tag_list:
        dict_tag.append(tag);

    return render(request, 'elearning_system/moderator/Exercise_Approved_Detail.html',
                  {'exApproved': dict_exApproved,'tagList':dict_tag})



