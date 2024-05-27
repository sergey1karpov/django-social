from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = 'auth_module'

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='auth_module/actions/reset_password/password_reset_form.html',
        success_url=reverse_lazy('auth_module:password_reset_done',),
        email_template_name='auth_module/actions/reset_password/password_reset_email.html'
    ), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='auth_module/actions/reset_password/password_reset_done.html',
    ), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='auth_module/actions/reset_password/password_reset_new_password_form.html',
        success_url=reverse_lazy('auth_module:password_reset_complete')
    ), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='auth_module/actions/reset_password/password_reset_complete.html'
    ), name='password_reset_complete'),
]
