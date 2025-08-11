import tkinter as tk
# from tkinter import ttk

from index import bd

bd = bd()

janela=tk.Tk()
janela.title("Cadastro de alunos")#título da janela

label_orientacao=tk.Label(janela,text="Adicionar Aluno:", font=('Arial',16))
label_orientacao.grid(column=0,row=0,padx=10,pady=10,sticky='nswe',columnspan=2)

label_matricula=tk.Label(janela,text="Mátricula do Aluno:",font=('Arial',13))
label_matricula.grid(column=0,row=1,padx=10,pady=10,sticky='nswe',columnspan=2)

entry_matricula=tk.Entry(janela)
entry_matricula.grid(column=3,row=1,padx=10,pady=10,sticky='nswe',columnspan=2)

label_nome=tk.Label(janela,text="Nome do Aluno:",font=('Arial',13))
label_nome.grid(column=0,row=2,padx=10,pady=10,sticky='nswe',columnspan=2)

entry_nome=tk.Entry(janela)
entry_nome.grid(column=3,row=2,padx=10,pady=10,sticky='nswe',columnspan=2)

label_curso=tk.Label(janela,text="curso do Aluno:",font=('Arial',13))
label_curso.grid(column=0,row=3,padx=10,pady=10,sticky='nswe',columnspan=2)

entry_curso=tk.Entry(janela)
entry_curso.grid(column=3,row=3,padx=10,pady=10,sticky='nswe',columnspan=4)

label_email=tk.Label(janela, text="E-mail do Aluno",font=('Arial',13))
label_email.grid(column=0,row=4,padx=10,pady=10,sticky='nswe',columnspan=2)

entry_email=tk.Entry(janela)
entry_email.grid(column=3,row=4,padx=10,pady=10,sticky='nswe',columnspan=2)

botao_inserir_aluno=tk.Button(text="Inserir Aluno ao Banco de dados",font=('Arial',12), command = lambda: bd.inserirAlunos(entry_matricula.get(), entry_nome.get(), entry_curso.get(), entry_email.get()))
botao_inserir_aluno.grid(column=0,row=5,padx=10,pady=10,sticky='nswe',columnspan=5)

label_deletar_aluno=tk.Label(text="Apagar Aluno:",font=('Arial',16))
label_deletar_aluno.grid(column=0,row=7,padx=10,pady=10,sticky='nswe',columnspan=2)

label_infodel=tk.Label(janela, text="Quem será deletado?",font=('Arial',13))
label_infodel.grid(column=0,row=8,padx=10,pady=10,sticky='nswe',columnspan=2)

entry_infodel=tk.Entry(janela)
entry_infodel.grid(column=3,row=8,padx=10,pady=10,sticky='nswe', columnspan=2)

botaoDEL=tk.Button(janela, text="Deletar Aluno",font=('Arial',12),  command = lambda: bd.apagarAlunos(entry_infodel.get()))
botaoDEL.grid(column=0,row=9,padx=10,pady=10,sticky='nswe',columnspan=5)

janela.mainloop()