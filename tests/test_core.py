from unittest.mock import Mock
from smart_2fa_secure.core import TwoFactorAuth


def test_custom_title_in_send_code():
    mock_sender = Mock()
    mock_storage = Mock()
    mock_storage.generate_code.return_value = "ABC123"
    mock_sender.send_code.return_value = True

    two_fa = TwoFactorAuth(mock_sender, mock_storage)
    two_fa.send_code("user1", "chat1", title="Your Access Code")

    mock_sender.send_code.assert_called_once_with("chat1", "ABC123", "Your Access Code")


def test_special_character_code_verification():
    mock_sender = Mock()
    mock_storage = Mock()
    mock_storage.verify_code.return_value = True

    two_fa = TwoFactorAuth(mock_sender, mock_storage)
    assert two_fa.verify_code("user1", "A@b#C1") is True
