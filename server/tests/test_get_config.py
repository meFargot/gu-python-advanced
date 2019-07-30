import pytest

from configure import get_config


@pytest.fixture
def expected_addr():
    return 'localhost'


@pytest.fixture
def expected_port():
    return 7777


@pytest.fixture
def expected_buffersize():
    return 1024


@pytest.fixture
def expected_config(expected_addr, expected_port, expected_buffersize):
    return {
        'addr': expected_addr,
        'port': expected_port,
        'buffersize': expected_buffersize
    }

def test_addr_get_config(expected_config, expected_addr):
    actual_config = get_config()
    assert actual_config.get('addr') == expected_addr


def test_port_get_config(expected_config, expected_port):
    actual_config = get_config()
    assert actual_config.get('port') == expected_port


def test_buffersize_get_config(expected_config, expected_buffersize):
    actual_config = get_config()
    assert actual_config.get('buffersize') == expected_buffersize
