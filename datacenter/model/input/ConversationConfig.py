from datacenter.model.input.MessageConfig import MessageConfig
from pydantic import BaseModel


class ConversationConfig(BaseModel):
    messageConfigs: list[MessageConfig]
