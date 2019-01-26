import csv, os
from reports.models import *
from django.core.management.base import BaseCommand


settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

    	resource_path = os.path.join(PROJECT_ROOT, 'resources/')
    	insert_count = Consulta.objects.from_csv(resource_path+'consulta.csv', delimiter=';')
    	print("{} \'consulta\' records inserted".format(insert_count))


    	insert_count = Exame.objects.from_csv(resource_path+'exame.csv', delimiter=';')
    	print("{} \'exame\' records inserted".format(insert_count))



