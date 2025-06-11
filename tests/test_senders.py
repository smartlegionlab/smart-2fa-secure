from unittest.mock import patch
from smart_2fa_secure.interfaces import TelegramSender


def test_telegram_message_formatting():
    with patch("requests.post") as mock_post:
        mock_post.return_value.json.return_value = {"ok": True}
        sender = TelegramSender("fake-token")
        assert sender.send_code("chat123", "123456", title="Security Code") is True
        assert "Security Code" in mock_post.call_args[1]["json"]["text"]


def test_telegram_message_with_special_chars():
    with patch("requests.post") as mock_post:
        mock_post.return_value.json.return_value = {"ok": True}
        sender = TelegramSender("fake-token")
        code = "A1b2@#"
        assert sender.send_code("chat123", code) is True
        assert code in mock_post.call_args[1]["json"]["text"]
