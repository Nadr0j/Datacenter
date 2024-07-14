from dataclasses import dataclass
from Role import Role
from pydantic import BaseModel


@dataclass
class Message(BaseModel):
    role: Role
    content: str

