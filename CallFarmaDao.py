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
    medicines = soup.find_all('div', class_='col-sm-12 text-center foto')
    prices = soup.find_all('div', class_='col-sm-12 text-center preco')
    
    print(len(medicines))
    print(len(prices))
    
    for medicine in medicines:
        try:
            print(medicine.find('img').get('title').strip())
        except AttributeError as e:
            continue
        
    for price in prices:
        try:
            print(price.get_text())
        except AttributeError as e:
            continue
        
    if len(medicines) != len(prices):
        return
    
    max_item = len(medicines)
    index = 0
    while (index < max_item):
        try:
            print(medicines[index].find('img').get('title').strip())
            
            index += 1

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
    return
    try:
        page = requests.get(site)
        soup = BeautifulSoup(page.content, 'html.parser')
        str_num_itens = re.findall(r'(\d+)', soup.find('div', class_='ToolbarContagem').get_text())
        num_itens = ast.literal_eval(str_num_itens[0])
        num_pages = num_itens / 16
        num_page = 1
        while (num_page < num_pages):
            s = "http://www.drogarianet.com.br/medicamentos.html?p=" + str(num_page)
            recoverMedicine(s)
            num_page += 1
    except AttributeError as e:
        ""
            
recoverMedicineCallFarma()

conn.commit()
conn.close()
print('Dados inseridos com sucesso.')