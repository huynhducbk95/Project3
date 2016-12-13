from django.shortcuts import render


def errorMessage(request):
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

    return render(request, 'elearning_system/moderator/errorMessage.html', {'messages': messages})


def messageDetail(request):
    return render(request, 'elearning_system/moderator/messageDetail.html')


def exApproved(request):
    exApproved = [
        {'STT': 1, 'id': 122, 'exName': 'Tim so hoan hao1', 'exTopic': 'Java1', 'exAuthor': 'donghm1','exViews': 30},
        {'STT': 2, 'id': 123, 'exName': 'Tim so hoan hao2', 'exTopic': 'Java2', 'exAuthor': 'donghm2','exViews': 31},
        {'STT': 3, 'id': 124, 'exName': 'Tim so hoan hao3', 'exTopic': 'Java3', 'exAuthor': 'donghm3','exViews': 32},
        {'STT': 4, 'id': 125, 'exName': 'Tim so hoan hao4', 'exTopic': 'Java4', 'exAuthor': 'donghm4','exViews': 33},
        {'STT': 5, 'id': 126, 'exName': 'Tim so hoan hao5', 'exTopic': 'Java5', 'exAuthor': 'donghm5','exViews': 34},
        {'STT': 6, 'id': 127, 'exName': 'Tim so hoan hao6', 'exTopic': 'Java6', 'exAuthor': 'donghm6','exViews': 35},
        {'STT': 7, 'id': 128, 'exName': 'Tim so hoan hao7', 'exTopic': 'Java7', 'exAuthor': 'donghm7','exViews': 36},
        {'STT': 8, 'id': 129, 'exName': 'Tim so hoan hao8', 'exTopic': 'Java8', 'exAuthor': 'donghm8','exViews': 37},
        {'STT': 9, 'id': 130, 'exName': 'Tim so hoan hao9', 'exTopic': 'Java9', 'exAuthor': 'donghm9','exViews': 38},
    ]

    return render(request, 'elearning_system/moderator/exApproved.html', {'exApproved':exApproved})

def exUnapprove(request):
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

    return render(request,'elearning_system/moderator/exUnapprove.html',{'exUnapprove':exUnapprove})

def exNoTopic(request):
    exNoTopic = [
        {'STT': 1, 'id': 122, 'exName': 'Tim so hoan hao1','exAuthor': 'donghm1', 'exViews': 30},
        {'STT': 2, 'id': 123, 'exName': 'Tim so hoan hao2','exAuthor': 'donghm2', 'exViews': 31},
        {'STT': 3, 'id': 124, 'exName': 'Tim so hoan hao3','exAuthor': 'donghm3', 'exViews': 32},
        {'STT': 4, 'id': 125, 'exName': 'Tim so hoan hao4','exAuthor': 'donghm4', 'exViews': 33},
        {'STT': 5, 'id': 126, 'exName': 'Tim so hoan hao5', 'exAuthor': 'donghm5', 'exViews': 34},
        {'STT': 6, 'id': 127, 'exName': 'Tim so hoan hao6', 'exAuthor': 'donghm6', 'exViews': 35},
        {'STT': 7, 'id': 128, 'exName': 'Tim so hoan hao7', 'exAuthor': 'donghm7', 'exViews': 36},
        {'STT': 8, 'id': 129, 'exName': 'Tim so hoan hao8', 'exAuthor': 'donghm8', 'exViews': 37},
        {'STT': 9, 'id': 130, 'exName': 'Tim so hoan hao9', 'exAuthor': 'donghm9', 'exViews': 38},
    ]

    return render(request, 'elearning_system/moderator/exNoTopic.html', {'exNoTopic': exNoTopic})

def viewExUnapprove_detail(request):

    return  render(request, 'elearning_system/moderator/exUnapprove_detail.html')