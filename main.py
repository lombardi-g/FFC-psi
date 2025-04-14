import requests
from bs4 import BeautifulSoup
from input_interface import url
import pandas as pd

response = requests.get(url)
targetURL = BeautifulSoup(response.text,'html.parser')

def scrape_temper (temper: str):
    temper_list = targetURL.find(id=temper).find_next().contents
    temper_score = int(temper_list[4])
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
    return [str(date),greatfive, temper, temper_score, temper_tier]

date = targetURL.find('span', class_='flex-1 text-inherit font-normal px-2').contents[0]

tempers = ['Ansiedade','Raiva','Melancolia','Autoconsciência','Impulsividade','Vulnerabilidade','Simpatia','Simpatia','Sociabilidade','Assertividade','Atividade','Busca de Sensações','Emoções Positivas','Fantasia','Estética','Emotividade','Aventura','Intelecto','Liberalismo','Confiança','Moralidade','Altruísmo','Cooperação','Modéstia','Empatia','Autoeficácia','Ordem','Senso de Dever','Realização-Esforço','Autodisciplina','Cautela']

results = []
for each in tempers:
    results.append(scrape_temper(each))
