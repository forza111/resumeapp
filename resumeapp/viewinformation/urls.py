from django.urls import path
from . import views

app_name = 'viewinformation'
urlpatterns=[
    path('', views.index, name ='index')
    ]