from django.urls import path
from . import views

app_name = 'kalikha_api'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('signup/', views.sign_up, name='sign_up'),
    path('signin/', views.sign_in, name='sign_in'),
    path('signout/', views.sign_out, name='sign_out'),
    path('resources/', views.resource_listing_list, name='resource_listing_list'),
    path('resources/create/', views.create_resource_listing, name='create_resource_listing'),
    path('resources/<int:pk>/', views.resource_listing_detail, name='resource_listing_detail'),
    path('resources/<int:listing_pk>/add-material/', views.add_material_to_listing, name='add_material_to_listing'),
]