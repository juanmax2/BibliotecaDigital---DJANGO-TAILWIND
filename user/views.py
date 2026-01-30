from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, FormView
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        return super().form_valid(form)
    


class LoginView(FormView):
    template_name = 'core/login.html'
    form_class = LoginForm
    
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            
            login(self.request, user)
            messages.add_message(self.request, messages.SUCCESS, f"Welcome, {user.username}")
            
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.add_message(self.request, messages.ERROR, "Usuario o contraseña incorrecto")
            return super(LoginView, self).form_invalid(form)
        
@login_required
def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, "Se ha cerrado la sesión correctamente.")
    return HttpResponseRedirect(reverse('home'))