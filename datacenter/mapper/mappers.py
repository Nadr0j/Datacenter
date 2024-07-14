from ..model.external.RoleConfig import RoleConfig
from ..model.internal.Role import Role
from ..model.external.MessageConfig import MessageConfig
from ..model.internal.Message import Message
from ..model.external.ConversationConfig import ConversationConfig
from ..model.internal.Conversation import Conversation
from ..model.external.DatasetConfig import DatasetConfig
from ..model.internal.Dataset import Dataset
from ..model.external.DatasetMetadataConfig import DatasetMetadataConfig
from ..model.internal.DatasetMetadata import DatasetMetadata


class Mapper:
    @classmethod
    def role_config_to_role(cls, role_config: RoleConfig) -> Role:
        role_map: dict[RoleConfig, Role] = {
            RoleConfig.USER: Role.USER,
            RoleConfig.ASSISTANT: Role.ASSISTANT
        }
        return role_map[role_config]

    @classmethod
    def dataset_metadata_config_to_dataset_metadata(cls, dataset_metadata: DatasetMetadataConfig) -> DatasetMetadata:
        return DatasetMetadata(dataset_metadata.id)

    @classmethod
    def message_config_to_message(cls, message_config: MessageConfig) -> Message:
        role = cls.role_config_to_role(message_config.role_config)
        return Message(role, message_config.content)

    @classmethod
    def conversation_config_to_conversation(cls, conversation_config: ConversationConfig) -> Conversation:
        messages: list[Message] = [cls.message_config_to_message(message_config)
                                   for message_config
                                   in conversation_config.messageConfigs]
        return Conversation(messages)

    @classmethod
    def dataset_config_to_config(cls, dataset_config: DatasetConfig) -> Dataset:
        metadata: DatasetMetadata = cls.dataset_metadata_config_to_dataset_metadata(dataset_config.metadata_config)
        dataset_metadata = DatasetMetadata(metadata)
        conversations: list[Conversation] = [cls.conversation_config_to_conversation(conversation)
                                             for conversation
                                             in dataset_config.conversations]
        return Dataset(conversations, dataset_metadata)
