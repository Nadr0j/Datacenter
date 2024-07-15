from datacenter.model.internal.Message import Message
from pydantic import BaseModel


class Conversation(BaseModel):
    messages: list[Message]
