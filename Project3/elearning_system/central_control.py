from elearning_system.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
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
        def new_function(request, *args, **kwargs):
            is_authorized = False
            if 'user_name' in request.session:
                for role_name in get_role_list(request.session['user_name']):
                    if role_needed == role_name:
                        is_authorized = True
                if not is_authorized:
                    return render_template(request, 'elearning_system/central_control/http_403_access_denied.html', {},
                                           status=403)
                else:
                    return function(request, *args, **kwargs)

            else:
                return HttpResponseRedirect(reverse('login') + '?next_page=' + request.path)

        return new_function

    return true_decorator


def check_user_is_login(request):
    if 'user_name' in request.session:
        return True
    else:
        return False


def get_user_name(request):
    try:
        return request.session['user_name']
    except Exception:
        return False


def check_user_is_block(user_name):
    return False


def render_template(request, template_name, context, status=200):
    is_login = False
    role_list = []
    full_name = ''
    if 'user_name' in request.session:
        is_login = True
        role_list = get_role_list(request.session['user_name'])
    if is_login is True and 'is_login' not in context:
        context['user_name'] = request.session['user_name']
        context['is_login'] = True
    if 'role_list' not in context and len(role_list) > 0:
        context['role_list'] = role_list
    return render(request, template_name=template_name, context=context, status=status)
