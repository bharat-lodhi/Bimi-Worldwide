import random

from django.conf import settings

from django.core.mail import EmailMessage, EmailMultiAlternatives



def send_email_otp(email):
    otp = random.randint(100000, 999999)

    html_body = f"""
<!DOCTYPE html>
<html>
<body style="margin:0;padding:0;background:#f0f4f2;font-family:Arial,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="padding:40px 16px;">
    <tr><td align="center">
      <table width="520" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:14px;overflow:hidden;max-width:520px;width:100%;">

        <tr>
          <td style="background:linear-gradient(135deg,#d4821d,#cc8f44);padding:28px 36px;">
            <p style="margin:0;font-size:19px;font-weight:600;color:#ffffff;">Bimi Worldwide</p>
            <p style="margin:4px 0 0;font-size:11px;color:#9FE1CB;letter-spacing:0.12em;text-transform:uppercase;">Verification Code</p>
          </td>
        </tr>

        <tr>
          <td style="padding:32px 36px;">
            <p style="margin:0 0 20px;font-size:15px;color:#444444;line-height:1.7;">Here is your one-time verification code:</p>

            <table width="100%" cellpadding="0" cellspacing="0" style="margin:0 0 20px;">
              <tr>
                <td style="background:#E1F5EE;border:1.5px solid #5DCAA5;border-radius:12px;padding:22px;text-align:center;">
                  <p style="margin:0 0 10px;font-size:11px;color:#0F6E56;letter-spacing:0.12em;text-transform:uppercase;font-weight:600;">OTP</p>
                  <p style="margin:0;font-family:'Courier New',monospace;font-size:38px;font-weight:700;color:#085041;letter-spacing:0.2em;">{otp}</p>
                  <p style="margin:10px 0 0;font-size:12px;color:#1D9E75;">Expires in <strong style="color:#085041;">10 minutes</strong></p>
                </td>
              </tr>
            </table>

            <p style="margin:0;font-size:13px;color:#888888;line-height:1.65;">
              Do not share this code with anyone. If you didn't request this, ignore this email.
            </p>
          </td>
        </tr>

        <tr>
          <td style="border-top:1px solid #eef5f1;padding:16px 36px;text-align:center;">
            <p style="margin:0;font-size:12px;color:#bbbbbb;">Bimi Worldwide &nbsp;·&nbsp; Do not reply to this email</p>
          </td>
        </tr>

      </table>
    </td></tr>
  </table>
</body>
</html>
"""

    text_body = f"Your Bimi Worldwide verification code is: {otp}\n\nExpires in 10 minutes. Do not share this code."

    msg = EmailMultiAlternatives(
        subject="Your Verification Code — Bimi Worldwide",
        body=text_body,
        from_email=settings.FROM_EMAIL,
        to=[email],
        reply_to=[settings.REPLY_TO_EMAIL],
    )
    msg.attach_alternative(html_body, "text/html")
    msg.send(fail_silently=False)

    return otp


# # =========================================================
# # send_otp.py
# # =========================================================

# import random

# from django.conf import settings

# from django.core.mail import EmailMessage


# def send_email_otp(email):

#     # GENERATE OTP
#     otp = random.randint(100000, 999999)

#     # EMAIL BODY
#     body = f"""
# Hello,

# Your OTP verification code is:

# {otp}

# Do not share this OTP with anyone.

# Thanks
# """

#     # EMAIL OBJECT
#     email_message = EmailMessage(
#         subject="Email Verification OTP",
#         body=body,

#         # USER KO YE MAIL DIKHEGI
#         from_email=settings.FROM_EMAIL,

#         to=[email],

#         # REPLY YAHAN AAYEGA
#         reply_to=[settings.REPLY_TO_EMAIL],
#     )

#     # ACTUAL SMTP LOGIN
#     email_message.connection = None

#     # SEND MAIL
#     email_message.send(
#         fail_silently=False
#     )

#     return otp