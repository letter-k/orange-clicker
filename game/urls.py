from django.urls import path, include
from . import auth_views, views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path("login/", auth_views.login_view, name="login"),
    path('register/', auth_views.register_view, name='register'),
    path('password_reset/', auth_views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path("", views.home, name="home"),
]
