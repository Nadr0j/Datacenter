from dataclasses import dataclass
from DatasetConfig import DatasetConfig
from ..Deserializable import Deserializable


@dataclass
class CreateConversationalDatasetRequest(Deserializable):
    id: str
    dataset: DatasetConfig



