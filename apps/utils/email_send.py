# _*_ encoding: utf-8 _*_
__author__ = 'Jason'
__date__ = '2018/3/24 16:46'

from random import Random

from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from mxonline.settings import EMAIL_FROM


def send_email(email, send_type):
    code = random_str(16)
    email_record = EmailVerifyRecord()
    email_record.email = email
    email_record.code = code
    email_record.send_type = send_type
    email_record.save()

    if send_type == "register":
        email_title = "慕学在线网注册激活链接"
        email_body = "请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "慕学在线网重置密码链接"
        email_body = "请点击下面的链接重置密码：http://127.0.0.1:8000/reset/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass


def send_register_email(email):
    send_email(email, "register")


def send_forget_pwd_email(email):
    send_email(email, "forget")


def random_str(random_length=8):
    str = ""
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
    length = len(chars)
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length - 1)]
    return str
