from django import forms
from .models import *

doctors = Consulta.objects.order_by('nome_medico').values('cod_medico', 'nome_medico').distinct()

class ProducaoMedicaForm(forms.Form):
	filter_doctors = forms.ModelChoiceField(queryset=doctors)
