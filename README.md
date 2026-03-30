# Python Example

A small Python example for the official PostMX SDK.

This version uses the sync client, so it fits nicely in small scripts and smoke tests. You can create an API key in [dash.postmx.co](https://dash.postmx.co), keep [docs.postmx.co](https://docs.postmx.co) open for the API reference, and use [postmx.co](https://postmx.co) for the main product overview.

## Code

```python
import os
from postmx import PostMXSync
postmx = PostMXSync(os.environ["POSTMX_API_KEY"])
inbox = postmx.create_inbox({"label": "login", "lifecycle_mode": "temporary", "ttl_minutes": 15})
message = postmx.wait_for_message(inbox["id"], timeout=120)
print(message.get("otp") or message["links"][0]["url"])
```

## Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
POSTMX_API_KEY=pmx_live_your_key_here python catch_login_email.py
```

The example file is [`catch_login_email.py`](./catch_login_email.py).

## Output

```text
Send your app email to: calm-river@test.postmx.email
Subject: Your login code
OTP: 482910
Link: https://app.example.com/login?token=...
```
