from django.urls import include, path
from .views import registration, profile, profileself
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("register/", registration, name="user_registration"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="user_login"),
    path("logout/", LogoutView.as_view(template_name="users/logout.html"), name="user_logout"),
    path("profileself/",profileself , name="user_profile_self"),
    path("profile/<int:id>",profile , name="user_profile"),


]
