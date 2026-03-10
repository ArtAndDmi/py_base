from datetime import datetime
from typing import List
from pathlib import Path

from src.classes.todo_app.models.task import Task
from src.classes.todo_app.repositories.task_repository import TaskRepository
from src.classes.todo_app.repositories.category_repository import CategoryRepository
from src.classes.todo_app.repositories.status_repository import StatusRepository


class TodoApp:
    dir_path = Path
    CATEGORIES_PATH = 'categories.json'
    STATUSES_PATH = 'statuses.json'
    TASKS_PATH = 'tasks.json'
    
    def __init__(self, data_dir: str):
        base_dir = Path(data_dir).resolve()

        self.dir_path = base_dir
        self.task_repo = TaskRepository(str(base_dir / self.TASKS_PATH))
        self.category_repo = CategoryRepository(str(base_dir / self.CATEGORIES_PATH))
        self.status_repo = StatusRepository(str(base_dir / self.STATUSES_PATH))

    
    def add_task(self, title: str, category_id: int, status_id: int, **kwargs) -> Task:
        if self.status_repo.get(status_id) and self.category_repo.get(category_id):
            new_task = Task(
                id=kwargs['id'],
                title=title,
                category_id=category_id,
                status_id=status_id,
                **kwargs
            )

            self.task_repo.add(new_task)
            return new_task
        else:
            raise ValueError("Категория или статус не существуют")

    
    def mark_task_done(self, task_id: int) -> bool:
        if self.task_repo.get(task_id):
            self.task_repo.update(id_=task_id, is_done=True)
            return True
        return False

    
    def get_overdue_tasks(self) -> List[Task]:
        res = []
        tasks = self.task_repo._data
        for task_id in tasks:
            deadline_str = tasks[task_id]['deadline']
            if (
                deadline_str is not None
                and datetime.fromisoformat(deadline_str) < datetime.now()
                and tasks[task_id]["is done"] is False
            ):
                res.append(tasks[task_id])
        return res



def load_sample_data(app: TodoApp) -> None:
    app.status_repo._load()
    app.category_repo._load()
    app.task_repo._load()


def print_task(task: Task) -> None:
    print('Название:', task['title'])
    print('Описание:', task['description'])
    print('ID Категории:', task['category_id'])
    print('ID Статуса:', task['status_id'])
    print('Выполнена:', 'Да' if task['is_done'] else 'Нет')
    print('Дедлайн:', task['deadline'])


def print_tasks(tasks: List[Task]) -> None:
    for task in tasks:
        print_task(task)
        print()

