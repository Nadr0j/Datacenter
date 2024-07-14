from dataclasses import dataclass
from ConversationConfig import ConversationConfig
from pydantic import BaseModel
from DatasetMetadataConfig import DatasetMetadataConfig


@dataclass
class DatasetConfig(BaseModel):
    conversations: list[ConversationConfig]
    metadata: DatasetMetadataConfig


