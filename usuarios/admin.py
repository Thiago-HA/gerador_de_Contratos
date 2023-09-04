from django.contrib import admin
from .models import Usuario

from django import forms

class UsuarioAdminForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and instance.pk:
            self.fields['senha'].widget.attrs['value'] = instance.senha

class UsuarioAdmin(admin.ModelAdmin):
    form = UsuarioAdminForm
    

admin.site.register(Usuario, UsuarioAdmin)
