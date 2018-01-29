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
    medicines = soup.find('div', class_='Produtos').find_all('li', class_="Produto")
    for medicine in medicines:
        try:
            title = medicine.find('div', class_='Nome').get_text().strip()
            price = medicine.find('div', class_='PrecoAgrupado').find('div', class_='PrecoPor').get_text()
            print(title)
            print(price)        
#            cursor.execute("""
#                           INSERT INTO Medicamentos(id_empresa, nome, preco, peso, categoria, especial)
#                           VALUES (1,?,?)
#                           """, (title, price[0]))
        except AttributeError as e:
            print(" NAO CONSEGUIU RECUPERAR O ITEM ")
            continue        
            

def recoverMedicineDrogariaNet():
    site = "http://www.drogarianet.com.br/medicamentos.html";
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
            
recoverMedicineDrogariaNet()

conn.commit()
conn.close()
print('Dados inseridos com sucesso.')

