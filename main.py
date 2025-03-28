import requests
from bs4 import BeautifulSoup
from input_interface import url

response = requests.get(url)
targetURL = BeautifulSoup(response.text,'html.parser')

ansiedade_list = targetURL.find(id='Ansiedade').find_next().contents
ansiedade_score = ansiedade_list[4]
ansiedade_tier = ansiedade_list[8]
ansiedade = {"score": ansiedade_score, "tier": ansiedade_tier}

def scrape_temper (temper: str):
    temper_list = targetURL.find(id=f'{temper}').find_next().contents
    temper_score = temper_list[4]
    temper_tier = temper_list[8]
    return {"score": temper_score, "tier": temper_tier}

