# _*_ encoding: utf-8 _*_
__author__ = 'Jason'
__date__ = '2018/3/24 11:17'
from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=20)
    password = forms.CharField(required=True, min_length=6, max_length=20)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6, max_length=20)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class ResetPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(required=True, min_length=6, max_length=20)
    password2 = forms.CharField(required=True, min_length=6, max_length=20)
