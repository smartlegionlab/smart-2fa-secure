# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2021-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from .core import TwoFactorAuth
from .backends.redis import Redis2FABackend
from .interfaces import TelegramSender

__all__ = ["TwoFactorAuth", "Redis2FABackend", "TelegramSender"]
__version__ = "0.1.1"
