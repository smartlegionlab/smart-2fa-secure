# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2021-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import pytest
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_redis():
    with patch('smart_2fa_secure.backends.redis.redis.Redis') as mock:
        mock.return_value = MagicMock()
        yield mock

@pytest.fixture
def mock_requests():
    with patch('requests.post') as mock:
        yield mock

@pytest.fixture
def redis_backend(mock_redis):
    from smart_2fa_secure.backends.redis import RedisBackend
    backend = RedisBackend()
    backend.conn = MagicMock()
    return backend

@pytest.fixture
def telegram_sender():
    from smart_2fa_secure.backends.telegram import TelegramSender
    sender = TelegramSender(token="test_token")
    sender.session = MagicMock()
    return sender

@pytest.fixture
def smart_2fa(mock_redis, mock_requests):
    from smart_2fa_secure.core import Smart2FA
    instance = Smart2FA(telegram_token="test_token")
    instance.backend = MagicMock()
    return instance
