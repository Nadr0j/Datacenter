from datacenter.model.input.ConversationConfig import ConversationConfig
from pydantic import BaseModel
from datacenter.model.input.DatasetMetadataConfig import DatasetMetadataConfig


class DatasetConfig(BaseModel):
    conversation_configs: list[ConversationConfig]
    metadata_config: DatasetMetadataConfig


