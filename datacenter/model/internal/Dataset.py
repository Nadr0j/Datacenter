from dataclasses import dataclass
from Conversation import Conversation
from pydantic import BaseModel
from DatasetMetadata import DatasetMetadata


@dataclass
class Dataset(BaseModel):
    conversations: list[Conversation]
    metadata: DatasetMetadata


