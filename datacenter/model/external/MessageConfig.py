from datacenter.model.external.RoleConfig import RoleConfig
from pydantic import BaseModel


class MessageConfig(BaseModel):
    role_config: RoleConfig
    content: str

