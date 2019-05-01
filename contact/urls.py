from django.urls import path
from . import views

app_name= 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_contact, name='create')
]