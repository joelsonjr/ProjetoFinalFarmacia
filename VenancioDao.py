import re
import requests
import numpy as np
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('products.db')

cursor = conn.cursor()

def recoverMedicine(site):
    #cursor.execute("delete from Medicamento where id_empresa = 1;")
    page = requests.get(site)
    soup = BeautifulSoup(page.content, 'html.parser')
    medicines = soup.find_all('li', class_="nome")
    for medicine in medicines:
        print(medicine.get_text().strip())
        
    prices = soup.find_all('li', class_="precoPor")
    for price in prices:
        print(price.get_text().strip())
#        try:
#            title = medicine.find('p', class_='price').a.get('title')
#            price = medicine.find('p', class_='price').a.find('ins', class_='price-new').get_text()
#            print(title)
#            print(price)
#            cursor.execute("""
#                           INSERT INTO Medicamentos(id_empresa, nome, preco, peso, categoria, especial)
#                           VALUES (1,?,?)
#                           """, (title, price[0]))
 #       except AttributeError as e:
#            print(" NAO CONSEGUIU RECUPERAR O ITEM ")
#            continue        
            

#Recuperando itens de açougue do supermercado Zona Sul
def recoverMedicineVenancio():
    site = "https://www.drogariavenancio.com.br/departamento/1014/03/medicamentos";
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
            
recoverMedicineVenancio()

conn.commit()
conn.close()
print('Dados inseridos com sucesso.')