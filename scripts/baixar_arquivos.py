import requests
import os
from zipfile import ZipFile
from io import BytesIO
from bs4 import BeautifulSoup


class BaixarArquivos():
    def __init__(self):
        self.url = "https://revistas.inpi.gov.br/txt/P"
        self.ultima_edicao = BaixarArquivos.buscar_ultima_edicao()
        
    def edicao_desejada(self, numero_edicao:int):
        if numero_edicao < 1 or numero_edicao > self.ultima_edicao:
            return False
        return f"{self.url}{numero_edicao}"
    
    def baixando_edicao(self, numero_edicao:int, pasta_destino='edicoes'):
        response = requests.get(self.edicao_desejada(numero_edicao))
        response.raise_for_status()

        os.makedirs(pasta_destino, exist_ok=True)
        with ZipFile(BytesIO(response.content)) as z:
            z.extractall(f"{pasta_destino}/P{numero_edicao}")
        return f"{pasta_destino}/P{numero_edicao}"
    

    @staticmethod
    def buscar_ultima_edicao():
        url = "https://revistas.inpi.gov.br/rpi/"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        lastest_row = soup.find('tr', class_="warning")
        if not lastest_row:
            raise ValueError("Não foi possível encontrar a edição mais recente!")
        lastest_edition = int(lastest_row.find('td').get_text(strip=True))
        return lastest_edition
    

d = BaixarArquivos()
d.baixando_edicao(2552)
