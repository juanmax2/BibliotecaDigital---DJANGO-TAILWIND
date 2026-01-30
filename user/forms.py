from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class RegistrationForm(UserCreationForm):
    
    birth_date = forms.DateField(
        label='Fecha de nacimiento',
        widget=forms.DateInput(attrs={'type':'date'})
    )
    
    class Meta(UserCreationForm.Meta):
        model = User
        
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'birth_date')
    
class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(),
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        estilo_input = "mb-3 px-2 appearance-none border-t-0 border-l-0 border-r-0 border-b border-teal-500 focus:ring-0 focus:border-teal-700"
        
        for field in self.fields.values():
            field.widget.attrs.update({'class': estilo_input})
            field.help_text = ''
        
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.helper.layout = Layout(
            'username',
            'password',
            Submit('submit', 'Iniciar Sesión', css_class="w-full bg-teal-600 text-white rounded-2xl mt-4 py-2 hover:bg-teal-700 transition-colors")
        )