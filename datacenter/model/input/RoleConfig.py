from pydantic import BaseModel, field_validator
from typing import ClassVar


class RoleConfig(BaseModel, frozen=True):
    role: str

    VALID_ROLES: ClassVar[set] = {"user", "assistant"}

    @classmethod
    def USER(cls) -> 'RoleConfig':
        return cls(role="user")

    @classmethod
    def ASSISTANT(cls) -> 'RoleConfig':
        return cls(role="assistant")

    @field_validator('role')
    @classmethod
    def role_must_be_valid(cls, v):
        if v not in cls.VALID_ROLES:
            raise ValueError(f"Invalid role: {v}. Must be one of {cls.VALID_ROLES}")
        return v
