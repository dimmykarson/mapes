from django.db import models
from postgres_copy import CopyManager

class Consulta(models.Model):
    numero_guia_consulta = models.AutoField(primary_key=True)
    cod_medico = models.IntegerField()
    nome_medico = models.CharField(max_length=5000, blank=True, null=True)
    data_consulta = models.DateField(blank=True, null=True)
    valor_consulta = models.DecimalField(max_digits=1000, decimal_places=2, blank=True, null=True)
    objects = CopyManager()

    class Meta:
        db_table = 'consulta'

    def __str__(self):
        return self.nome_medico


class Exame(models.Model):
    cod_exame = models.IntegerField(primary_key=True)
    numero_guia_consulta = models.ForeignKey(
        Consulta, models.DO_NOTHING, 
        db_column='numero_guia_consulta', 
        default=None)
    valor_exame = models.DecimalField(max_digits=1000, decimal_places=2, blank=True, null=True)
    objects = CopyManager()

    class Meta:
        db_table = 'exame'
        unique_together = (('cod_exame', 'numero_guia_consulta'),)
