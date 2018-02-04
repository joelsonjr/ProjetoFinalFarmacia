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
            price = re.findall(r'(\d+\,?\d*)',medicine.find('p', class_='price').a.find('ins', class_='price-new').get_text())
            cursor.execute("""
                           INSERT INTO Medicamentos(id_empresa, nome, preco)
                           VALUES (9,?,?)
                           """, (title, price[0]))
        except AttributeError as e:
            continue        
            
def recoverMedicinePagueMenos():
    cursor.execute("delete from Medicamentos where id_empresa = 9;")
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
        
def selectMedicinePagueMenos():
    cursor.execute("select id_empresa, nome, preco from Medicamentos where id_empresa = 9;")
    data = []
    for row in cursor:
        data.append(row)
    return data
            
recoverMedicinePagueMenos()

conn.commit()
conn.close()
print('Dados inseridos com sucesso.')