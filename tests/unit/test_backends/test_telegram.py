# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2021-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
from unittest.mock import MagicMock


def test_send_message_success(telegram_sender, mock_requests):
    mock_response = MagicMock()
    mock_response.json.return_value = {"ok": True}
    mock_requests.return_value = mock_response

    result = telegram_sender.send_message("chat123", "Your code: 123456")
    assert result is True
    mock_requests.assert_called_once()

    # Check URL and payload
    assert telegram_sender.base_url in mock_requests.call_args[0][0]
    payload = mock_requests.call_args[1]['json']
    assert payload["chat_id"] == "chat123"
    assert "123456" in payload["text"]


def test_send_code_failure(telegram_sender, mock_requests):
    mock_response = MagicMock()
    mock_response.json.return_value = {"ok": False}
    mock_requests.return_value = mock_response

    result = telegram_sender.send_message("chat123", "123456")
    assert result is False


def test_send_code_exception(telegram_sender, mock_requests):
    mock_requests.side_effect = Exception("Network error")
    result = telegram_sender.send_message("chat123", "123456")
    assert result is False
