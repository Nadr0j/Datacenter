from datacenter.model.output.Role import Role
from pydantic import BaseModel


class Message(BaseModel):
    role: Role
    content: str

