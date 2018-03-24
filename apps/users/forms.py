# _*_ encoding: utf-8 _*_
__author__ = 'Jason'
__date__ = '2018/3/24 11:17'
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=20)
    password = forms.CharField(required=True, min_length=6, max_length=20)
