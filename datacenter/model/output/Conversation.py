from datacenter.model.output.Message import Message
from pydantic import BaseModel


class Conversation(BaseModel):
    messages: list[Message]
