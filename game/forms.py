from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Введите имя пользователя'
        }),
        label=_("Имя пользователя")
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Введите пароль'
        }),
        label=_("Пароль")
    )

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите email'
        }),
        label=_("Электронная почта")
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        labels = {
            'username': _('Имя пользователя'),
            'password1': _('Пароль'),
            'password2': _('Подтверждение пароля'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Введите имя пользователя'
        })
        self.fields['username'].label = _("Имя пользователя")
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Введите пароль'
        })
        self.fields['password1'].label = _("Пароль")
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Подтвердите пароль'
        })
        self.fields['password2'].label = _("Подтверждение пароля")
