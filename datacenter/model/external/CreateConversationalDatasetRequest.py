from datacenter.model.external.DatasetConfig import DatasetConfig
from pydantic import BaseModel


class CreateConversationalDatasetRequest(BaseModel):
    id: str
    dataset: DatasetConfig



