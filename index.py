import sqlite3
import tkinter as tk


class bd:

    def __init__(self):
        self.banco= sqlite3.connect('cadastroBD.bd')
        self.cursor=self.banco.cursor()

    def criarBD(self):
        sql='''CREATE TABLE IF NOT EXISTS tabelaAlunos(
                    matricula INTEGER PRIMARY KEY,
                    nome TEXT,
                    curso TEXT,
                    email TEXT
            )'''

        self.cursor.execute(sql)
        self.banco.commit()

    def inserirAlunos(self, matricula, nome, curso, email):
        sqlInto="INSERT INTO tabelaAlunos (matricula, nome, curso, email) VALUES (?, ?, ?, ?)"
        self.cursor.execute(sqlInto, (matricula, nome, curso, email))
        self.banco.commit()

    def apagarAlunos(self, infodel):
        self.cursor.execute("DELETE from tabelaAlunos where matricula="+str(infodel)+"")
        self.cursor.execute("DELETE FROM tabelaAlunos WHERE matricula = ?", (infodel,))
        self.banco.commit()

    def __del__(self):
        self.cursor.close()
        self.banco.close()