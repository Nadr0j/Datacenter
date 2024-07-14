from pydantic import BaseModel
import json


class DataclassSerializer:
    @classmethod
    def deserialize_to_dataclass(cls, output_class: type[BaseModel], data: str):
        data_dict: dict[str, str | int] = json.loads(data)
        return output_class(**data_dict)
