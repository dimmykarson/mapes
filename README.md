Teste programador Django
O teste consiste em implementar um caso de uso.
Exigências: django, jquery, ajax, bootstrap, postgres, teste unitário.

Caso de Uso: Emitir relatório de produção médica
Opções de Filtros:
Nome do Médico SELECTBOX não orbigatório
Período DD/MM/AAAA não obrigatório Período relacionado a data da consulta

Requisitos para o sistema: postgresql


Para executar o sistema, as dependencias devem ser instaladas como segue:

'''
pip install -r requirements.txt
'''

Os dados base estão no arquivo db.json. Para executar, crie um database chamado mapes_application (pode ser modificado, desde que modifique as condigurações de banco constantes no arquivo settings.py)
Para importar os dados rode:
'''
python manage.py migrate 
python manage.py loaddata db.json
'''


Para executar o serviço:
'''
python manage.py runserver
'''

Material auxiliar enviado :
Tabela consulta contém as consultas realizadas por pacientes
Tabela exame contém os exames solicitados na consulta. Podem haver 0 ou mais exames
por consulta.