# IC - Extração de Patentes

## 📖 Descrição

Este projeto faz parte de uma Iniciação Científica em Ciência da Computação e tem como objetivo **automatizar a extração, processamento e análise de dados de patentes** da Revista da Propriedade Industrial (RPI), publicada semanalmente pelo INPI.
O sistema baixa os arquivos da RPI, processa os dados, e reutiliza os números identificadores das patentes, para efetuar um scraping no site de consulta de patentes do INPI, o scraping retorna os dados, que são guaradados e enviados para uma planilha online e organiza para posterior análise.

Além disso, o projeto tem como visão futura a criação de uma **biblioteca Python** que permitirá consultas, filtros, análises e outras funcionalidades diretamente a partir dos dados extraídos.

## 🚀 Funcionalidades

* Baixar automaticamente as edições dos despachos da RPI.
* Scraping do portal de busca de patentes do INPI.
* Extrair e organizar os dados das patentes.
* Envio dos dados para uma planilha online no Google Sheets.
* Estruturação dos dados em abas organizadas.
* Possibilidade futura de API, biblioteca Python e visualizações gráficas.

## 📊 Bases de Dados Utilizadas

* **Revista da Propriedade Industrial (RPI)** → [https://revistas.inpi.gov.br/rpi/](https://revistas.inpi.gov.br/rpi/)
  Usada para coletar os **despachos de patentes**, permitindo mapear todas as patentes disponíveis e seus identificadores.

* **Busca Patente INPI** → [https://busca.inpi.gov.br/pePI/jsp/patentes/PatenteSearchBasico.jsp](https://busca.inpi.gov.br/pePI/jsp/patentes/PatenteSearchBasico.jsp)
  Utilizada para buscar informações detalhadas de cada patente a partir de seu número identificador.

## 📂 Estrutura do Repositório

* `acessando_inpi.py` → script para acessar o portal do INPI e navegar pelos dados.
* `baixar_arquivos.py` → realiza o download dos arquivos do site da revista RPI.
* `enviando_planilha.py` → envia/exporta os dados processados para planilhas (Google Sheets, Excel, etc).
* `Pipfile / Pipfile.lock` → controle das dependências do projeto.
* `README.md` → documentação do repositório.

## 🗂 Estrutura dos Dados (Planilha)

Os dados são organizados em uma planilha online, disponível para leitura neste link:
👉 [Planilha de Patentes](https://docs.google.com/spreadsheets/d/11iNsEaxtqCDp8DRnC5K_B4q0L57kWuzhOo1eBD044nA/edit?usp=sharing)

A planilha contém três abas principais:

* **Patentes** → principais informações de cada patente.
* **Classificações** → valores de classificação IPC e CPC.
* **Prioridades** → informações sobre prioridade unionista.

## ☁️ Integração com Google Sheets

Para viabilizar a integração com a planilha, foi desenvolvido um script em **Google Apps Script** associado à planilha.
Esse script recebe os dados via requisições HTTP e organiza nas abas descritas acima.

## 🛠️ Tecnologias Utilizadas

* Python 3.x
* [Requests](https://docs.python-requests.org/) – download e requisições HTTP
* [PyPDF2](https://pypi.org/project/PyPDF2/) – extração de texto dos PDFs
* [pandas](https://pandas.pydata.org/) – manipulação e análise de dados
* (futuro) [spaCy](https://spacy.io/) ou [NLTK](https://www.nltk.org/) – Processamento de Linguagem Natural
* PostgreSQL – armazenamento dos dados
* FastAPI – criação de API RESTful
* Google Apps Script – integração com Google Sheets

## 📦 Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/Lichwyy/IC-Extracao-de-patentes.git
   cd IC-Extracao-de-patentes
   ```

2. Instale as dependências com **Pipenv**:

   ```bash
   pipenv install
   ```

3. Ative o ambiente virtual:

   ```bash
   pipenv shell
   ```

## ▶️ Uso

* Todos os scripts Python estão localizados no diretório `scripts/`.  
Para executar qualquer um deles, certifique-se de navegar até essa pasta:

  ```bash
  cd scripts/
  ```

* Para baixar os PDFs da RPI:

  ```bash
  pipenv run python baixar_arquivos.py
  ```

* Para acessar diretamente dados do site do INPI:

  ```bash
  pipenv run python acessando_inpi.py
  ```

* Para enviar resultados para planilha:

  ```bash
  pipenv run python enviando_planilha.py
  ```

## ⚙️ Configuração de Variáveis de Ambiente

Este projeto depende de variáveis de ambiente para funcionar corretamente.  
Antes de rodar os scripts, crie um arquivo `.env` na raiz do projeto com as seguintes chaves:

- `API_URL` → URL da API do Google Apps Script para enviar os dados para a planilha desejada  
- `LOGIN_USER` → Nome de usuário para acesso do site INPI
- `LOGIN_PASS` → Senha para acesso do site INPI

Exemplo de conteúdo do arquivo `.env` no arquivo `.env.example`:

## 📌 Roadmap

* Desenvolver API RESTful (FastAPI).
* Implementar análise exploratória (pandas, matplotlib, seaborn).
* Criar relatórios e visualizações.
* Disponibilizar biblioteca Python para acesso e filtros de dados.

## 🎓 Instituição

Este projeto é desenvolvido no âmbito do **Programa Institucional de Iniciação Científica (PIIC)** da
**Universidade de Marília (UNIMAR)**.

## 👤 Autor

* **Paulo Henrique Almeida Veloso Leite** – Pesquisador bolsista (Universidade de Marília - UNIMAR)
* **Rafael Gutierres Castanha** – Orientador (Universidade de Marília - UNIMAR)

---

Este projeto contribui para democratizar o acesso a informações técnicas sobre patentes no Brasil e facilitar análises estratégicas em inovação e tecnologia.
