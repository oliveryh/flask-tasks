from flask_tasks.viewmodels.shared.viewmodelbase import ViewModelBase
from flask_tasks.services import users_service


class IndexViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.user = users_service.get_user_by_id(self.user_id)
