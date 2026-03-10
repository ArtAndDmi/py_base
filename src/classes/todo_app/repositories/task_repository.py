from typing import List
from src.classes.todo_app.models.task import Task
from src.classes.todo_app.repositories.base_repository import BaseRepository


class TaskRepository(BaseRepository[Task]):
    def __init__(self, file_path: str):
        super().__init__(file_path=file_path, model=Task)

    def get_by_category(self, category_id: int) -> List[Task]:
        res = []

        for task_id in self._data:
            if self._data[task_id]['category_id'] == category_id:
                res.append(self._data[task_id])
        return res

    def get_by_status(self, status_id: int) -> List[Task]:
        res = []

        for task_id in self._data:
            if self._data[task_id]['status_id'] == status_id:
                res.append(self._data[task_id])
        return res



