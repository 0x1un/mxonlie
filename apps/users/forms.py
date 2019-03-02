# -*- coding: utf-8 -*-
__author__ = '0x1un'
__date__ = '11/28/18 6:36 PM'

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    # if required is set to True, an error is thrown when the value is empty
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField()


class ActiveForm(forms.Form):
    captcha = CaptchaField(error_messages={"invalid": "Verify code is error"})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": "Verify code is error"})


class ModifyPwdForm(forms.Form):
    MIN_LENGTH = 5
    password1 = forms.CharField(required=True, min_length=MIN_LENGTH)
    password2 = forms.CharField(required=True, min_length=MIN_LENGTH)