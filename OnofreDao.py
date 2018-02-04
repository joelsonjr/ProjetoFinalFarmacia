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
    medicines = soup.find_all('div', class_='product-price')
    for medicine in medicines:
        try:
            title = medicine.a.get('title')
            price = re.findall(r'(\d+\,?\d*)', medicine.a.find('span', class_='regular-price').get_text())
            cursor.execute("""
                           INSERT INTO Medicamentos(id_empresa, nome, preco)
                           VALUES (7,?,?)
                           """, (title, price[0]))            
        except AttributeError as e:
            continue

def recoverMedicineOnofre():
    cursor.execute("delete from Medicamentos where id_empresa = 7;")
    site = "https://www.onofre.com.br/medicamentos/51/01";
    recoverMedicine(site)
            
recoverMedicineOnofre()

conn.commit()
conn.close()
print('Dados inseridos com sucesso.')