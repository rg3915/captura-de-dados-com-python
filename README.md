# Captura de Dados com Python

#### Tutorial Captura de dados com Python PyBR 13

by [@turicas](https://github.com/turicas)


## Instalação

```bash
pip install rows click lxml requests requests-cache xlrd xlwt ipython ipdb
```

[bit.ly/pybr13-gn](bit.ly/pybr13-gn)


## Dados


### Obtenção

* scrapy
* requests
* urllib
* selenium
* mechanize
* wget
* aria2


### Extração

* Beautiful Soup
* etree
* pdfminer
* pdftotext (poppler)
* [rows](https://github.com/turicas/rows)
* selector
* slate
* pandas
* gunzip, unar
* lxml
* regexp
* string manipulation
* json
* [jsonbender](https://github.com/Onyo/jsonbender)

[http://censo2010.ibge.gov.br/nomes](http://censo2010.ibge.gov.br/nomes)


```python
names = rows.import_from_csv('names.csv')

for name in names:
    print(name)

alternatives = set()
for name in names:
    alternatives.update(name.alternatives)

print(alternatives)

sum(name.female for name in names)

```

[generonumero/logradouros](https://github.com/generonumero/logradouros)

https://www.sports-reference.com/olympics/countries/BRA/summer/2012

https://cidades.ibge.gov.br/comparamun/compara.php?idtema=1&codv=v01&coduf=33


* xpath -> lxml
* CSS Select
* Beautiful Soup
* regexp
* string manipulation
* rows

```python
rows convert --input-locale=pt_BR.UTF-8 "https://cidades.ibge.gov.br/comparamun/compara.php?idtema=1&codv=v01&coduf=31" mg.csv

rows query --input-locale=pt_BR.UTF-8 "pessoas > 500000" "https://cidades.ibge.gov.br/comparamun/compara.php?idtema=1&codv=v01&coduf=31" --output=top-mg.xls

ou

rows convert --input-locale=pt_BR.UTF-8
rows query 'pessoas > 500000' mg.csv
```

```python
import rows
import requests
import io

url = 'https://cidades.ibge.gov.br/comparamun/compara.php?idtema=1&codv=v01&coduf=31'
response = requests.get(url)
mg = rows.import_from_html(io.BytesIO(response.content))
mg[0]

with rows.locale_context('pt_BR.UTF-8'):
    mg = rows.import_from_html(io.BytesIO(response.content))

sum(municipio.pessoas for municipio in mg)
```

**Dica:** `$x()` no inspect.

