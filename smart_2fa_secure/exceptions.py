# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2021-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------


class Smart2FAError(Exception):
    """Basic 2FA Error"""
    pass


class InvalidCodeError(Smart2FAError):
    """Invalid code"""
    pass


class TooManyAttemptsError(Smart2FAError):
    """Number of attempts exceeded"""
    pass


class CodeExpiredError(Smart2FAError):
    """The code is out of date"""
    pass
