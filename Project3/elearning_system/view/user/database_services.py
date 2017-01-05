from elearning_system.models import User, Role, ExerciseWebServer, Tag
from elearning_system.view.user import plugin_services
from django.utils import formats


def get_top_view_exercise_list():
    exercise_list = ExerciseWebServer.objects.all().order_by('-view_number')
    count = 1
    top_view_exercise_list = []
    for exercise in exercise_list:
        if count == 18:
            break
        elif exercise.approver == None:
            continue
        else:
            response = plugin_services.exercise_detail(exercise.id)
            if response['status'] == 'success':
                exercise_top = {
                    'id': exercise.id,
                    'name': response['exercise']['name'],
                    'description': response['exercise']['description'],
                    'date_created': exercise.date_created,
                    'contributor': exercise.contributor.user_name,
                    'view': exercise.view_number,
                }
                top_view_exercise_list.append(exercise_top)
                count += 1
    return top_view_exercise_list


def get_lastest_exercise_list():
    exercise_list = ExerciseWebServer.objects.all().order_by('-date_created')
    count = 1
    top_last_exercise_list = []
    for exercise in exercise_list:
        if count == 18:
            break
        elif exercise.approver == None:
            continue
        else:
            response = plugin_services.exercise_detail(exercise.id)
            if response['status'] == 'success':
                exercise_top = {
                    'id': exercise.id,
                    'name': response['exercise']['name'],
                    'description': response['exercise']['description'],
                    'date_created': exercise.date_created,
                    'contributor': exercise.contributor.user_name,
                    'view': exercise.view_number,
                }
                top_last_exercise_list.append(exercise_top)
                count += 1
    return top_last_exercise_list


def get_tag_list():
    tag_list_db = Tag.objects.all()
    tag_list = []
    for tag in tag_list_db:
        tag_info = {
            'name': tag.tag_name,
            'id': tag.id
        }
        tag_list.append(tag_info)
    return tag_list


def get_exercise_by_tag(tag_id):
    tag_db = Tag.objects.get(pk=tag_id)
    exercises = tag_db.exercisewebserver_set.all().order_by('-date_created')
    exercise_list = []
    for exercise in exercises:
        if exercise.approver == None:
            continue
        date_joined = exercise.date_created
        formatted_datetime = formats.date_format(date_joined, "d-m-Y H:i")
        response = plugin_services.exercise_detail(exercise.id)
        if response['status'] == 'success':
            exercise_info = {
                'id':exercise.id,
                'name': response['exercise']['name'],
                'description': response['exercise']['description'],
                'date_created': formatted_datetime,
                'contributor': exercise.contributor.user_name,
                'view': exercise.view_number,
            }
            exercise_list.append(exercise_info)
    return exercise_list


def get_top_user_contribute_list():
    user_contribute_list_db = User.objects.all().order_by('-contribute_number')
    user_contribute_list = []
    for user in user_contribute_list_db:
        user_infor = {
            'user_name': user.user_name,
            'contribute_number': user.contribute_number,
            'solve_number': user.solve_number,
        }
        user_contribute_list.append(user_infor)
    return user_contribute_list


def get_top_user_solve_list():
    user_solve_list_db = User.objects.all().order_by('-solve_number')
    user_solve_list = []
    for user in user_solve_list_db:
        user_infor = {
            'user_name': user.user_name,
            'contribute_number': user.contribute_number,
            'solve_number': user.solve_number,
        }
        user_solve_list.append(user_infor)
    return user_solve_list


def check_user_name_exist(user_name, email):
    user_list = User.objects.all()
    result = {
        'result': 'success'
    }
    for user in user_list:
        if user.user_name == user_name:
            result = {
                'result': 'error',
                'message': 'Username is already exist'
            }
            break
        if user.email_address == email:
            result = {
                'result': 'error',
                'message': 'Email address is already exist'
            }
            break

    return result


def add_new_user(user_name, password, email, full_name):
    try:
        block_status = 'Active'
        user = User(user_name=user_name,
                    password=password,
                    email_address=email,
                    full_name=full_name,
                    block_status=block_status)

        user.save()
        role_user = Role.objects.get(role_name='user')
        role_user.user_list.add(user)
        result = {
            'result': 'success'
        }
        role_user.save()
    except Exception:
        result = {
            'result': 'error'
        }
    return result


def get_user_detail(user_name):
    return User.objects.get(user_name=user_name)


def get_tag_detail(tag_id):
    return Tag.objects.get(pk=tag_id)


def change_password_user(user_name, password):
    user = User.objects.get(user_name=user_name)
    user.password = password
    user.save()


def check_exercise_is_approved(exercise_id):
    try:
        exercise = ExerciseWebServer.objects.get(pk=exercise_id)
        if exercise.approver == None:
            return False
        return True
    except Exception as e:
        return False


def get_exercise_list_info(exercise_list_plugin_response, search_option):
    id_list = []
    for exercise in exercise_list_plugin_response:
        id_list.append(exercise['id'])
    if search_option == 'All':
        exercise_list = ExerciseWebServer.objects.all()
    elif search_option == 'View':
        exercise_list = ExerciseWebServer.objects.all().order_by('-view_number')
    elif search_option == 'Solve':
        exercise_list = ExerciseWebServer.objects.all().order_by('-solve_number')
    else:
        exercise_list = ExerciseWebServer.objects.all().order_by('-date_created')
    exercise_info_list = []
    for exercise in exercise_list:
        if exercise.id in id_list:
            for ex_plugin in exercise_list_plugin_response:
                if ex_plugin['id'] == exercise.id:
                    exercise_plugin = ex_plugin
                    break
            date_joined = exercise.date_created
            formatted_datetime = formats.date_format(date_joined, "d-m-Y H:i")
            exercise_info = {
                'name': exercise_plugin['name'],
                'description': exercise_plugin['description'],
                'date_created': formatted_datetime,
                'contributor': exercise.contributor.user_name,
                'view': exercise.view_number,
            }
            exercise_info_list.append(exercise_info)
    return exercise_info_list


def sort_by_option(page_compare_option, page_exercise_option, page_name, page_number):
    if page_name == 'tag':
        tag = Tag.objects.get(pk=int(page_exercise_option))
        if page_compare_option == 'view':
            exercise_list = tag.exercisewebserver_set.all().order_by('-view_number')
        else:
            exercise_list = tag.exercisewebserver_set.all().order_by('-date_created')
    else:
        if page_compare_option == 'date':
            exercise_list = ExerciseWebServer.objects.all().order_by('-date_created')
        if page_compare_option == 'view':
            exercise_list = ExerciseWebServer.objects.all().order_by('-view_number')
    start_index = (int(page_number) - 1) * 5
    exercise_list_result = []
    for i in range(5):
        if start_index + i > len(exercise_list) - 1:
            break
        else:
            date_joined = exercise_list[start_index + i].date_created
            formatted_datetime = formats.date_format(date_joined, "d-m-Y H:i")
            exercise_data_from_plugin = plugin_services.exercise_detail(exercise_list[start_index+i])
            exercise_info = {
                'id': exercise_list[start_index + i].id,
                'name': exercise_data_from_plugin['name'],
                'description': exercise_data_from_plugin['description'],
                'date_created': str(formatted_datetime),
                'contributor': exercise_list[start_index + i].contributor.user_name,
                'view': exercise_list[start_index + i].view_number,
            }
            exercise_list_result.append(exercise_info)
    return exercise_list_result
