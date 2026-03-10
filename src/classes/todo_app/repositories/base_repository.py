import json
from datetime import datetime
from json import JSONEncoder
from typing import TypeVar, Generic, Dict, Optional, Type, List, Any
from pydantic import BaseModel
from pathlib import Path

T = TypeVar('T', bound=BaseModel)

class DateTimeEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

class BaseRepository(Generic[T]):
    _data: dict[Any, Optional[T]]


    def __init__(self, file_path: str, model: Type[T]):
        self._file_path = file_path
        self.file_path = Path(file_path).resolve()
        self._model = model
        self._load()

    def _load(self) -> None:
        if self.file_path.exists():
            with open(self.file_path, "r", encoding="utf-8") as f:
                json_data = json.load(f)
                self._data = {int(k): self._model(**v) for k, v in json_data.items()}
        else:
            self._data = {}



    def _save(self) -> None:
        json_data = {
            str(k): v.model_dump() if hasattr(v, "model_dump") else v
            for k, v in self._data.items()
        }
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2, cls=DateTimeEncoder)

    def add(self, item: T) -> T:
        if item.id in self._data.keys():
            raise ValueError(f'Item with id {item.id} already exists')
        else:
            self._data[item.id] = item
            self._save()
            return item

    def get(self, id_: int) -> Optional[T]:
        return self._data.get(id_)

    def get_all(self) -> List[T]:
        res = []
        for el_id in self._data:
            res.append(self._data[el_id])
        return res

    def update(self, id_: int, **kwargs) -> bool:
        item_id = id_
        if item_id in self._data:
            item = self._data[item_id]
            for key, value in kwargs.items():
                if hasattr(item, key):
                    setattr(item, key, value)
            return True
        return False

    def delete(self, id_: int) -> bool:
        if id_ in self._data.keys():
            del self._data[id_]
            return True
        return False
