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
    medicines = soup.find_all('a', class_='productPrateleira transition_all Medicamentos')
    for medicine in medicines:
        try:
            title = medicine.find('h3').get_text()
            price = re.findall(r'(\d+\,?\d*)', medicine.find('span', class_='bestPrice transition_all').find('span', class_='the-price').get_text())
            cursor.execute("""
                           INSERT INTO Medicamentos(id_empresa, nome, preco)
                           VALUES (5,?,?)
                           """, (title, price[0]))
        except AttributeError as e:
            continue


def recoverMedicineDrogariaSaoPaulo():
    cursor.execute("delete from Medicamentos where id_empresa = 5;")
    site = "https://www.drogariasaopaulo.com.br/medicamentos?PS=20&O=OrderByTopSaleDESC";
    recoverMedicine(site)
    try:
        page = requests.get(site)
        soup = BeautifulSoup(page.content, 'html.parser')        
        str_num_itens = soup.find('div', class_='mainPrateleira prateleiraDepartamento flt_right').find('div', class_='main').find('p', class_='searchResultsTime').find('span', class_='resultado-busca-numero').find('span', class_='value').get_text()
        num_pages = ast.literal_eval(str_num_itens) / 20
        num_page = 2
        while (num_page < num_pages):            
            s = "https://www.drogariasaopaulo.com.br/medicamentos?PS=20&O=OrderByTopSaleDESC#" + str(num_page)
            recoverMedicine(s)
            num_page += 1
    except AttributeError as e:
        ""
            

def selectMedicineSaoPaulo():
    cursor.execute("select id_empresa, nome, preco from Medicamentos where id_empresa = 5;")
    data = []
    for row in cursor:
        data.append(row)
    return data

recoverMedicineDrogariaSaoPaulo()

conn.commit()
conn.close()
print('Dados inseridos com sucesso.')