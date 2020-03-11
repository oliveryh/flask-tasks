from flask_tasks.viewmodels.shared.viewmodelbase import ViewModelBase
from flask_tasks.services import tasks_service


class UpdateViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.task_id = self.request.json["id"]
        self.update_type = self.request.json["type"]

    def update(self):

        if self.update_type == "item_completed":
            tasks_service.item_completed(self.task_id)
        elif self.update_type == "item_uncompleted":
            tasks_service.item_uncompleted(self.task_id)
        return {}
