import string
from smart_2fa_secure.backends.redis import Redis2FABackend


def test_code_generation_length():
    backend = Redis2FABackend(db=9)
    code = backend.generate_code("user1", length=8)
    assert len(code) == 8
    assert all(c in (string.ascii_letters + string.digits + string.punctuation) for c in code)


def test_special_characters_in_code():
    backend = Redis2FABackend(db=9)
    code = backend.generate_code("user1", length=20)
    assert any(c in string.punctuation for c in code)


def test_custom_ttl():
    backend = Redis2FABackend(db=9)
    code = backend.generate_code("user1", ttl=30)
    assert backend.verify_code("user1", code) is True
