import sqlite3
import os

"""
Módulo responsável por criar o banco de dados na primeira vez.
"""

dir_db = './Banco de dados'
if not os.path.exists(dir_db):
    os.mkdir(dir_db)
    con = sqlite3.connect(dir_db + '/VGymSystem.db')
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE Usuario(
        username TEXT NOT NULL PRIMARY KEY,
        senha TEXT NOT NULL);
        """
    )
    cursor.execute(
        """
        CREATE TABLE Responsavel(
        matricula_responsavel INTEGER NOT NULL PRIMARY KEY,
        nome TEXT NOT NULL,
        data_nascimento TEXT NOT NULL,
        cpf TEXT NOT NULL UNIQUE,
        celular TEXT NOT NULL,
        whatsapp INTEGER NOT NULL,
        bairro TEXT NOT NULL,
        cep TEXT NOT NULL,
        cidade TEXT NOT NULL,
        email TEXT NOT NULL,
        foto TEXT);
        """
    )
    cursor.execute(
        """
        CREATE TABLE Aluno(
        matricula_aluno INTEGER NOT NULL PRIMARY KEY,
        nome_aluno TEXT NOT NULL,
        data_nascimento TEXT NOT NULL,
        cpf TEXT NOT NULL UNIQUE,
        celular TEXT NOT NULL,
        whatsapp INTEGER NOT NULL,
        bairro TEXT NOT NULL,
        cep TEXT NOT NULL,
        cidade TEXT NOT NULL,
        email TEXT NOT NULL,
        data_pagamento INTEGER NOT NULL,
        valor_pagamento INTEGER NOT NULL,
        foto TEXT NOT NULL,
        data_entrada TEXT NOT NULL,
        matricula_responsavel INTEGER,
        FOREIGN KEY (matricula_responsavel)
        REFERENCES Responsavel (matricula_responsavel)
        ON DELETE CASCADE);
        """
    )
    cursor.execute(
        """
        CREATE TABLE Professor(
        matricula_professor INTEGER NOT NULL PRIMARY KEY,
        nome TEXT NOT NULL,
        data_nascimento TEXT NOT NULL,
        cpf TEXT NOT NULL UNIQUE,
        celular TEXT NOT NULL,
        whatsapp INTEGER NOT NULL,
        email TEXT NOT NULL,
        cidade TEXT NOT NULL,
        bairro TEXT NOT NULL,
        cep TEXT NOT NULL,
        formacao TEXT NOT NULL,
        salario INTEGER NOT NULL,
        dia_pagamento INTEGER NOT NULL,
        foto TEXT NOT NULL,
        data_entrada TEXT NOT NULL);
        """
    )
    con.commit()
    cursor.execute("""INSERT INTO usuario VALUES ('admin', 'admin');""")
    con.commit()
