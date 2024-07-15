from datacenter.model.internal.Role import Role
from datacenter.model.external.RoleConfig import RoleConfig
from datacenter.model.internal.Message import Message
from datacenter.model.external.MessageConfig import MessageConfig


class TestData:
    # Other Objects
    ARBITRARY_STRING = "some-string"

    # Role Objects
    ROLE_USER = Role(role="user")
    ROLE_CONFIG_USER = RoleConfig(role="user")
    ROLE_ASSISTANT = Role(role="assistant")
    ROLE_CONFIG_ASSISTANT = RoleConfig(role="assistant")

    # Message Objects
    MESSAGE_USER = Message(role=ROLE_USER, content=ARBITRARY_STRING)
    MESSAGE_ASSISTANT = Message(role=ROLE_ASSISTANT, content=ARBITRARY_STRING)
    MESSAGE_CONFIG_USER = MessageConfig(role_config=ROLE_CONFIG_USER, content=ARBITRARY_STRING)
    MESSAGE_CONFIG_ASSISTANT = MessageConfig(role_config=ROLE_CONFIG_ASSISTANT, content=ARBITRARY_STRING)
