from datacenter.model.input.DatasetConfig import DatasetConfig
from pydantic import BaseModel


class CreateConversationalDatasetRequest(BaseModel):
    id: str
    dataset: DatasetConfig



