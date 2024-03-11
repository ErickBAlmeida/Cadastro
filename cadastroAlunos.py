# PROJETO DO SEGUNDO PERÍODO DA FACULDADE DE ENG. DE COMPUTAÇÃO

import sqlite3
import tkinter as tk
from tkinter import ttk

janela=tk.Tk()

def criarBD():
    import sqlite3 as conector
    banco=conector.connect('cadastroBD.bd')
    cursor=banco.cursor()
    sql='CREATE TABLE if not exists tabelaAlunos(matricula INTEGER, nome TEXT, curso TEXT, email TEXT)'
    cursor.execute(sql)
    cursor.fetchall()
    banco.commit()#confirmação
    cursor.close()
    banco.close()
criarBD()

def inserirAlunos():
    import sqlite3 as conector
    banco=conector.connect('cadastroBD.bd')#conectar banco
    cursor=banco.cursor()#criar cursor
    matricula=entry_matricula.get()
    nome=entry_nome.get()
    curso=entry_curso.get()
    email=entry_email.get()
    sqlInto="INSERT into tabelaAlunos VALUES("+str(matricula)+",'"+nome+"','"+curso+"','"+email+"')"
    cursor.execute(sqlInto)#executar comando
    banco.commit()#confirmação
    cursor.close()#fechar cursor
    banco.close()#fechar banco
    label_confirmacao=tk.Label(janela,text="Aluno Inserido!!",font=('Arial', 13))
    label_confirmacao.grid(column=2,row=6,padx=10,pady=10,sticky='nswe',columnspan=1)
    

def apagarAlunos():
    import sqlite3 as conector
    banco=conector.connect('cadastroBD.bd')
    cursor=banco.cursor()
    matriculaDEL=entry_infodel.get()
    cursor.execute("DELETE from tabelaAlunos where matricula="+str(matriculaDEL)+"")
    banco.commit()
    cursor.close()
    banco.close()
    label_confirmacaodel=tk.Label(janela,text="Aluno Deletado!",font=('Arial',13))
    label_confirmacaodel.grid(column=2,row=10,padx=10,pady=10,sticky='nswe',columnspan=1)

janela.title("Cadastro de alunos")#título da janela

label_orientacao=tk.Label(janela,text="Adicionar Aluno:", font=('Arial',16))
label_orientacao.grid(column=0,row=0,padx=10,pady=10,sticky='nswe',columnspan=2)

label_matricula=tk.Label(janela,text="Mátricula do Aluno:",font=('Arial',13))
label_matricula.grid(column=0,row=1,padx=10,pady=10,sticky='nswe',columnspan=2)

entry_matricula=tk.Entry()
entry_matricula.grid(column=3,row=1,padx=10,pady=10,sticky='nswe',columnspan=2)

label_nome=tk.Label(janela,text="Nome do Aluno:",font=('Arial',13))
label_nome.grid(column=0,row=2,padx=10,pady=10,sticky='nswe',columnspan=2)

entry_nome=tk.Entry()
entry_nome.grid(column=3,row=2,padx=10,pady=10,sticky='nswe',columnspan=2)

label_curso=tk.Label(janela,text="curso do Aluno:",font=('Arial',13))
label_curso.grid(column=0,row=3,padx=10,pady=10,sticky='nswe',columnspan=2)

entry_curso=tk.Entry()
entry_curso.grid(column=3,row=3,padx=10,pady=10,sticky='nswe',columnspan=4)

label_email=tk.Label(janela, text="E-mail do Aluno",font=('Arial',13))
label_email.grid(column=0,row=4,padx=10,pady=10,sticky='nswe',columnspan=2)

entry_email=tk.Entry()
entry_email.grid(column=3,row=4,padx=10,pady=10,sticky='nswe',columnspan=2)

botao_inserir_aluno=tk.Button(text="Inserir Aluno ao Banco de dados",font=('Arial',12),command=inserirAlunos)
botao_inserir_aluno.grid(column=0,row=5,padx=10,pady=10,sticky='nswe',columnspan=5)

label_deletar_aluno=tk.Label(text="Apagar Aluno:",font=('Arial',16))
label_deletar_aluno.grid(column=0,row=7,padx=10,pady=10,sticky='nswe',columnspan=2)

label_infodel=tk.Label(janela, text="Quem será deletado?",font=('Arial',13))
label_infodel.grid(column=0,row=8,padx=10,pady=10,sticky='nswe',columnspan=2)

entry_infodel=tk.Entry()
entry_infodel.grid(column=3,row=8,padx=10,pady=10,sticky='nswe', columnspan=2)

botaoDEL=tk.Button(janela, text="Deletar Aluno",font=('Arial',12),command=apagarAlunos)
botaoDEL.grid(column=0,row=9,padx=10,pady=10,sticky='nswe',columnspan=5)

janela.mainloop()