from django.shortcuts import render, redirect
from django.contrib.auth.forms import  UserCreationForm
from django.http import HttpResponse
from .models import *
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape


def index(request):
	consultas = Consulta.objects.all()
	return render(request, 'reports/index.html', {'consultas':consultas})



class DoctorProductionJSON(BaseDatatableView):
	model = Consulta
	columns = ['nome_medico', 'numero_guia_consulta', 'data_consulta', 'valor_consulta']
	order_columns = ['nome_medico']
	max_display_length = 50

	def render_column(self, row, column):
		return super(ProducaoMedicaJson, self).render_column(row, column)

	def filter_queryset(self, qs):
		return qs