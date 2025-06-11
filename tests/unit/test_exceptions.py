# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2021-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import pytest
from smart_2fa_secure.exceptions import (
    Smart2FAError,
    InvalidCodeError,
    TooManyAttemptsError,
    CodeExpiredError
)


def test_exception_hierarchy():
    assert issubclass(InvalidCodeError, Smart2FAError)
    assert issubclass(TooManyAttemptsError, Smart2FAError)
    assert issubclass(CodeExpiredError, Smart2FAError)


def test_exception_messages():
    with pytest.raises(InvalidCodeError, match="Invalid code"):
        raise InvalidCodeError("Invalid code")

    with pytest.raises(TooManyAttemptsError, match="Number of attempts exceeded"):
        raise TooManyAttemptsError("Number of attempts exceeded")

    with pytest.raises(CodeExpiredError, match="The code is out of date"):
        raise CodeExpiredError("The code is out of date")
