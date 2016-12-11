from django.shortcuts import render


def manageTopic(request):
    dict = [{'STT': 1, 'topicName': 'Java1','numberOfEx':20},
            {'STT': 2, 'topicName': 'Java2', 'numberOfEx': 20},
            {'STT': 3, 'topicName': 'Java3', 'numberOfEx': 20},
            {'STT': 4, 'topicName': 'Java4', 'numberOfEx': 20},
            {'STT': 5, 'topicName': 'Java5', 'numberOfEx': 20},
            {'STT': 6, 'topicName': 'Java6', 'numberOfEx': 20},
            {'STT': 7, 'topicName': 'Java7', 'numberOfEx': 20}]

    return render(request, 'elearning_system/admin/manageTopic.html', {'data': dict})

def manageUser(request):
    dict = [{'STT': 1, 'userName': 'donghm1','email': 'abc1@gmail.com', 'ID': 20, 'status': 'Active', 'posted':  15,'resolved': 30},
            {'STT': 2, 'userName': 'donghm2','email': 'abc2@gmail.com', 'ID': 21, 'status': 'Block', 'posted': 15, 'resolved': 30},
            {'STT': 3, 'userName': 'donghm3','email': 'abc3@gmail.com', 'ID': 22, 'status': 'Block', 'posted': 15, 'resolved': 30},
            {'STT': 4, 'userName': 'donghm4','email': 'abc4@gmail.com', 'ID': 23, 'status': 'Active', 'posted': 15, 'resolved': 30},
            {'STT': 5, 'userName': 'donghm5','email': 'abc5@gmail.com', 'ID': 24, 'status': 'Active', 'posted': 15, 'resolved': 30},
            {'STT': 6, 'userName': 'donghm6','email': 'abc6@gmail.com', 'ID': 25, 'status': 'Block', 'posted': 15, 'resolved': 30},
            {'STT': 7, 'userName': 'donghm7','email': 'abc7@gmail.com', 'ID': 26, 'status': 'Active', 'posted': 15, 'resolved': 30},]

    return render(request, 'elearning_system/admin/manageUser.html', {'dataUser': dict})


def manageModerator(request):
    dict = [{'STT': 1, 'userName': 'donghm1','email': 'abc1@gmail.com','fullName':'Ha Manh Dong 1', 'ID': 20, 'status': 'Active'},
            {'STT': 2, 'userName': 'donghm2','email': 'abc2@gmail.com','fullName':'Ha Manh Dong 2', 'ID': 21, 'status': 'Block'},
            {'STT': 3, 'userName': 'donghm3','email': 'abc3@gmail.com','fullName':'Ha Manh Dong 3', 'ID': 22, 'status': 'Block'},
            {'STT': 4, 'userName': 'donghm4','email': 'abc4@gmail.com','fullName':'Ha Manh Dong 4', 'ID': 23, 'status': 'Active'},
            {'STT': 5, 'userName': 'donghm5','email': 'abc5@gmail.com','fullName':'Ha Manh Dong 5', 'ID': 24, 'status': 'Active'},
            {'STT': 6, 'userName': 'donghm6','email': 'abc6@gmail.com','fullName':'Ha Manh Dong 6', 'ID': 25, 'status': 'Block'},
            {'STT': 7, 'userName': 'donghm7','email': 'abc7@gmail.com','fullName':'Ha Manh Dong 7', 'ID': 26, 'status': 'Active'},]

    return render(request, 'elearning_system/admin/manageModerator.html', {'dataModerator': dict})