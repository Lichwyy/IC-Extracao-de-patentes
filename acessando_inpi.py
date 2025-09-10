import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv



load_dotenv()

class AcessarInpi():
    def __init__(self):
        self.options = Options()
        self.options.headless = False
        self.navegador = webdriver.Firefox(options=self.options)
        self.link_login = "https://busca.inpi.gov.br/pePI/"
        self.link_pesquisa = "https://busca.inpi.gov.br/pePI/jsp/patentes/PatenteSearchBasico.jsp"

    def clicar(self, by_type, value:str):
        clicando = self.navegador.find_element(by=by_type, value=value)
        clicando.click()
    
    def enviar_dados(self, by_type, value:str, key:str):
        enviando = self.navegador.find_element(by=by_type, value=value)
        enviando.send_keys(key)

    def fazer_login(self):
        self.navegador.get(self.link_login)
        self.enviar_dados(By.NAME, 'T_Login', os.getenv("login"))
        self.enviar_dados(By.NAME, 'T_Senha', os.getenv("pass"))
        self.clicar(By.XPATH, "//input[@value=' Continuar » ']")

    def extraindo_dados(self):
        html = self.navegador.page_source
        soup = bs(html, "html.parser")

        patente = {}

        for tr in soup.find_all("tr"):
            alerta = tr.find("font", class_="alerta")
            if not alerta:
                continue
            inid = alerta.get_text(strip=True)

            td_valor = tr.find("td", align="left")
            if not td_valor:
                continue

            if td_valor.find("table"):
                sublista = []
                for sub in td_valor.find_all("tr")[1:]:
                    cols = sub.find_all("td")
                    sub_dict = {}
                    for i, col in enumerate(cols, start=1):
                        texto = col.get_text(strip=True)
                        if texto:
                            sub_dict[f"col{i}"] = texto
                    if sub_dict:
                        sublista.append(sub_dict) 
                if sublista:
                    patente[inid] = sublista
                continue

            links = td_valor.find_all("a")
            if links:
                lista_links = [l.get_text(strip=True) for l in links if l.get_text(strip=True)]
                patente[inid] = lista_links
                continue

            valor = td_valor.get_text(strip=True)
            if valor:
                patente[inid] = valor

        return patente 


    def acessando_pagina_patente(self, numpedido:str):
        self.navegador.get(self.link_pesquisa)
        self.enviar_dados(By.NAME, 'NumPedido', numpedido)
        self.clicar(By.XPATH, "//input[@value=' pesquisar » ']")
        self.clicar(By.XPATH, f"//a[normalize-space(text())='{numpedido}']")
        