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
    medicines = soup.find('div', class_='category-products').find_all('div', class_='product-info')
    for medicine in medicines:
        try:
            title = medicine.find('div', class_='product-name').find('a', class_='show-hover').get_text().strip()
            price = re.findall(r'(\d+\,?\d*)',medicine.find('div', class_='product-price').find('p', class_='special-price').find('span', class_='price').get_text().strip())
            cursor.execute("""
                           INSERT INTO Medicamentos(id_empresa, nome, preco)
                           VALUES (6,?,?)
                           """, (title, price[0]))
        except AttributeError as e:
            continue
    conn.commit()
    conn.close()
            

def recoverMedicineDrogasRaia():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("delete from Medicamentos where id_empresa = 6;")
    conn.commit()
    conn.close()
    site = "http://www.drogaraia.com.br/saude/medicamentos.html";
    recoverMedicine(site)    
    try:
        page = requests.get(site)
        soup = BeautifulSoup(page.content, 'html.parser')
        str_num_itens = re.findall(r'(\d+)', soup.find('div', class_='toolbar').find('div', class_='limit no-padding').find('div', class_='col-1').find('div', class_='pager inline').find('div', class_='count-containe inline').find('p', class_='amount inline amount--has-pages').get_text())
        num_itens = ast.literal_eval(str_num_itens[0])
        num_pages = num_itens / 24
        num_page = 1
        while (num_page < num_pages):            
            s = "http://www.drogaraia.com.br/saude/medicamentos.html?p=" + str(num_page)
            recoverMedicine(s)
            num_page += 1
    except AttributeError as e:
        ""
        
def selectMedicineDrogasRaia():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("select id_empresa, nome, preco from Medicamentos where id_empresa = 6;")
    conn.close()
    data = []
    for row in cursor:
        data.append(row)
    return data
