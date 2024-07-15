from datacenter.model.output.Conversation import Conversation
from pydantic import BaseModel
from datacenter.model.output.DatasetMetadata import DatasetMetadata


class Dataset(BaseModel):
    conversations: list[Conversation]
    metadata: DatasetMetadata


