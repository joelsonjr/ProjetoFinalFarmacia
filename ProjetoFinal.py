import sqlite3
import numpy as np
import matplotlib.pyplot as plt
from platypus import NSGAII, Problem, Real, Integer
# plot the results using matplotlib
import matplotlib.pyplot as plt

#import DaoManager
#DaoManager.recoverData()

products = [("dorflex","10 comprimidos"),
            ("cimegripe","20 c"),
            ("Finasterida","5mg"),
            ("Triazol","4"),
            ("Stub","30"),
            ("damater", ""),
            ("Neosaldina","30"),
            ("Dexilant 60mg","60"),
            ("TEBONIN","40"),
            ("Benegrip","20")]

def schaffer(id_company, conn):
    cursor = conn.cursor()
    list_product = []
    lin = 0
    for product in products:
        p = "%" + product[0] + "%" + product[1] + "%"
        for row in  cursor.execute("""
                       select nome, min(preco) from Medicamentos where id_empresa = ? and nome like ?;
                       """, (id_company, p)):
            if row[0]:
                list_product.append(row)
    amount = len(list_product)
    total_price = 10
    return [amount, total_price]


def get_companies(conn):
    cursor = conn.cursor()
    c = []
    for row in cursor.execute("select * from empresas;"):
        c.append(row)
    return c


def project():
    conn = sqlite3.connect('products.db')
    companies = get_companies(conn)
    
    problem = Problem(len(companies),2)
    #problem.types[:] = [Integer(1, nlojas) for _ range(nprodutos)]    
    
    problem.function = schaffer

    algorithm = NSGAII(problem)
    algorithm.run(10000)    
    
    company = 0
    while (company < len(companies)):
        result = schaffer(companies[company][0], conn)
        print(result)
        company += 1
    
    conn.close()
    
    plt.scatter([s.objectives[0] for s in algorithm.result],
            [s.objectives[1] for s in algorithm.result])
    plt.xlim([0, 1.1])
    plt.ylim([0, 1.1])
    plt.xlabel("Preço")
    plt.ylabel("Distancia")
    plt.show()












    
project()
