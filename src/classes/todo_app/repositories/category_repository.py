from src.classes.todo_app.models.category import Category
from src.classes.todo_app.repositories.base_repository import BaseRepository
from typing import Optional

class CategoryRepository(BaseRepository[Category]):
    def __init__(self, file_path: str):
        super().__init__(file_path=file_path, model=Category)

    def get_by_name(self, name: str) -> Optional[Category]:
        for cat_id in self._data:
            if self._data[cat_id].name.lower() == name.lower():
                return self._data[cat_id]
        return None


