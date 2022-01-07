from django.forms import ModelForm, fields
from .models import *

class CarroForm(ModelForm):
    class Meta:
        model = CarroModel
        fields = ['modelo', 'marca', 'ano', 'valor', 'data_cadastro']