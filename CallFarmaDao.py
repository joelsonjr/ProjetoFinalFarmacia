import re
import ast
import requests
import numpy as np
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('products.db')

cursor = conn.cursor()

def recoverMedicine(site):    
    page = requests.get(site)
    print(site)
    soup = BeautifulSoup(page.content, 'html.parser')
    medicines = soup.find_all('div', class_='boxProduto')
    for medicine in medicines:
        try:
            print(medicine.find('div', class_='detalhes').img.get('title').strip())
            price = medicine.find('div', class_='detalhes').find('div', class_='col-sm-12 text-center preco').get_text()
            print(re.findall(r'(\d+\,?\d*)',price)[0])
#            cursor.execute("""
#                           INSERT INTO Medicamentos(id_empresa, nome, preco, peso, categoria, especial)
#                           VALUES (1,?,?)
#                           """, (title, price[0]))
        except AttributeError as e:
            continue

            

def recoverMedicineCallFarma():
    #cursor.execute("delete from Medicamento where id_empresa = 1;")
    site = "https://www.callfarma.com.br/departamento/medicamentos";
    recoverMedicine(site)
    try:
        page = requests.get(site)
        soup = BeautifulSoup(page.content, 'html.parser')
        str_num_pages = re.findall(r'(\d+)', soup.find('div', class_='linkAtual').get_text())
        num_pages = ast.literal_eval(str_num_pages[0])
        num_page = 0        
        num_itens = 20
        while (num_page < num_pages):            
            s = "https://www.callfarma.com.br/departamento/medicamentos&limit=" + str(num_itens)
            recoverMedicine(s)
            num_itens += 20
            num_page += 1
    except AttributeError as e:
        ""
            
recoverMedicineCallFarma()

conn.commit()
conn.close()
print('Dados inseridos com sucesso.')