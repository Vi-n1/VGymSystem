import sqlite3
import os

"""
Módulo responsável por criar o banco de dados na primeira vez.
"""


def cria_db():
    dir_db = './Banco de dados'
    if not os.path.exists(dir_db):
        os.mkdir(dir_db)
        con = sqlite3.connect(dir_db + '/SystemFit.db')
        cursor = con.cursor()
        cursor.execute(
            """
        CREATE TABLE usuario(
            username TEXT NOT NULL PRIMARY KEY,
            senha TEXT NOT NULL
        );
        """
        )
        con.commit()
        cursor.execute("""INSERT INTO usuario VALUES ('admin', 'admin');""")
        con.commit()
