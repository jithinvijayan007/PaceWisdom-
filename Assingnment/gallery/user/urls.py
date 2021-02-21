from django.urls import path
from user import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name = "index"),
    path('about/', views.about, name = "about"),
    path('user/login/',auth_views.LoginView.as_view(template_name = "user/login.html"), name = "login"),
    path('user/logout/',auth_views.LogoutView.as_view(template_name = "user/logout.html"), name = "logout"),
    path('user/register/', views.register, name = "register"),


]