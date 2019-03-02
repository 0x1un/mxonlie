# -*- coding: utf-8 -*-


__author__ = '0x1un'
__date__ = '12/2/18 1:23 PM'
import string
import random
from users.models import EmailVerifyRecord
from django.core.mail import send_mail
from MxOnline.settings import EMAIL_FROM


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    # code is random strings
    code = generate_random_str(8)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    # sending email
    email_title, email_body = "", ""
    if send_type == "register":
        email_title = "MxOnline Register Active Url"
        email_body = "Please click on the link below to activate: http://localhost:8000/active/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            print("sending email is successful")
    elif send_type == "forget":
        email_title = "MxOnline Forget Password Url"
        email_body = "Please click on the link below to activate:\n http://localhost:8000/reset/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            print("sending email is successful")



    pass


def generate_random_str(randomLength):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=random.randint(randomLength, len(chars))))
