# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2021-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from .core import Smart2FA
from .backends.redis import RedisBackend
from .backends.telegram import TelegramSender

__all__ = ["Smart2FA"]
__version__ = "0.2.3"
