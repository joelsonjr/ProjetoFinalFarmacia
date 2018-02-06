import re
import ast
import requests
import numpy as np
from bs4 import BeautifulSoup
import sqlite3

def recoverMedicine(site):    
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    page = requests.get(site)
    soup = BeautifulSoup(page.content, 'html.parser')
    medicines = soup.find('div', class_='Produtos').find_all('li', class_="Produto")
    for medicine in medicines:
        try:
            title = medicine.find('div', class_='Nome').get_text().strip()
            price = re.findall(r'(\d+ ?\d+\,?\d*)', medicine.find('div', class_='PrecoAgrupado').find('div', class_='PrecoPor').get_text())
            cursor.execute("""
                           INSERT INTO Medicamentos(id_empresa, nome, preco)
                           VALUES (3,?,?)
                           """, (title, price[0]))
        except AttributeError as e:
            continue        
    conn.commit()
    conn.close()
            

def recoverMedicineDrogariaNet():
    print("INICIO DROGA NET")
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("delete from Medicamentos where id_empresa = 3;")
    conn.commit()
    conn.close()
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
    print("FIM DROGA NET")
            

def selectMedicineDrogariaNet():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("select id_empresa, nome, preco from Medicamentos where id_empresa = 3;")
    conn.close()
    data = []
    for row in cursor:
        data.append(row)
    return data
