# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2021-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from abc import ABC, abstractmethod


class CodeSender(ABC):
    @abstractmethod
    def send_code(self, recipient: str, message: str) -> bool:
        pass


class AttemptsManager(ABC):
    @abstractmethod
    def get_attempts_left(self, user_id: str) -> int:
        pass

    @abstractmethod
    def decrement_attempts(self, user_id: str) -> int:
        pass

    @abstractmethod
    def reset_attempts(self, user_id: str) -> None:
        pass
