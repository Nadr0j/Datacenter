from datacenter.model.internal.Conversation import Conversation
from pydantic import BaseModel
from datacenter.model.internal.DatasetMetadata import DatasetMetadata


class Dataset(BaseModel):
    conversations: list[Conversation]
    metadata: DatasetMetadata


