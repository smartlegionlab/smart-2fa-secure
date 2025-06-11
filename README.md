# Smart 2FA Security System
---

Advanced Two-Factor Authentication system with enhanced security features.

---


# Smart 2FA Security System

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
  - Customizable code length (default: 6, configurable up to 64)
  
- ⏱ **Flexible Expiration**:
  - Adjustable TTL (Time-To-Live) for codes
  - Default 60 seconds expiration

- 📱 **Secure Delivery**:
  - Telegram integration with customizable message templates
  - Support for special characters in codes

## Installation

```bash
pip install smart-2fa-secure
```

## Advanced Usage

### Generating Complex Codes

```python
from smart_2fa_secure import Redis2FABackend

backend = Redis2FABackend()
# Generate 10-character code with special characters
code = backend.generate_code("user1", length=10, ttl=120)
```

### Customizing Telegram Messages

```python
from smart_2fa_secure import TelegramSender

sender = TelegramSender("YOUR_BOT_TOKEN")
# Send code with custom title
sender.send_code("chat123", "A1b2@#", title="Your Secure Code")
```

### Complete Example

```python
from smart_2fa_secure import TwoFactorAuth, Redis2FABackend, TelegramSender
from smart_2fa_secure.exceptions import InvalidCodeError

# Initialize with enhanced security
backend = Redis2FABackend(host="secure.redis.server", port=6379)
sender = TelegramSender(token="YOUR_BOT_TOKEN")
auth = TwoFactorAuth(sender, backend)

# Generate and send secure code
code = auth.send_code(
    user_id="user123",
    recipient="telegram_chat_id",
    title="Your Verification Code"
)

# Verify with complex code
try:
    auth.verify_code("user123", "A1b2@#")
    print("Authentication successful!")
except InvalidCodeError:
    print("Invalid security code!")
```

## Security Best Practices

1. **Use long codes** (minimum 8 characters) for sensitive operations
2. **Include special characters** in generated codes
3. **Set short TTL** (30-60 seconds) for time-sensitive operations
4. **Rotate Telegram bot tokens** regularly

## Testing Security Features

```bash
pytest tests/ --cov=smart_2fa_secure --cov-report=html
open htmlcov/index.html
```

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