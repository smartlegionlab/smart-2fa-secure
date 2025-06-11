# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2021-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import requests


class TelegramSender:
    def __init__(self, token: str):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{self.token}"

    def send_message(self, chat_id: str, message: str = "") -> bool:
        try:
            url = f"{self.base_url}/sendMessage"
            payload = {
                "chat_id": chat_id,
                "text": f"{message}",
                "parse_mode": "HTML"
            }
            response = requests.post(url, json=payload)
            return response.json().get("ok", False)
        except Exception as e:
            print(e)
            return False
