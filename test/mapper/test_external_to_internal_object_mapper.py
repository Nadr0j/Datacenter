import pytest
from datacenter.mapper.external_to_internal_object_mapper import ExternalToInternalObjectMapper
from datacenter.model.external.MessageConfig import MessageConfig
from datacenter.model.external.RoleConfig import RoleConfig
from datacenter.model.internal.Message import Message
from datacenter.model.internal.Role import Role
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
