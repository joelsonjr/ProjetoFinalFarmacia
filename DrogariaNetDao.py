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
    medicines = soup.find('div', class_='Produtos').find_all('li', class_="Produto")
    for medicine in medicines:
        try:
            title = medicine.find('div', class_='Nome').get_text().strip()
            price = medicine.find('div', class_='PrecoAgrupado').find('div', class_='PrecoPor').get_text()
            print(title)
            print(re.findall(r'(\d+\,?\d*)',price)[0])
#            cursor.execute("""
#                           INSERT INTO Medicamentos(id_empresa, nome, preco, peso, categoria, especial)
#                           VALUES (1,?,?)
#                           """, (title, price[0]))
        except AttributeError as e:
            continue        
            

def recoverMedicineDrogariaNet():
    #cursor.execute("delete from Medicamento where id_empresa = 1;")
    site = "http://www.drogarianet.com.br/medicamentos.html";
    recoverMedicine(site)
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
            
recoverMedicineDrogariaNet()

conn.commit()
conn.close()
print('Dados inseridos com sucesso.')

