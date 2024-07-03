from django.urls import path
from . import views

app_name = 'blogger'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('create_post', views.create_post, name='create_post')
]