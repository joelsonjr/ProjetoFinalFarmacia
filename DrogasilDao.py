import ast
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
    '''
    medicines = soup.find_all('div', class_='product-info')
    for medicine in medicines:
        try:
            print(medicine.find('div', class_='product-name').find('a', class_='show-hover').get_text())
        except AttributeError as e:
            continue
    ''' 
    prices = soup.find_all('div', class_='product-price')
    for price in prices:
        try:
            print(price.find('div', class_='price-box').find('p', class_='special-price').find('span', property_='price').get_text())
        except AttributeError as e:
            continue
        
    '''
    medicines = soup.find_all('div', class_='caption text-center')
    for medicine in medicines:
        try:
            print(medicine.p.get_text().strip())
            print(medicine.find_all('div')[2].find('div').find('div', class_='row').find('div').h4.find_all('label')[1].get_text())
#            cursor.execute("""
#                           INSERT INTO Medicamentos(id_empresa, nome, preco, peso, categoria, especial)
#                           VALUES (1,?,?)
#                           """, (title, price[0]))
        except AttributeError as e:
            continue
        '''
def recoverMedicineDrogasil():
    #cursor.execute("delete from Medicamento where id_empresa = 1;")
    site = "http://www.drogasil.com.br/medicamentos.html";
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
            
recoverMedicineDrogasil()

conn.commit()
conn.close()
print('Dados inseridos com sucesso.')