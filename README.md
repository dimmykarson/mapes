# Teste programador Django
O teste consiste em implementar um caso de uso.
Exigências: django, jquery, ajax, bootstrap, postgres, teste unitário.

Caso de Uso: Emitir relatório de produção médica
Opções de Filtros:
Nome do Médico SELECTBOX não orbigatório
Período DD/MM/AAAA não obrigatório Período relacionado a data da consulta

Dependencies:

* Python 2.7/3.5 or later
* [Django](http://www.djangoproject.com/) >= 2.0
* [jQuery](https://jquery.com/) >= 2


Para executar o sistema, as dependencias devem ser instaladas como segue:

```bash
pip install -r requirements.txt
```

Os dados base estão no arquivo db.json. Para executar, crie um database chamado mapes_application (pode ser modificado, desde que modifique as condigurações de banco constantes no arquivo settings.py)
Para importar os dados rode:

```bash
python manage.py migrate 
python manage.py loaddata db.json
```


Para executar o serviço:

```bash
python manage.py runserver
```

Material auxiliar enviado :
Tabela consulta contém as consultas realizadas por pacientes
Tabela exame contém os exames solicitados na consulta. Podem haver 0 ou mais exames
por consulta.


## Authors

* Dimmy Magalhães


## Copyright and license

Creative Commons (cc0)

