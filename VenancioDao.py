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
    medicines = soup.find_all('li', class_="nome")
        
    prices = soup.find_all('li', class_="precoPor")

    if len(medicines) != len(prices):
        return
    
    max_item = len(medicines)
    index = 0
    while (index < max_item):
        title = medicines[index].get_text().strip()
        p = prices[index].find('b').get_text()
        print(title)
        print(re.findall(r'(\d+\,?\d*)',p)[0])
        index += 1
#            cursor.execute("""
#                           INSERT INTO Medicamentos(id_empresa, nome, preco, peso, categoria, especial)
#                           VALUES (1,?,?)
#                           """, (title, price[0]))

def recoverMedicineVenancio():
    site = "https://www.drogariavenancio.com.br/departamento/1014/03/medicamentos";
    recoverMedicine(site)
    try:
        page = requests.get(site)
        soup = BeautifulSoup(page.content, 'html.parser')
        pages = soup.find_all('div', class_="paginacao")
        num_pages = ast.literal_eval(re.search(r'\d+',pages[0].find('a', class_='last').get('onclick')).group(0))
        num_page = 0
        while (num_page < num_pages):
            s = "https://www.drogariavenancio.com.br/categoria.asp?idcategoria=1014&nivel=03&categoria=Medicamentos&viewType=M&nrRows=20&idPage=" + str(num_page) + "2&ordem=V"
            recoverMedicine(s)
            num_page += 1
    except AttributeError as e:
        ""
        
#cursor.execute("delete from Medicamento where id_empresa = 1;")
recoverMedicineVenancio()

conn.commit()
conn.close()
print('Dados inseridos com sucesso.')