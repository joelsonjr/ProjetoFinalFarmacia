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


cursor.execute("insert into Empresas(nome, site) values ('Drogaria Net', 'http://www.drogarianet.com.br/')")
cursor.execute("insert into Empresas(nome, site) values ('Drogas Raia', 'http://www.drogaraia.com.br/')")
cursor.execute("insert into Empresas(nome, site) values ('Drogarias Pacheco', 'https://www.drogariaspacheco.com.br/')")
cursor.execute("insert into Empresas(nome, site) values ('Pague Menos', 'https://www.paguemenos.com.br/')")
cursor.execute("insert into Empresas(nome, site) values ('Ultra Farma', 'http://www.ultrafarma.com.br/')")
cursor.execute("insert into Empresas(nome, site) values ('Drogaria Venancio', 'https://www.drogariavenancio.com.br/home')")

conn.commit()

conn.close()

print('Dados inseridos com sucesso.')