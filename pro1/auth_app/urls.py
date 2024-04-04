from django.urls import path
from .views import user_login, user_signup, user_logout

urlpatterns = [
    path("login/",user_login,name="login_url"),
    path("logout/",user_logout,name="logout_url"),
    path("signup/",user_signup,name="signup_url")
]