import ast
import re
import requests
import numpy as np
from bs4 import BeautifulSoup
import sqlite3

def recoverMedicine(site):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    page = requests.get(site)
    soup = BeautifulSoup(page.content, 'html.parser')
    medicines = soup.find_all('div', class_='conj_prod_categorias')    
    for medicine in medicines:
        try:
            title = medicine.find('div', class_='alt_prod_categorias').find('a', class_='lista_prod').get_text()
            price = re.findall(r'(\d+ ?\d+\,?\d*)',medicine.find('div', class_='preco_lista_prod').find('div', class_='preco_por').get_text())
            print(title)
            cursor.execute("""
                           INSERT INTO Medicamentos(id_empresa, nome, preco)
                           VALUES (10,?,?)
                           """, (title, price[0]))
        except AttributeError as e:
            continue
    conn.commit()
    conn.close()
            

def recoverMedicineUltraFarma():
    print("INICIO ULTRA FARMA")
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("delete from Medicamentos where id_empresa = 10;")
    conn.commit()
    conn.close()
    site = "http://www.ultrafarma.com.br/categoria-372/ordem-1/Medicamentos.html";
    recoverMedicine(site)    
    try:
        page = requests.get(site)
        soup = BeautifulSoup(page.content, 'html.parser')        
        num_pages = 0
        for item in soup.find_all('span', class_='txt_cinza'):            
            if item.get_text():
                num = re.findall(r'(\d+)', item.get_text())[0]
                num_pages = ast.literal_eval(num)
        num_page = 1
        while (num_page < num_pages):            
            s = "http://www.ultrafarma.com.br/categoria-372/ordem-1/pagina-" + str(num_page) + "/Medicamentos.html"
            recoverMedicine(s)
            num_page += 1
        
    except AttributeError as e:
        ""
    print("FIM ULTRA FARMA")
            
def selectMedicineUltraFarma():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("select id_empresa, nome, preco from Medicamentos where id_empresa = 10;")
    conn.close()
    data = []
    for row in cursor:
        data.append(row)
    return data
