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

from smart_2fa_secure.exceptions import InvalidCodeError


def test_full_flow(smart_2fa, mock_requests):
    # Mock Telegram response
    mock_response = MagicMock()
    mock_response.json.return_value = {"ok": True}
    mock_requests.return_value = mock_response

    # Mock Redis responses
    smart_2fa.backend.get_attempts.return_value = 0
    smart_2fa.backend.verify_code.return_value = True

    # 1. Send code
    code = smart_2fa.send_code("user1", "chat123", "message")
    assert code is not None

    # 2. Verify code
    assert smart_2fa.verify_code("user1", code) is True

    # Verify all expected calls were made
    smart_2fa.backend.store_code.assert_called_once()
    smart_2fa.backend.reset_attempts.assert_called_once_with("user1")
    mock_requests.assert_called_once()
    smart_2fa.backend.verify_code.assert_called_once_with("user1", code)
    smart_2fa.backend.delete_code.assert_called_once_with("user1")


def test_invalid_code_flow(smart_2fa, mock_requests):
    # Mock Telegram response
    mock_response = MagicMock()
    mock_response.json.return_value = {"ok": True}
    mock_requests.return_value = mock_response

    # Mock Redis responses
    smart_2fa.backend.get_attempts.side_effect = [0, 1]
    smart_2fa.backend.verify_code.side_effect = [False, True]

    # 1. Send code
    code = smart_2fa.send_code("user1", "chat123", "message")

    # 2. First verification fails
    with pytest.raises(InvalidCodeError):
        smart_2fa.verify_code("user1", "wrong_code")

    # 3. Second verification succeeds
    assert smart_2fa.verify_code("user1", code) is True

    # Verify attempts were incremented
    smart_2fa.backend.increment_attempts.assert_called_once_with("user1")
