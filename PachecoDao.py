import ast
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
    medicines = soup.find_all('a', class_='productPrateleira transition_all')
    for medicine in medicines:
        try:
            title = medicine.find('h3').get_text()
            price = re.findall(r'(\d+\,?\d*)',medicine.find('span', class_='bestPrice transition_all').find('span', class_='the-price').get_text())
            cursor.execute("""
                           INSERT INTO Medicamentos(id_empresa, nome, preco)
                           VALUES (8,?,?)
                           """, (title, price[0]))
        except AttributeError as e:
            continue        
            

def recoverMedicinePacheco():
    cursor.execute("delete from Medicamentos where id_empresa = 8;")
    site = "https://www.drogariaspacheco.com.br/medicamentos/";
    recoverMedicine(site)    
    try:
        page = requests.get(site)
        soup = BeautifulSoup(page.content, 'html.parser')
        str_num_itens = re.findall(r'(\d+)', soup.find('div', class_='vitrine resultItemsWrapper').find_all('script')[0].get_text())[2]
        num_pages = ast.literal_eval(str_num_itens)
        num_page = 1
        while (num_page < num_pages):            
            s = "https://www.drogariaspacheco.com.br/medicamentos/#" + str(num_page)
            recoverMedicine(s)
            num_page += 1
    except AttributeError as e:
        ""
        
def selectMedicinePacheco():
    cursor.execute("select id_empresa, nome, preco from Medicamentos where id_empresa = 8;")
    data = []
    for row in cursor:
        data.append(row)
    return data


recoverMedicinePacheco()

conn.commit()
conn.close()
print('Dados inseridos com sucesso.')

