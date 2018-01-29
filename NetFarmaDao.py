import re
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
    #<div id="lista-produtos" class="product-list">
    print(soup.find('option', value_='lancamento'))
    #print(soup.find('div', class_='product-list'))
 #   try:        
#        medicines = soup.find('div', id='product-list').find_all('div', class_='product-item ')
#        for medicine in medicines:
#            print(medicine)
#            title = medicine.find('div', class_='Nome').get_text().strip()
#            price = medicine.find('div', class_='PrecoAgrupado').find('div', class_='PrecoPor').get_text()
#            print(title)
#            print(price)        
#            cursor.execute("""
#                           INSERT INTO Medicamentos(id_empresa, nome, preco, peso, categoria, especial)
#                           VALUES (1,?,?)
#                           """, (title, price[0]))
#    except AttributeError as e:
#        print(" NAO CONSEGUIU RECUPERAR O ITEM ")
            

def recoverMedicineNetFarma():
    site = "https://www.netfarma.com.br/categoria/medicamentos";
    recoverMedicine(site)
    #page = requests.get(site)
    #soup = BeautifulSoup(page.content, 'html.parser')
    #try:
    #    itens = soup.find('div', class_="vitrine resultItemsWrapper").script.get_text()
    #    print(itens)
        #for page in pages:
            #p = foodsSite[0] + "?Pagina=" + page.get_text()
            #recoverZonaSulFood(p)
    #except AttributeError as e:
    #    ""
            
recoverMedicineNetFarma()

conn.commit()
conn.close()
print('Dados inseridos com sucesso.')
