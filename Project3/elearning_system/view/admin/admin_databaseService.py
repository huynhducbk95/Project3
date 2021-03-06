from elearning_system.models import User, Tag, Role


# tag database service

def get_tag_list():
    return Tag.objects.all()


def create_tag(tag_name):
    tag = Tag(tag_name=tag_name)
    tag.save()
    return tag.id


def update_tag_name(tag_id, new_name):
    tag = Tag.objects.get(pk=tag_id)
    tag.tag_name = new_name
    tag.save()


# user database service

def get_all_user_list():
    return User.objects.all()


def get_normal_user_list():
    all_user =  Role.objects.get(role_name='user').user_list.all()
    moderator_list =  Role.objects.get(role_name='moderator').user_list.all()
    admin_list =  Role.objects.get(role_name='admin').user_list.all()
    user_list = []
    for user in all_user:
        if user not in moderator_list and user not in admin_list:
            user_list.append(user)
    return user_list


def create_user(userName, fullName, password, email, status):
    user = User(full_name=fullName, password=password, user_name=userName, email_address=email,
                block_status=status)
    user.save()
    return user


def get_user(user_id):
    return User.objects.get(pk=user_id)


#  moderator database serviec

def get_moderator_list():
    return Role.objects.get(role_name='moderator').user_list.all()


def add_moderator(moderator):
    role_moderator = Role.objects.get(pk=2)
    role_moderator.user_list.add(moderator)
    role_moderator.save()

    role_user = Role.objects.get(pk=3)
    role_user.user_list.add(moderator)
    role_user.save()


def change_user_status(userID):
    user = User.objects.get(pk=userID)
    if user.block_status == 'Active':
        user.block_status = 'Block'
    else:
        user.block_status = 'Active'
    user.save()


def get_moderator(moderator_id):
    return Role.objects.get(role_name='moderator').user_list.get(pk=moderator_id)
