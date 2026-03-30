# Python Example

Minimal PostMX example in Python.

Links:
- [postmx.co](https://postmx.co)
- [dash.postmx.co](https://dash.postmx.co)
- [docs.postmx.co](https://docs.postmx.co)

## Code

```python
inbox = postmx.create_inbox({"label": "login", "lifecycle_mode": "temporary"})
message = postmx.wait_for_message(inbox["id"])
print(message.get("otp") or message["links"][0]["url"])
```

The actual file stays under 10 lines.

## Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
POSTMX_API_KEY=pmx_live_your_key_here python catch_login_email.py
```

## Output

```text
Send your app email to: calm-river@test.postmx.email
Subject: Your login code
OTP: 482910
Link: https://app.example.com/login?token=...
```

## File

- `catch_login_email.py`
