from django.urls import path, include
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    # path("account/", include('allauth.urls')),
    path('', views.login_signup, name="login_signup"),
    path("login/",views.login, name="login"),
    path("logout/",views.logout, name="logout"),
    path("signup/",views.signup, name="signup"),
    path("setting/", views.setting, name="setting"),
    
    
]
