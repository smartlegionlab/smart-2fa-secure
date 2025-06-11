# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2021-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import string

import redis
import secrets


class Redis2FABackend:
    def __init__(self, host: str = "localhost", port: int = 6379, db: int = 0):
        self.r = redis.Redis(host=host, port=port, db=db)

    def generate_code(self, user_id: str, ttl: int = 60, length=6) -> str:
        characters = string.ascii_letters + string.digits + string.punctuation
        code = ''.join(secrets.choice(characters) for _ in range(length))
        self.r.setex(f"2fa:{user_id}", ttl, code)
        return code

    def verify_code(self, user_id: str, code: str) -> bool:
        stored_code = self.r.get(f"2fa:{user_id}")
        return stored_code and stored_code.decode() == code
