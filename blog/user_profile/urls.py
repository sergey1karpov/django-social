from django.urls import path
from . import views

app_name = 'user_profile'

urlpatterns = [
    path('information/', views.profile_info, name='profile_information'),
    path('information/edit', views.edit_profile_info, name='edit_information'),
]
