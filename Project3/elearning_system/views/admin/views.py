from django.shortcuts import render


def manageTopic(request):
    dict = [{'STT': 1, 'topicName': 'Java','numberOfEx':20},
            {'STT': 2, 'topicName': 'Java', 'numberOfEx': 20},
            {'STT': 3, 'topicName': 'Java', 'numberOfEx': 20},
            {'STT': 4, 'topicName': 'Java', 'numberOfEx': 20},
            {'STT': 5, 'topicName': 'Java', 'numberOfEx': 20},
            {'STT': 6, 'topicName': 'Java', 'numberOfEx': 20},
            {'STT': 7, 'topicName': 'Java', 'numberOfEx': 20}]

    return render(request, 'elearning_system/admin/manageTopic.html', {'data': dict})


