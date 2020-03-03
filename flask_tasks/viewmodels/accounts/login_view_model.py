from viewmodels.shared.viewmodelbase import ViewModelBase
from flask_tasks.services import users_service
from flask_tasks.services import tasks_service


class LoginViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.email = self.request_dict.email.lower().strip()
        self.password = self.request_dict.password.strip()

    def validate(self):
        user = users_service.login_user(self.email, self.password)
        if not user:
            self.error = "The email or password you have entered is incorrect"

        self.user = user