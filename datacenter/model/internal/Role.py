from enum import Enum
from pydantic import BaseModel


class Role(Enum, BaseModel):
    USER = "user"
    ASSISTANT = "assistant"
