from elearning_system.models import ExerciseWebServer, User


class DatabaseService:
    def __init__(self):
        pass

    @staticmethod
    def save_exercise(web_server_exercise):
        web_server_exercise.save()

    @staticmethod
    def add_error_message(error_message):
        error_message.save()

    @staticmethod
    def get_exercise_web_server_detail(exercise_id):
        try:
            exercise_web_server = ExerciseWebServer.objects.filter(id=exercise_id).first()
            if exercise_web_server is None:
                return 'not_found'
            else:
                return exercise_web_server
        except Exception:
            return 'error'

    @staticmethod
    def get_user_by_user_name(user_name):
        try:
            user = User.objects.filter(user_name=user_name).first()
            if user is None:
                return 'not_found'
            else:
                return user
        except Exception:
            return 'error'
