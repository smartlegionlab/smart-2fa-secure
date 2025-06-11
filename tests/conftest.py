import pytest
from unittest.mock import Mock
from smart_2fa_secure.backends.redis import Redis2FABackend
from smart_2fa_secure.interfaces import TelegramSender


@pytest.fixture
def mock_redis():
    return Mock(spec=Redis2FABackend)


@pytest.fixture
def mock_sender():
    return Mock(spec=TelegramSender)


@pytest.fixture
def redis_backend():
    return Redis2FABackend(db=9)


@pytest.fixture
def telegram_sender():
    return TelegramSender(token="test_token")
