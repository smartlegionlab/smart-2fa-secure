# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2021-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from abc import ABC, abstractmethod
import requests


class CodeSender(ABC):
    @abstractmethod
    def send_code(self, recipient: str, code: str, title: str = 'Code:') -> bool:
        pass


class TelegramSender(CodeSender):
    def __init__(self, token: str):
        self.token = token

    def send_code(self, chat_id: str, code: str, title: str = 'Code:') -> bool:
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        message = f"{title}\n\n{code}"
        try:
            response = requests.post(url, json={"chat_id": chat_id, "text": message})
            return response.json().get("ok", False)
        except Exception as e:
            print(e)
            return False
