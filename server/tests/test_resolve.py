import pytest

from echo.controllers import get_echo
from messenger.controllers import send_message


from actions import resolve


@pytest.fixture
def initial_action_name_echo():
    return 'echo'


@pytest.fixture
def initial_action_name_send():
    return 'send'


def test_echo_resolve(initial_action_name_echo):
    actual_controller = resolve(initial_action_name_echo)
    assert actual_controller is get_echo


def test_send_resolve(initial_action_name_send):
    actual_controller = resolve(initial_action_name_send)
    assert actual_controller is send_message
