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
    medicines = soup.find_all('div', class_='conj_prod_categorias')    
    for medicine in medicines:
        try:
            title = medicine.find('div', class_='alt_prod_categorias').find('a', class_='lista_prod').get_text()
            price = medicine.find('div', class_='preco_lista_prod').find('div', class_='preco_por').get_text()
            print(title)
            print(price)
#            cursor.execute("""
#                           INSERT INTO Medicamentos(id_empresa, nome, preco, peso, categoria, especial)
#                           VALUES (1,?,?)
#                           """, (title, price[0]))
        except AttributeError as e:
            print(" NAO CONSEGUIU RECUPERAR O ITEM ")
            continue        
            

def recoverMedicineUltraFarma():
    site = "http://www.ultrafarma.com.br/categoria-372/ordem-1/Medicamentos.html";
    recoverMedicine(site)
    try:
        page = requests.get(site)
        soup = BeautifulSoup(page.content, 'html.parser')
        pages = soup.find_all('div', align_="center")#.find('span', class_='txt_cinza')
        for p in pages:
            print(p)
        #num_pages = ast.literal_eval(re.search(r'\d+',pages[0].find('a', class_='last').get('onclick')).group(0))
        #num_page = 0
        #while (num_page < num_pages):
        #    s = "https://www.drogariavenancio.com.br/categoria.asp?idcategoria=1014&nivel=03&categoria=Medicamentos&viewType=M&nrRows=20&idPage=" + str(num_page) + "2&ordem=V"
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
            
recoverMedicineUltraFarma()

conn.commit()
conn.close()
print('Dados inseridos com sucesso.')
