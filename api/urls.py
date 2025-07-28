from home.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [

    path("trans/",tranaAPI.as_view()),
     path("login/",loginAPI.as_view()),
      path("register/",RegisterAPI.as_view()),
    path('bike/', bike),
]