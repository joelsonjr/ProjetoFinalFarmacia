import sqlite3

conn = sqlite3.connect('products.db')

cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Empresas (
        id_empresa INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        site TEXT NOT NULL
        );
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Localizacao_Empresa (
        id_localizacao INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        id_empresa INTEGER NOT NULL,
        endereco TEXT NOT NULL,
        numero INTEGER NOT NULL,
        cep VARCHAR(9) NOT NULL,
        bairro TEXT NOT NULL,
        cidade TEXT NOT NULL,
        telefone VARCHAR(9) NOT NULL,
        FOREIGN KEY(id_empresa) REFERENCES Empresa(id_empresa)
        );
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Medicamentos (
        id_produto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        id_empresa INTEGER NOT NULL,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        quantidade REAL,
        FOREIGN KEY(id_empresa) REFERENCES Empresa(id_empresa)
        );
""")

cursor.execute("insert into Empresas(nome, site) values ('Call Farma', 'https://www.callfarma.com.br/departamento/medicamentos')")
cursor.execute("insert into Empresas(nome, site) values ('Drogaria Cristal', 'https://www.drogariacristal.com/categoria/1/263/medicamentos')")
cursor.execute("insert into Empresas(nome, site) values ('Drogaria Net', 'http://www.drogarianet.com.br/')")
cursor.execute("insert into Empresas(nome, site) values ('Drogaria Pereque', 'https://www.drogariapereque.com.br/medicamentos')")
cursor.execute("insert into Empresas(nome, site) values ('Drogaria Sao Paulo', 'https://www.drogariasaopaulo.com.br/medicamentos?PS=20&O=OrderByTopSaleDESC')")
cursor.execute("insert into Empresas(nome, site) values ('Drogas Raia', 'http://www.drogaraia.com.br/')")
cursor.execute("insert into Empresas(nome, site) values ('Onofre', 'https://www.onofre.com.br/medicamentos/51/01')")
cursor.execute("insert into Empresas(nome, site) values ('Drogarias Pacheco', 'https://www.drogariaspacheco.com.br/')")
cursor.execute("insert into Empresas(nome, site) values ('Pague Menos', 'https://www.paguemenos.com.br/')")
cursor.execute("insert into Empresas(nome, site) values ('Ultra Farma', 'http://www.ultrafarma.com.br/')")
cursor.execute("insert into Empresas(nome, site) values ('Drogaria Venancio', 'https://www.drogariavenancio.com.br/home')")

conn.commit()

conn.close()

print('Dados inseridos com sucesso.')