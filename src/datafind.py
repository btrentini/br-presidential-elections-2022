
import requests
from bs4 import BeautifulSoup
 
# Isso aqui vai ajudar o site do TSE entender que eh um acesso de usuario, nao de robo
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

# Aqui vamos criar o conector para pegar os links
eletlink = requests.get("https://dadosabertos.tse.jus.br/dataset/resultados-2022-arquivos-transmitidos-para-totalizacao", headers=headers)
soup = BeautifulSoup(eletlink.content, 'html.parser')
 
# vamos salvas os links nessa lista
urls = []

# Analisando o website
# Vi que a classe da URL pra baixar os dados e resource-url-analytics
# Isso pode ser alterado
for link in soup.find_all('a', attrs={'class':'resource-url-analytics'}):
    if '.zip' in link.get('href'):
        urls.append(link.get('href'))

# create a wget command for the directory ./data for each file to be downloaded
with open("./resources/download_logs.sh", "w") as files:
    for url in urls:
        l = 'wget --user-agent="Mozilla" ' + url + ' -P ./data \n'
        files.write(l)

