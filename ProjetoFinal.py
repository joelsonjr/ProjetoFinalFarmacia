import sqlite3
#import DaoManager

#DaoManager.recoverData()


#'%dorflex%10 comprimidos' (1,2,3,4,5,7,8,10)
#'%doril %6%' (2,3,4)
#'%cimegripe%20 c%' (1,2,3,4,10)
#'%Finasterida%5mg%'(3,4,6, 10)
#'%Triazol%4%' (3,10,11)
#'%Stub%30%' (1,2,10,11)
#'%damater%' (3,4,6,9)
#'%Neosaldina%30%' (1,2,3,9,10)
#'%Dexilant 60mg%60%' (5,8,9)
#'%TEBONIN%40%' (6,10)
#'%Benegrip%20%' (2,3,10)

#example
#http://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
#select id_empresa, nome, min(preco) from medicamentos
#where nome like '%dorflex%10%comprimidos'
#and id_empresa = 8

products = [()]

def get_companies(conn):
    cursor = conn.cursor()
    c = []
    for row in cursor.execute("select * from empresas;"):
        c.append(row)
    return c
    
def medicines(id_company):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("select id_empresa, nome, preco from Medicamentos where id_empresa = 3;")
    conn.close()
    data = []
    for row in cursor:
        data.append(row)
    return data


def project():
    conn = sqlite3.connect('products.db')
    companies = get_companies(conn)
    company = 0
    while (company < companies.count):
        print(companies[company][0])
        company += 1
    
    conn.close()
    
project()
