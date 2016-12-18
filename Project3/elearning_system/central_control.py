from elearning_system.models import User

from django.shortcuts import render


class ViewResult:
    def __init__(self, view_name, model, redirect_dest=None, option=None):
        self.view_name = view_name
        self.model = model
        self.redirect_dest = redirect_dest
        self.option = option


def get_role_list(user_name):
    user = User.objects.filter(user_name=user_name).first()
    role_list = []
    for role in user.role_set.all():
        role_list.append(role.role_name)
    return role_list


def check_role(role_needed):
    def true_decorator(function):
        def new_function(request, *args):
            is_authorized = False
            if 'user_name' in request.session:
                for role_name in get_role_list(request.session['user_name']):
                    if role_needed == role_name:
                        is_authorized = True
            if not is_authorized:
                return render_template(request, 'elearning_system/central_control/http_403_access_denied.html', {},
                                       status=403)
            else:
                return function(*args)

        return new_function

    return true_decorator


def render_template(request, template_name, context, status=200):
    is_login = False
    role_list = []
    account_name = ''
    if 'user_name' in request.session:
        is_login = True
        account_name = User.objects.filter(user_name=request.session['user_name']).first().account_name
        role_list = get_role_list(request.session['user_name'])
    if is_login is True and 'is_login' not in context:
        context['account_name'] = account_name
        context['is_login'] = True
    if 'user_role_list' not in context and len(role_list) > 0:
        context['user_role_list'] = role_list
    return render(request, template_name=template_name, context=context, status=status)
