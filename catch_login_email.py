import os

from postmx import PostMXSync

postmx = PostMXSync(os.environ["POSTMX_API_KEY"])

inbox = postmx.create_inbox({"label": "login", "lifecycle_mode": "temporary", "ttl_minutes": 15})

print(f"Send your app email to: {inbox['email_address']}")

message = postmx.wait_for_message(inbox["id"], timeout=120)

print(f"Subject: {message.get('subject') or '(no subject)'}")

print(f"OTP: {message.get('otp') or 'none'}")

print(f"Link: {(message.get('links') or [{}])[0].get('url', 'none')}")
