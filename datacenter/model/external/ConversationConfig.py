from dataclasses import dataclass
from MessageConfig import MessageConfig
from pydantic import BaseModel


@dataclass
class ConversationConfig(BaseModel):
    messageConfigs: list[MessageConfig]
