from flask_tasks.viewmodels.shared.viewmodelbase import ViewModelBase
from flask_tasks.services import users_service


class RegisterViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.name = self.request_dict.name
        self.email = self.request_dict.email.lower().strip()
        self.password = self.request_dict.password.strip()

    def validate(self):

        email_exists = users_service.does_email_exist(self.email)
        if email_exists:
            self.error = "A user with that email already exists"

    def register_user(self):

        self.user = users_service.add_user(self.name, self.email, self.password)