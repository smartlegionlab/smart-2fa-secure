# Smart 2FA Security System <sup>v0.2.3</sup>

---

Advanced Two-Factor Authentication system with enhanced security features.

---

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-BSD--3--Clause-blue)]()
[![Security](https://img.shields.io/badge/security-high-brightgreen)]()

![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smart-2fa-secure)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smart-2fa-secure)](https://github.com/smartlegionlab/smart-2fa-secure/)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smart-2fa-secure)](https://github.com/smartlegionlab/smart-2fa-secure/blob/master/LICENSE)
[![GitHub Repo stars](https://img.shields.io/github/stars/smartlegionlab/smart-2fa-secure?style=social)](https://github.com/smartlegionlab/smart-2fa-secure/)
[![GitHub watchers](https://img.shields.io/github/watchers/smartlegionlab/smart-2fa-secure?style=social)](https://github.com/smartlegionlab/smart-2fa-secure/)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/smart-2fa-secure?style=social)](https://github.com/smartlegionlab/smart-2fa-secure/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/smart-2fa-secure?label=pypi%20downloads)](https://pypi.org/project/smart-2fa-secure/)
[![PyPI](https://img.shields.io/pypi/v/smart-2fa-secure)](https://pypi.org/project/smart-2fa-secure)
[![PyPI - Format](https://img.shields.io/pypi/format/smart-2fa-secure)](https://pypi.org/project/smart-2fa-secure)



## Key Security Features

- 🔐 **Complex Code Generation**: 
  - Supports ASCII letters, digits and special characters
  - Customizable code length (default: 6)
  
- ⏱ **Flexible Expiration**:
  - Adjustable TTL (Time-To-Live) for codes
  - Default 60 seconds expiration

- 📱 **Secure Delivery**:
  - Telegram integration with customizable message templates

## Installation

```bash
pip install smart-2fa-secure
```

## Advanced Usage

```python
from smart_2fa_secure import Smart2FA
from smart_2fa_secure.exceptions import InvalidCodeError

smart_2fa = Smart2FA(
  redis_host="localhost",
  redis_port=6379,
  telegram_token="YOUR_BOT_TOKEN",
  code_ttl=60,
  max_attempts=3,
  code_length=6,
)
code = smart_2fa.send_code(user_id="user1", recipient="1234567", message="Your code:")

# Verify with complex code
try:
    smart_2fa.verify_code("user123", "A1b2@#")
    print("Authentication successful!")
except InvalidCodeError:
    print("Invalid security code!")

```

## 💻 Information for developers:

- `pip install pytest`
- `pip install pytest-cov`
- `pip install setuptools`
- `pip install wheel`
- `pip install build`
- `pip install twine`

- `pytest tests/ -v`
- `pytest tests/ -v --cov=smart_2fa_secure --cov-report=html`
- `python -m build` or `python setup.py sdist bdist_wheel`
- `twine upload dist/*`


---

![LOGO](https://github.com/smartlegionlab/smart-2fa-secure/raw/master/data/images/cov.png)

---

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2025, A.A. Suvorov
    All rights reserved.
    --------------------------------------------------------
