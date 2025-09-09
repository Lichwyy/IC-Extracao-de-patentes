from acessando_inpi import AcessarInpi
from time import sleep
import json
import requests
import os
from dotenv import load_dotenv



load_dotenv()
numpedidos = ['BR 11 2012 015207 6', 'BR 11 2013 021204-7', 'BR 11 2013 021217-9']
dados = []

API_URL = os.getenv("API_URL")

def enviar_para_planilha(dados):
    """
    Envia os dados formatados como JSON para a planilha via Apps Script.
    """
    try:
        resposta = requests.post(API_URL, json=dados, timeout=30)
        print("Envio para API:", resposta.text, resposta.status_code)
    except Exception as e:
        print("Erro ao enviar para API:", e)

acessarinpi = AcessarInpi()
acessarinpi.fazer_login()

for n in numpedidos:
    acessarinpi.acessando_pagina_patente(n.replace('-', ' '))
    sleep(1)
    dados.append(acessarinpi.extraindo_dados())

enviar_para_planilha(dados)
