from datacenter.model.external.ConversationConfig import ConversationConfig
from pydantic import BaseModel
from datacenter.model.external.DatasetMetadataConfig import DatasetMetadataConfig


class DatasetConfig(BaseModel):
    conversations: list[ConversationConfig]
    metadata: DatasetMetadataConfig


