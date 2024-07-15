from datacenter.model.input.RoleConfig import RoleConfig
from pydantic import BaseModel


class MessageConfig(BaseModel):
    role_config: RoleConfig
    content: str

