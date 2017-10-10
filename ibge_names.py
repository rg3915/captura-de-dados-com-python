import requests
import requests_cache


def _parse_response(json_response):
    if isinstance(json_response, dict) or json_response == []:
        freq = None
        name = None
        alternatives = None
    else:
        name = json_response[0]['nome']
        freq = json_response[0]['freq']
        alternatives = json_response[0]['nomes'].split(',')

    return name, freq, alternatives


def classify_by_sex(name):
    ''' Classify a name by sex using IBGE Nomes API '''
    # Obtenção
    url_male = 'https://servicodados.ibge.gov.br/api/v1/censos/nomes/basica?nome={}&sexo=m'
    url_female = 'https://servicodados.ibge.gov.br/api/v1/censos/nomes/basica?nome={}&sexo=f'
    response_male = requests.get(url_male.format(name))
    response_female = requests.get(url_female.format(name))

    # Extração
    json_male = response_male.json()
    json_female = response_female.json()

    male = _parse_response(json_male)
    female = _parse_response(json_female)

    if male[0] is not None:
        name = male[0]
    else:
        name = female[0]

    alternatives = []
    if male[2] is not None:
        alternatives.extend(male[2])
    if female[2] is not None:
        alternatives.extend(female[2])

    return {
        'name': name,
        'male': male[1],
        'female': female[1],
        'alternatives': alternatives,
    }


requests_cache.install_cache('ibge-names')
print(classify_by_sex('Regis'))
print(classify_by_sex('xv'))
