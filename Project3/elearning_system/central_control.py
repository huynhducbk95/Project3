from functools import wraps
from elearning_system.models import User, UserRole


# from web_app.model import account_services
# from web_app.model.customer import Customer




class ViewResult:
    def __init__(self, view_name, model, redirect_dest=None, option=None):
        self.view_name = view_name
        self.model = model
        self.redirect_dest = redirect_dest
        self.option = option
        # for x in self.args:
        # print(x)


# def set_login_user(function):
#     @wraps(function)
#     def new_function(*args, **kwargs):
#         view_result = function(*args, **kwargs)
#         model = view_result.model
#         if not session.get('login_account'):
#             model['user_info'] = None
#         else:
#             model['user_info'] = account_services.get_user_name_and_roles_info(session.get('login_account'))
#         if view_result.option is None:
#             return render_template(view_result.view_name, model=model)
#         elif view_result.option == 'redirect':
#             return redirect(url_for(view_result.redirect_dest))
#
#     return new_function

def get_role_list(user):
    return []


def check_role(role_needed):
    def true_decorator(function):
        def new_function(request, *args):
            is_authorized = False
            if 'user_name' in request.session:
                user_name = request.session['user_name']
                user = User.objects.filter(user_name=user_name)
                for role_name in get_role_list(user):
                    if role_needed == role_name:
                        is_authorized = True
            else:
                model = []
                return render_template('error.html', model=model)
            if not is_authorized:
                model = {}
                model['user_info'] = account_services.get_user_name_and_roles_info(session.get('login_account'))
                return render_template('error.html', model=model)
            else:
                return function(*args)

        return new_function

    return true_decorator
