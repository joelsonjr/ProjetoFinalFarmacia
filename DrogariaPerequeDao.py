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
    medicines = soup.find_all('div', class_='caption text-center')
    for medicine in medicines:
        try:
            title = medicine.p.get_text().strip()
            price = medicine.find_all('div')[2].find('div').find('div', class_='row').find('div').h4.find_all('label')[1].get_text()
            print(title)
            print(re.findall(r'(\d+\,?\d*)',price)[0])
#            cursor.execute("""
#                           INSERT INTO Medicamentos(id_empresa, nome, preco, peso, categoria, especial)
#                           VALUES (1,?,?)
#                           """, (title, price[0]))
        except AttributeError as e:
            continue

def recoverMedicineDrogariaPereque():
    #cursor.execute("delete from Medicamento where id_empresa = 1;")
    site = "https://www.drogariapereque.com.br/medicamentos";
    recoverMedicine(site)
    try:
        page = requests.get(site)
        soup = BeautifulSoup(page.content, 'html.parser')
        itens = soup.find_all('ul')[241].find_all('li')
        num_pages = len(itens)
        num_page = 2
        while (num_page < num_pages):            
            s = "https://www.drogariapereque.com.br/medicamentos?page=" + str(num_page)
            recoverMedicine(s)
            num_page += 1
    except AttributeError as e:
        ""
            
recoverMedicineDrogariaPereque()

conn.commit()
conn.close()
print('Dados inseridos com sucesso.')
