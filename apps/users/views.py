from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ActiveForm, ForgetForm, ModifyPwdForm
from utils.email_send import send_register_email


# Create your views here.

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            # verify that the account and password matches the database
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class ActiveUserView(View):
    # when users click on the activate link, jump to here, execute the following logic.
    def get(self, request, active_code):
        # filter the active_code, find the email and *is_active* flag
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        active_form = ActiveForm(request.GET)
        if all_records:
            for record in all_records:
                # because the *all_records* is a list, the have email, user and *is_active* flag inside
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True  # if *is_active* is True, the account are already activate, and vice versa
                user.save()  # save as
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {
                'msg': 'Your activate link is invalid',
                'active_form': active_form,
            })


class UserLogin(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():

            # get username and password from POST data form
            user_name = request.POST.get("username", '')
            pass_word = request.POST.get("password", '')
            user = authenticate(username=user_name, password=pass_word)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    # after the verification is successful, login to it.
                    return render(request, 'index.html')
                    # if the users login successfully, return home pages
                else:
                    return render(request, 'login.html', {'msg': 'Account does not activate.'})
            else:
                # if login failed. return again *login.html* and send error messages to front pages
                return render(request, 'login.html', {
                    'msg': 'Incorrect username or password!', })

        else:
            return render(request, 'login.html', {
                'login_form': login_form,
            })


# register accounts
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", '')
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {"register_form": register_form,
                                                         'msg': 'Account is already exists'})
            user_password = request.POST.get("password", '')

            user_profile = UserProfile()
            user_profile.username = user_name
            # the *make_password* are encryption user_name plaintext
            user_profile.password = make_password(user_password)
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.save()

            # sending email
            send_register_email(user_name, 'register')

            return render(request, "login.html")
        else:
            return render(request, 'register.html', {"register_form": register_form})


class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'forgetpwd.html', {
            'forget_form': forget_form
        })

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get("email", '')
            send_register_email(email, "forget")
            return render(request, "send_sucess.html")
        else:
            return render(request, 'forgetpwd.html', {
                'forget_form': forget_form
            })


class ResetPwdView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        active_form = ActiveForm(request.GET)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, 'password_reset.html', {
                'email': email
            })
        else:
            return render(request, 'register.html', {
                'msg': 'Your activate link is invalid',
                'active_form': active_form,
            })


class ModifyPwdView(View):
    def post(self, request):
        modifiy_form = ModifyPwdForm(request.POST)
        if modifiy_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            email = request.POST.get('email', '')
            if pwd1 != pwd2:
                return render(request, "password_reset.html", {
                    'email': email,
                    'msg': 'The passwords entered do not match',
                })
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()
            return render(request, 'login.html')
        else:
            email = request.POST.get('email', '')
            return render(request, 'password_reset.html', {
                'email': email,
                'modify_form': modifiy_form
            })
