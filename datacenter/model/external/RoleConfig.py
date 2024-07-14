from enum import Enum
from pydantic import BaseModel


class RoleConfig(Enum, BaseModel):
    USER = "user"
    ASSISTANT = "assistant"
