
class FormUserLogIn:
    def _init__(self, username, password):
        self.username = username
        self.password = password


class FormUserRegistry:
    def __init__(self, username, email, password, account_name):
        self.username = username
        self.email = email
        self.password = password
        self.account_name = account_name