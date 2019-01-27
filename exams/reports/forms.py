from django import forms
from reports.models import *
from django.utils.translation import gettext as _

doctors_aux = Consulta.objects.distinct('cod_medico', 'nome_medico').order_by('nome_medico')

class DoctorProductionForm(forms.Form):
	doctors = forms.ModelChoiceField(required=False, label=_('Doctor').title(), 
		widget=forms.Select, 
		queryset=doctors_aux, 
		to_field_name="cod_medico")
	period = forms.DateField(required=False, label=_('Period').title(), widget=forms.TextInput(attrs={'type':'date'}),)
