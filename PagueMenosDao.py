import re
import requests
import numpy as np
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('products.db')

cursor = conn.cursor()

def recoverMedicine(site):    
    page = requests.get(site)
    soup = BeautifulSoup(page.content, 'html.parser')
    medicines = soup.find_all('div', class_="product-content")
    for medicine in medicines:
        try:
            title = medicine.find('p', class_='price').a.get('title')
            price = medicine.find('p', class_='price').a.find('ins', class_='price-new').get_text()
            print(title)
            print(re.findall(r'(\d+\,?\d*)',price)[0])
#            cursor.execute("""
#                           INSERT INTO Medicamentos(id_empresa, nome, preco, peso, categoria, especial)
#                           VALUES (1,?,?)
#                           """, (title, price[0]))
        except AttributeError as e:
            print(" NAO CONSEGUIU RECUPERAR O ITEM ")
            continue        
            
def recoverMedicinePagueMenos():
    #cursor.execute("delete from Medicamento where id_empresa = 1;")
    site = "https://www.paguemenos.com.br/medicamentos-e-saude";
    recoverMedicine(site)
    try:
        page = requests.get(site)
        soup = BeautifulSoup(page.content, 'html.parser')
        js = soup.find('div', class_='vitrine resultItemsWrapper').find('script').get_text()
        num_pages = ast.literal_eval(re.findall(r'\d+',js)[2])
        num_page = 2
        while (num_page < num_pages):
            s = "https://www.paguemenos.com.br/medicamentos-e-saude#" + str(num_page)
            recoverMedicine(s)
            num_page += 1
    except AttributeError as e:
        ""
            
recoverMedicinePagueMenos()

conn.commit()
conn.close()
print('Dados inseridos com sucesso.')