from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.home,name="home"),
    path('insert', views.insert,name="insert"),
    path('update',views.update,name="update"),
    path("delete/<deleteId>/",views.delete,name="delete"),
    path('contents',views.content,name="content"),
    # path("update",views.update,name="update"),
    
]
