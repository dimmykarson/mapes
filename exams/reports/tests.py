from django.test import TestCase
from .models import *
from django.db.models import Count

class ConsultaModelTests(TestCase):
	def setUp(self):
		Consulta.objects.create(valor_consulta=0, cod_medico=1)
		Consulta.objects.create(valor_consulta=-1, cod_medico=2)

	def test_valores_consultas(self):
		consultas_valor_negativo = Consulta.objects.filter(valor_consulta__lte=0).count()
		self.assertIs(consultas_valor_negativo, 0)
