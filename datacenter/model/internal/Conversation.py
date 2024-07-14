from dataclasses import dataclass
from Message import Message
from pydantic import BaseModel


@dataclass
class Conversation(BaseModel):
    messages: list[Message]
