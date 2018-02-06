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
    medicines = soup.find_all('div', class_='box-produto box-produtoCustom NoDesc')
    for medicine in medicines:
        try:
            title = medicine.find('div', class_='descricao').get_text().strip()
            price = re.findall(r'(\d+ ?\d+\,?\d*)', medicine.find('div', class_='product-box-control').find('div', class_='boxPreco').find('ul', class_='preco').find('li', class_='precoPor comum-color').get_text().strip())
            if title and price[0]:
                cursor.execute("""
                               INSERT INTO Medicamentos(id_empresa, nome, preco)
                               VALUES (2,?,?)
                               """, (title, price[0]))
        except AttributeError as e:
            continue
        
    conn.commit()
    conn.close()

            

def recoverMedicineDrogariaCristal():
    print("INICIO CRISTAL")
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("delete from Medicamentos where id_empresa = 2;")
    conn.commit()
    conn.close()
    site = "https://www.drogariacristal.com/categoria/1/263/medicamentos";
    recoverMedicine(site)
    try:
        page = requests.get(site)
        soup = BeautifulSoup(page.content, 'html.parser')
        str_num_pages = re.findall(r'(\d+)', soup.find('link', rel='canonical').get('href'))[0]
        num_pages = ast.literal_eval(str_num_pages) / 12
        num_page = 2
        while (num_page < num_pages):
            s = "https://www.drogariacristal.com/categoria/" + str(num_page) + "/posicao/263/medicamentos"
            recoverMedicine(s)
            num_page += 1
    except AttributeError as e:
        ""
    print("FIM CRISTAL")

def selectMedicineDrogariaCristal():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("select id_empresa, nome, preco from Medicamentos where id_empresa = 2;")
    conn.commit()
    conn.close()
    data = []
    for row in cursor:
        data.append(row)
    return data