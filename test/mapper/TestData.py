from datacenter.model.input.ConversationConfig import ConversationConfig
from datacenter.model.input.DatasetConfig import DatasetConfig
from datacenter.model.input.DatasetMetadataConfig import DatasetMetadataConfig
from datacenter.model.output.Conversation import Conversation
from datacenter.model.output.Dataset import Dataset
from datacenter.model.output.DatasetMetadata import DatasetMetadata
from datacenter.model.output.Role import Role
from datacenter.model.input.RoleConfig import RoleConfig
from datacenter.model.output.Message import Message
from datacenter.model.input.MessageConfig import MessageConfig


class TestData:
    # Other Objects
    ARBITRARY_STRING = "some-string"
    USER_MESSAGE = "user-message"
    ASSISTANT_MESSAGE = "user-assistant"

    # Role Objects
    ROLE_USER = Role(role="user")
    ROLE_CONFIG_USER = RoleConfig(role="user")
    ROLE_ASSISTANT = Role(role="assistant")
    ROLE_CONFIG_ASSISTANT = RoleConfig(role="assistant")

    # Message Objects
    MESSAGE_USER = Message(role=ROLE_USER, content=USER_MESSAGE)
    MESSAGE_ASSISTANT = Message(role=ROLE_ASSISTANT, content=ASSISTANT_MESSAGE)
    MESSAGE_CONFIG_USER = MessageConfig(role_config=ROLE_CONFIG_USER, content=USER_MESSAGE)
    MESSAGE_CONFIG_ASSISTANT = MessageConfig(role_config=ROLE_CONFIG_ASSISTANT, content=ASSISTANT_MESSAGE)

    # DatasetMetadata Objects
    DATASET_METADATA_CONFIG = DatasetMetadataConfig(id=ARBITRARY_STRING)
    DATASET_METADATA = DatasetMetadata(id=ARBITRARY_STRING)

    # Conversation Objects
    CONVERSATION_CONFIG = ConversationConfig(messageConfigs=[MESSAGE_CONFIG_ASSISTANT, MESSAGE_CONFIG_USER])
    CONVERSATION = Conversation(messages=[MESSAGE_ASSISTANT, MESSAGE_USER])

    # Dataset Objects
    DATASET_CONFIG = DatasetConfig(conversation_configs=[CONVERSATION_CONFIG], metadata_config=DATASET_METADATA_CONFIG)
    DATASET = Dataset(conversations=[CONVERSATION], metadata=DATASET_METADATA)

