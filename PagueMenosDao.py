import re
import requests
import numpy as np
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('products.db')

cursor = conn.cursor()

def recoverMedicine(site):
    #cursor.execute("delete from Medicamento where id_empresa = 1;")
    page = requests.get(site)
    soup = BeautifulSoup(page.content, 'html.parser')
    medicines = soup.find_all('div', class_="product-content")
    for medicine in medicines:
        try:
            title = medicine.find('p', class_='price').a.get('title')
            price = medicine.find('p', class_='price').a.find('ins', class_='price-new').get_text()
            print(title)
            print(price)
#            cursor.execute("""
#                           INSERT INTO Medicamentos(id_empresa, nome, preco, peso, categoria, especial)
#                           VALUES (1,?,?)
#                           """, (title, price[0]))
        except AttributeError as e:
            print(" NAO CONSEGUIU RECUPERAR O ITEM ")
            continue        
            

#Recuperando itens de açougue do supermercado Zona Sul
def recoverMedicinePagueMenos():
    site = "https://www.paguemenos.com.br/medicamentos-e-saude";
    recoverMedicine(site)
    try:
        page = requests.get(site)
        soup = BeautifulSoup(page.content, 'html.parser')
        js = soup.find('div', class_='vitrine resultItemsWrapper').find('script').get_text()
        print(js)
        print(re.findall(r'pagecount_43841405 = \d+?',js))
        #p = re.compile('pagecount_43841405 = (.*?);')
        #pages = soup.find('div', class_='vitrine resultItemsWrapper')
        #num_pages = ast.literal_eval(re.search(r'\d+',pages[0].find('a', class_='last').get('onclick')).group(0))
        #num_page = 0
        #while (num_page < num_pages):
        #    s = "https://www.drogariavenancio.com.br/categoria.asp?idcategoria=1014&nivel=03&categoria=Medicamentos&viewType=M&nrRows=20&idPage=" + str(num_page) + "2&ordem=V"
        #    recoverMedicine(s)
        #    num_page += 1
    except AttributeError as e:
        ""
            
recoverMedicinePagueMenos()

conn.commit()
conn.close()
print('Dados inseridos com sucesso.')