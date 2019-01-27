from django.shortcuts import render, redirect
from django.contrib.auth.forms import  UserCreationForm
from django.http import HttpResponse
from reports.models import *
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q, Sum, Count
from django.db.models.functions import Coalesce
import locale
from .forms import DoctorProductionForm

def index(request):
	form = DoctorProductionForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
	return render(request, 'reports/index.html', {'form':form})
	
class DoctorProductionJSON(BaseDatatableView):
	columns = ['nome_medico', 'numero_guia_consulta', 'data_consulta', 'valor_consulta', 'gasto', 'qt_exames']
	order_columns = ['gasto', 'nome_medico', 'numero_guia_consulta', 'data_consulta', 'valor_consulta', 'qt_exames']
	max_display_length = 50
	model = Consulta

	def filter_queryset(self, qs):
		doc_cod = self.request.GET.get('doctor_cod')
		period = self.request.GET.get('period')
		print(doc_cod, period)
		if doc_cod:
			qs = qs.filter(cod_medico=doc_cod)
		if period:
			qs = qs.filter(data_consulta=period)
		qs = qs\
		.annotate(gasto=Coalesce(Sum('exame__valor_exame'), 0), qt_exames=Count('exame'))
		return qs

	def prepare_results(self, qs):
		locale.setlocale( locale.LC_ALL, '' )
		json_data = []
		for item in qs:
			gasto = item.gasto
			if not item.gasto:
				gasto = 0
			json_data.append([
				item.nome_medico, 
				item.numero_guia_consulta,  
				item.data_consulta.strftime("%d/%m/%Y"),
				locale.currency(item.valor_consulta),
				locale.currency(gasto),
				item.qt_exames
				])
		return json_data