import requests
from bs4 import BeautifulSoup
from input_interface import url

response = requests.get(url)
targetURL = BeautifulSoup(response.text,'html.parser')

def scrape_temper (temper: str):
    temper_list = targetURL.find(id=temper).find_next().contents
    temper_score = temper_list[4]
    temper_tier = temper_list[8]
    match temper:
        case 'Ansiedade'|'Raiva'|'Melancolia'|'Autoconsciência'|'Impulsividade'|'Vulnerabilidade':
            greatfive = 'Neurociticismo'
        case 'Simpatia'|'Simpatia'|'Sociabilidade'|'Assertividade'|'Atividade'|'Busca de Sensações'|'Emoções Positivas':
            greatfive = 'Extroversão'
        case 'Fantasia'|'Estética'|'Emotividade'|'Aventura'|'Intelecto'|'Liberalismo':
            greatfive = 'Abertura a Extroversão'
        case 'Confiança'|'Moralidade'|'Altruísmo'|'Cooperação'|'Modéstia'|'Empatia':
            greatfive = 'Afabilidade'
        case 'Autoeficácia'|'Ordem'|'Senso de Dever'|'Realização-Esforço'|'Autodisciplina'|'Cautela':
            greatfive = 'Consciência'
    return [greatfive, temper, temper_score, temper_tier]
