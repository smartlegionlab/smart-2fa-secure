# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2021-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import redis


class RedisBackend:
    def __init__(self, host: str = "localhost", port: int = 6379, db: int = 0):
        self.conn = redis.Redis(host=host, port=port, db=db)

    def store_code(self, user_id: str, code: str, ttl: int):
        self.conn.setex(f"2fa:{user_id}", ttl, code)

    def verify_code(self, user_id: str, code: str) -> bool:
        stored = self.conn.get(f"2fa:{user_id}")
        print(stored and stored.decode() == code)
        return stored and stored.decode() == code

    def delete_code(self, user_id: str):
        self.conn.delete(f"2fa:{user_id}")

    def get_attempts(self, user_id: str) -> int:
        return int(self.conn.get(f"2fa_attempts:{user_id}") or 0)

    def increment_attempts(self, user_id: str):
        self.conn.incr(f"2fa_attempts:{user_id}")
        self.conn.expire(f"2fa_attempts:{user_id}", 3600)

    def reset_attempts(self, user_id: str):
        self.conn.delete(f"2fa_attempts:{user_id}")
