from datacenter.model.external.MessageConfig import MessageConfig
from pydantic import BaseModel


class ConversationConfig(BaseModel):
    messageConfigs: list[MessageConfig]
