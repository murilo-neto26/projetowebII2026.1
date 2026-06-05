from django import forms
from django.contrib.auth.models import User
from.models import Perfil
from .models import Lista, Desenho

class CadastroForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput)
    foto=forms.ImageField(required=False)
    
    class Meta:
        model=User
        fields=['username','email','password']
    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class ListaForm(forms.ModelForm):
    desenhos = forms.ModelMultipleChoiceField(
        queryset=Desenho.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Lista
        fields = ['nome', 'desenhos']