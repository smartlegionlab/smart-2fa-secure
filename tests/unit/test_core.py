# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2021-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from unittest.mock import MagicMock

import pytest

from smart_2fa_secure.exceptions import InvalidCodeError, TooManyAttemptsError


def test_generate_code(smart_2fa):
    code = smart_2fa.generate_code()
    assert len(code) == 6
    assert any(c.isupper() for c in code)
    assert any(c.islower() for c in code)
    assert any(c.isdigit() for c in code)
    assert any(c in "!@#$%^&*" for c in code)


def test_send_code_with_telegram(smart_2fa, mock_requests):
    mock_response = MagicMock()
    mock_response.json.return_value = {"ok": True}
    mock_requests.return_value = mock_response

    smart_2fa.backend.store_code.return_value = None
    smart_2fa.backend.reset_attempts.return_value = None

    code = smart_2fa.send_code("user1", "chat123", "message")
    assert code is not None
    assert len(code) == 6
    smart_2fa.backend.store_code.assert_called_once()
    smart_2fa.backend.reset_attempts.assert_called_once_with("user1")
    mock_requests.assert_called_once()


def test_send_code_without_telegram():
    from smart_2fa_secure.core import Smart2FA
    smart_2fa = Smart2FA(telegram_token=None)
    smart_2fa.backend = MagicMock()

    code = smart_2fa.send_code("user1", "chat123", "message")
    assert code is not None
    assert len(code) == 6
    smart_2fa.backend.store_code.assert_called_once()
    smart_2fa.backend.reset_attempts.assert_called_once_with("user1")


def test_verify_code_success(smart_2fa):
    smart_2fa.backend.get_attempts.return_value = 0
    smart_2fa.backend.verify_code.return_value = True

    assert smart_2fa.verify_code("user1", "123456") is True
    smart_2fa.backend.delete_code.assert_called_once_with("user1")


def test_verify_code_invalid(smart_2fa):
    smart_2fa.backend.get_attempts.return_value = 0
    smart_2fa.backend.verify_code.return_value = False

    with pytest.raises(InvalidCodeError):
        smart_2fa.verify_code("user1", "wrong_code")
    smart_2fa.backend.increment_attempts.assert_called_once_with("user1")


def test_verify_code_too_many_attempts(smart_2fa):
    smart_2fa.backend.get_attempts.return_value = 3

    with pytest.raises(TooManyAttemptsError):
        smart_2fa.verify_code("user1", "123456")
