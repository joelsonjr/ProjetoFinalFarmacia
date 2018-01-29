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
    medicines = soup.find_all('a', class_='productPrateleira transition_all')
    for medicine in medicines:
        try:
            title = medicine.find('h3').get_text()
            price = medicine.find('span', class_='bestPrice transition_all').find('span', class_='the-price').get_text()
            print(title)
            print(price)
#            cursor.execute("""
#                           INSERT INTO Medicamentos(id_empresa, nome, preco, peso, categoria, especial)
#                           VALUES (1,?,?)
#                           """, (title, price[0]))
        except AttributeError as e:
            print(" NAO CONSEGUIU RECUPERAR O ITEM ")
            continue        
            

def recoverMedicinePacheco():
    site = "https://www.drogariaspacheco.com.br/medicamentos/";
    recoverMedicine(site)
    
    #function to get num page
            
recoverMedicinePacheco()

conn.commit()
conn.close()
print('Dados inseridos com sucesso.')

