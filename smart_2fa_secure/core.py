# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2021-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from typing import Optional
from .backends.redis import RedisBackend
from .backends.telegram import TelegramSender
from .exceptions import InvalidCodeError, TooManyAttemptsError
from .generators import CodeGenerator


class Smart2FA:
    def __init__(
            self,
            redis_host: str = "localhost",
            redis_port: int = 6379,
            telegram_token: Optional[str] = None,
            code_ttl: int = 60,
            max_attempts: int = 3,
            code_length: int = 6,
    ):
        self.backend = RedisBackend(redis_host, redis_port)
        self.sender = TelegramSender(telegram_token) if telegram_token else None
        self.code_ttl = code_ttl
        self.max_attempts = max_attempts
        self.code_generator = CodeGenerator()
        self.code_length = code_length

    def generate_code(self, length: int = 6) -> str:
        return self.code_generator.generate_code(length)

    def send_code(self, user_id: str, recipient: str, message: str) -> str:
        code = self.generate_code(self.code_length)
        text = f"{message}\n\n{code}"
        self.backend.store_code(user_id, code, self.code_ttl)
        self.backend.reset_attempts(user_id)

        if self.sender:
            self.sender.send_message(recipient, text)

        return code

    def verify_code(self, user_id: str, code: str) -> bool:
        attempts = self.backend.get_attempts(user_id)

        if attempts >= self.max_attempts:
            raise TooManyAttemptsError("Number of attempts exceeded")

        if not self.backend.verify_code(user_id, code):
            self.backend.increment_attempts(user_id)
            raise InvalidCodeError("Invalid code")

        self.backend.delete_code(user_id)
        return True
