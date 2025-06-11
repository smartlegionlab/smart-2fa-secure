# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2021-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------


def test_store_code(redis_backend):
    user_id = "user1"
    code = "123456"
    ttl = 120

    redis_backend.store_code(user_id, code, ttl)
    redis_backend.conn.setex.assert_called_once_with(f"2fa:{user_id}", ttl, code)


def test_verify_code(redis_backend):
    user_id = "user1"
    code = "123456"

    # Test successful verification
    redis_backend.conn.get.return_value = code.encode()
    assert redis_backend.verify_code(user_id, code) is True
    redis_backend.conn.get.assert_called_once_with(f"2fa:{user_id}")

    # Test failed verification
    redis_backend.conn.get.return_value = "654321".encode()
    assert redis_backend.verify_code(user_id, code) is False

    # Test no code exists
    redis_backend.conn.get.return_value = None
    assert redis_backend.verify_code(user_id, code) is None


def test_delete_code(redis_backend):
    user_id = "user1"
    redis_backend.delete_code(user_id)
    redis_backend.conn.delete.assert_called_once_with(f"2fa:{user_id}")


def test_get_attempts(redis_backend):
    user_id = "user1"

    # Test with no attempts
    redis_backend.conn.get.return_value = None
    assert redis_backend.get_attempts(user_id) == 0

    # Test with attempts
    redis_backend.conn.get.return_value = b"3"
    assert redis_backend.get_attempts(user_id) == 3


def test_increment_attempts(redis_backend):
    user_id = "user1"
    redis_backend.increment_attempts(user_id)
    redis_backend.conn.incr.assert_called_once_with(f"2fa_attempts:{user_id}")
    redis_backend.conn.expire.assert_called_once_with(f"2fa_attempts:{user_id}", 3600)


def test_reset_attempts(redis_backend):
    user_id = "user1"
    redis_backend.reset_attempts(user_id)
    redis_backend.conn.delete.assert_called_once_with(f"2fa_attempts:{user_id}")
