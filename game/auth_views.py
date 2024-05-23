from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages
from .forms import CustomUserCreationForm
from .forms import CustomLoginForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

def unauthenticated_user(view_func):
    @user_passes_test(lambda user: not user.is_authenticated, login_url="/")
    def wrapper_func(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)

    return wrapper_func

def login_view(request):
    if request.method == "POST":
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Добро пожаловать!")
            return redirect('home')
        else:
            messages.error(request, "Неправильное имя пользователя или пароль.")
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация прошла успешно!")
            return redirect('home')
        else:
            messages.error(request, "Пожалуйста, исправьте ошибки.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')
    form_class = SetPasswordForm

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'
