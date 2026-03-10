from src.classes.todo_app.models.status import Status
from src.classes.todo_app.repositories.base_repository import BaseRepository

class StatusRepository(BaseRepository[Status]):
    def __init__(self, file_path: str):
        super().__init__(file_path=file_path, model=Status)
        if len(self._data) == 0:
            self._init_default_statuses()

    def _init_default_statuses(self) -> None:
        self._data: dict[int, Status] = {
            1: Status(id=1, name='В ожидании'),
            2: Status(id=2, name='В работе'),
            3: Status(id=3, name='Завершено')
        }

    def is_valid_status(self, status_id: int) -> bool:
        return status_id in self._data.keys()



