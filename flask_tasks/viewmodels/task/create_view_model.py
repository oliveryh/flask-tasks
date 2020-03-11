from flask_tasks.viewmodels.shared.viewmodelbase import ViewModelBase
from flask_tasks.services import tasks_service, users_service


class CreateViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.desc = self.request_dict.desc
        self.user = users_service.get_user_by_id(self.user_id)

    def validate(self):

        if len(self.desc.strip()) == 0:
            self.error = "You must type in a task name"

    def create(self):

        tasks_service.create_user_task(self.user_id, self.desc)
