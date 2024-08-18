from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from home.forms import CustomUserCreationForm


class HomeView(TemplateView):
    template_name = 'home/home.html'


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'home/register.html' 
    success_url = reverse_lazy('admin:index')