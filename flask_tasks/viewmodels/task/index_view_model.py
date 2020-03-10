from flask_tasks.viewmodels.shared.viewmodelbase import ViewModelBase
from flask_tasks.services import users_service
from flask_tasks.services import tasks_service


class IndexViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.user = users_service.get_user_by_id(self.user_id)
        self.tasks = tasks_service.get_tasks()
        self.task_count = tasks_service.get_task_count()