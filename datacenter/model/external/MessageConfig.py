from dataclasses import dataclass
from RoleConfig import RoleConfig
from pydantic import BaseModel


@dataclass
class MessageConfig(BaseModel):
    role_config: RoleConfig
    content: str

