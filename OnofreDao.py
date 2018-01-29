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
            price = medicine.a.find('span', class_='regular-price').get_text()
            print(title)
            print(price)
        except AttributeError as e:
            print(" NAO CONSEGUIU RECUPERAR O ITEM ")
            continue

def recoverMedicineOnofre():
    site = "https://www.onofre.com.br/medicamentos/51/01";
    #recoverMedicine(site)
    try:
        page = requests.get(site)
        soup = BeautifulSoup(page.content, 'html.parser')
        str_num_itens = re.findall(r'(\d+)', soup.find('div', class_="item pages last").get_text())
        print(str_num_itens)
        num_itens = ast.literal_eval(str_num_itens[2])
        #print(num_itens)
        #num_pages = num_itens / 15
        #print(num_pages)
        #num_page = 1
        #while (num_page < num_pages):            
        #    s = "http://www.drogaraia.com.br/saude/medicamentos.html?p=" + str(num_page)
        #    recoverMedicine(s)
        #    num_page += 1
    except AttributeError as e:
        ""
    
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
            
recoverMedicineOnofre()

conn.commit()
conn.close()
print('Dados inseridos com sucesso.')