# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2021-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from .interfaces import CodeSender
from .exceptions import InvalidCodeError


class TwoFactorAuth:
    def __init__(self, code_sender: CodeSender, storage_backend):
        self.sender = code_sender
        self.storage = storage_backend

    def send_code(self, user_id: str, recipient: str, title: str = 'Code:', length=6) -> str:
        code = self.storage.generate_code(user_id, length=length)
        if not self.sender.send_code(recipient, code, title):
            raise RuntimeError("Error sending code")
        return code

    def verify_code(self, user_id: str, code: str) -> bool:
        if not self.storage.verify_code(user_id, code):
            raise InvalidCodeError("Invalid code")
        return True
