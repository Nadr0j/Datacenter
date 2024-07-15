from ..model.input.RoleConfig import RoleConfig
from ..model.output.Role import Role
from ..model.input.MessageConfig import MessageConfig
from ..model.output.Message import Message
from ..model.input.ConversationConfig import ConversationConfig
from ..model.output.Conversation import Conversation
from ..model.input.DatasetConfig import DatasetConfig
from ..model.output.Dataset import Dataset
from ..model.input.DatasetMetadataConfig import DatasetMetadataConfig
from ..model.output.DatasetMetadata import DatasetMetadata


class ExternalToInternalObjectMapper:
    @classmethod
    def role_config_to_role(cls, role_config: RoleConfig) -> Role:
        role_map: dict[RoleConfig, Role] = {
            RoleConfig.USER(): Role.USER(),
            RoleConfig.ASSISTANT(): Role.ASSISTANT()
        }
        return role_map[role_config]

    @classmethod
    def message_config_to_message(cls, message_config: MessageConfig) -> Message:
        role = cls.role_config_to_role(message_config.role_config)
        return Message(role=role, content=message_config.content)

    @classmethod
    def dataset_metadata_config_to_dataset_metadata(cls, dataset_metadata: DatasetMetadataConfig) -> DatasetMetadata:
        return DatasetMetadata(id=dataset_metadata.id)

    @classmethod
    def conversation_config_to_conversation(cls, conversation_config: ConversationConfig) -> Conversation:
        messages: list[Message] = [cls.message_config_to_message(message_config)
                                   for message_config
                                   in conversation_config.messageConfigs]
        return Conversation(messages=messages)

    @classmethod
    def dataset_config_to_config(cls, dataset_config: DatasetConfig) -> Dataset:
        metadata: DatasetMetadata = cls.dataset_metadata_config_to_dataset_metadata(dataset_config.metadata_config)
        conversations: list[Conversation] = [cls.conversation_config_to_conversation(conversation)
                                             for conversation
                                             in dataset_config.conversation_configs]
        return Dataset(conversations=conversations, metadata=metadata)
