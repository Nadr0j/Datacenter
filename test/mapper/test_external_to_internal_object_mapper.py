import pytest
from datacenter.mapper.external_to_internal_object_mapper import ExternalToInternalObjectMapper
from datacenter.model.input.ConversationConfig import ConversationConfig
from datacenter.model.input.DatasetConfig import DatasetConfig
from datacenter.model.input.DatasetMetadataConfig import DatasetMetadataConfig
from datacenter.model.input.MessageConfig import MessageConfig
from datacenter.model.input.RoleConfig import RoleConfig
from datacenter.model.output.Conversation import Conversation
from datacenter.model.output.Dataset import Dataset
from datacenter.model.output.DatasetMetadata import DatasetMetadata
from datacenter.model.output.Message import Message
from datacenter.model.output.Role import Role
from test.mapper.TestData import TestData


class TestExternalToInternalObjectMapper:
    mapper = ExternalToInternalObjectMapper()

    @pytest.mark.parametrize("role_config, expected_output", [
        (TestData.ROLE_CONFIG_USER, TestData.ROLE_USER),
        (TestData.ROLE_CONFIG_ASSISTANT, TestData.ROLE_ASSISTANT)
    ])
    def test_role_config_to_role_returns_expected_role_when_called(
            self, role_config: RoleConfig, expected_output: Role):
        mapped_role: Role = self.mapper.role_config_to_role(role_config)
        assert expected_output == mapped_role

    @pytest.mark.parametrize("message_config, expected_output", [
        (TestData.MESSAGE_CONFIG_USER, TestData.MESSAGE_USER),
        (TestData.MESSAGE_CONFIG_ASSISTANT, TestData.MESSAGE_ASSISTANT)
    ])
    def test_message_config_to_message_returns_expected_message_when_called(
            self, message_config: MessageConfig, expected_output: Message):
        mapped_messaged: Message = self.mapper.message_config_to_message(message_config)
        assert expected_output == mapped_messaged

    @pytest.mark.parametrize("dataset_metadata_config, expected_output", [
        (TestData.DATASET_METADATA_CONFIG, TestData.DATASET_METADATA),
    ])
    def test_dataset_metadata_config_to_dataset_metadata_returns_expected_metadata_when_called(
            self, dataset_metadata_config: DatasetMetadataConfig, expected_output: DatasetMetadata):
        mapped_metadata: DatasetMetadata = self.mapper.dataset_metadata_config_to_dataset_metadata(dataset_metadata_config)
        assert expected_output == mapped_metadata

    @pytest.mark.parametrize("conversation_config, expected_output", [
        (TestData.CONVERSATION_CONFIG, TestData.CONVERSATION)
    ])
    def test_conversation_config_to_conversation_returns_expected_conversation_when_called(
            self, conversation_config: ConversationConfig, expected_output: Conversation):
        mapped_conversation: Conversation = self.mapper.conversation_config_to_conversation(conversation_config)
        assert expected_output == mapped_conversation

    @pytest.mark.parametrize("dataset_config, expected_output", [
        (TestData.DATASET_CONFIG, TestData.DATASET)
    ])
    def test_conversation_config_to_conversation_returns_expected_conversation_when_called(
            self, dataset_config: DatasetConfig, expected_output: Dataset):
        mapped_dataset: Dataset = self.mapper.dataset_config_to_config(dataset_config)
        assert expected_output == mapped_dataset
