from flask_tasks.viewmodels.shared.viewmodelbase import ViewModelBase
from flask_tasks.services import users_service
from flask_tasks.services import tasks_service


class IndexViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.user = users_service.get_user_by_id(self.user_id)

    def load_tasks(self):
        self.tasks = tasks_service.get_user_tasks(self.user_id)
        self.task_count = tasks_service.get_user_task_count(self.user_id)
