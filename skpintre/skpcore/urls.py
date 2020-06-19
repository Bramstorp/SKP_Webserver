from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"), 
    path("husregler/", views.husregler, name="husregler"), 

    path("login/", views.loginpage, name="loginpage"), 
    path("signup/", views.signuppage, name="signuppage"),
    path("logout/", views.logoutUser, name="logoutUser"),

    path("info/", views.info, name="info"),
    path("idekasse/", views.idekasse, name="idekasse"),
    path("ide/<str:pk>/", views.ide, name="ide"),
]