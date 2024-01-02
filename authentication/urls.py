
from django.urls import path
from .views import AuthView




urlpatterns = [
    
    
    path('register',AuthView.register,name='register'),
    path('login',AuthView.login,name='login'),
    path('logout',AuthView.logout,name='logout')


]