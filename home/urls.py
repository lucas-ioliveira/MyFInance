from django.urls import path
from home.views import HomeView, UserRegisterView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', UserRegisterView.as_view(), name='register')


]