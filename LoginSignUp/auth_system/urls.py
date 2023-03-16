from django.urls import path
from .views import HomePage, AuthenticationView, registerUser, loginUser, logoutUser

urlpatterns = [
    path('', HomePage, name="home-page"),
    path('auth/', AuthenticationView, name="auth-page"),
    path('registerUser/', registerUser, name='registerUser'),
    path('loginUser/', loginUser, name="loginUser"),
    path('logoutUser/', logoutUser, name="logoutUser")
]