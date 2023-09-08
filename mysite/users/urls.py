from django.urls import path
from . import views

urlpatterns = [   
    path("", views.home, name = "home"),
    path("signup/", views.signup, name = "signup"),
    path("login_page/", views.login_page, name = "login_page"),
    path("loggedin_Home/",views.loggedin_Home, name = "loggedin_Home"),
]