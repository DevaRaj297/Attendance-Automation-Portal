from django.urls import path
from django.contrib.auth import views as auth_views

from . import views as user_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('register/', user_views.studentRegister, name="register"),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),

    path('register/f/', user_views.facultyRegister, name='faculty-register'), #Faculty Register
    # path('profile/', user_views.profile, name="profile"),   
]

