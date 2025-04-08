from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('signUp/', views.sign_up, name='sign_up'),
    path('signIn/', views.sign_in, name='sign_in'),
    path('signOut/', views.sign_out, name='sign_out'),
]


app_name = 'kalikha_api'