from elearning_system.models import Tag
from elearning_system.models import ExerciseWebServer, User, ErrorMessage

# error message

def get_message_list():
    return ErrorMessage.objects.all()

