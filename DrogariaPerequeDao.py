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
    medicines = soup.find_all('div', class_='caption text-center')
    for medicine in medicines:
        try:
            title = medicine.p.get_text().strip()
            price = re.findall(r'(\d+ ?\d+\,?\d*)', medicine.find_all('div')[2].find('div').find('div', class_='row').find('div').h4.find_all('label')[1].get_text())
            cursor.execute("""
                           INSERT INTO Medicamentos(id_empresa, nome, preco)
                           VALUES (4,?,?)
                           """, (title, price[0]))
        except AttributeError as e:
            continue
        
    conn.commit()
    conn.close()

def recoverMedicineDrogariaPereque():
    print("INICIO PERTEQUE")
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("delete from Medicamentos where id_empresa = 4;")
    conn.commit()
    conn.close()
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
    print("FIM PEREQUE")
            
def selectMedicineDrogariaPereque():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("select id_empresa, nome, preco from Medicamentos where id_empresa = 4;")
    conn.close()
    data = []
    for row in cursor:
        data.append(row)
    return data

