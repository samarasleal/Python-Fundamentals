##### SPYDER #####
# Aula 09 - Tutorial - Interface Gráfica em Python

# Parte 01 - Criando uma interface gráfica com o Tkinter (Classe Banco e Classe Usuário)
# Na aula anterior... Nós criamos o banco de dados sistemaX no workbench.
# Abrir o Workbench verificar se o sistemaX esta la se não: create database sistemaX;

# Nós abrimos o spyder e criamos a classe Banco para criar uma conexão com o banco de dados
# Peguem o código da aula anterior e copie para essa aula 
# (ou se não tiver copie o código que esta na tela e salve como minhaInterface.py)

import pymysql
from tkinter import *
class Banco:    
    def __init__(self):
        self.conexao = pymysql.connect(host="localhost", user="root", passwd="1234", db="sistemaX")
        self.criarTabela()       
    def criarTabela(self):       
        c = self.conexao.cursor()
        c.execute("""CREATE TABLE if not exists usuario(
                    id INT NOT NULL AUTO_INCREMENT,
                    nome VARCHAR(45) NOT NULL,
                    senha VARCHAR(45) NOT NULL,
                    email VARCHAR(45) NOT NULL,
                    PRIMARY KEY (id))""")           
        self.conexao.commit()
        self.conexao.close

# testar CONSOLE
# banco = Banco()

class Usuario:
    def __init__(self, id, nome, senha, email):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.email = email
    def inserirUsuario(self):  
        banco = Banco()
        c = banco.conexao.cursor()
        c.execute("insert into usuario (nome, senha, email) values ('" + self.nome + "', '" + self.senha + "', '" + self.email + "')")        
        banco.conexao.commit()
        c.close()
    def atualizarUsuario(self):
        banco = Banco()
        c = banco.conexao.cursor()
        self.id = str(self.id)
        c.execute("update usuario set nome = '" + self.nome + "', email = '" + self.email + "', senha = '" + self.senha + "' where id = " + self.id + " ")
        banco.conexao.commit()
        c.close()    
    # testar
    # samara = Usuario(1,'Samara','1234','samarateste')
    # samara.inserirUsuario()    
    # verificar no workbench: 
    # use sistemasX;
    # verificar o id que foi criado no workbench: select * from usuario;
    
    # samara = Usuario(id do WORKBENCH,'Samara','4321','samarateste')
    # samara.atualizarUsuario()
    # verificar alteração no workbench: select * from usuario;
 




   
    
# PARTE 02 - Continuação da classe Usuario: criar métodos para selecionar(buscar) e deletar
    def selecionarUsuario(self, id):
        banco = Banco()
        c = banco.conexao.cursor()
        id = str(id)
        c.execute("select * from usuario where id = " + id + "  ")
        for linha in c:
            self.id = linha[0]
            self.nome = linha[1]
            self.senha = linha[2]
            self.email = linha[3]           
        c.close()
        
    def deletarUsuario(self):
        banco = Banco()
        c = banco.conexao.cursor()
        self.id = str(self.id)
        c.execute("delete from usuario where id = " + self.id + " ")
        banco.conexao.commit()
        c.close() 
    # testar
    # verificar o que esta salvo banco: select * from usuario;
    # samara.selecionarUsuario(id do WORKBENCH)
        
    # samara = Usuario(id do WORKBENCH,'Samara','4321','samarateste')
    # samara.deletarUsuario()
    # verificar deleção no workbench: select * from usuario;
        

# Parte 03 - Criando uma interface gráfica com o Tkinter (Classe Aplicação)
# colocar: from tkinter import *

class Aplicacao:
    def __init__(self, master=None):
        self.cont1 = Frame(master, pady =10)
        self.cont1.pack()
        self.cont2 = Frame(master, padx =20, pady=5)
        self.cont2.pack()
        self.cont3 = Frame(master, padx =20, pady=5)
        self.cont3.pack()
        self.cont4 = Frame(master, padx =20, pady=5)
        self.cont4.pack()
        self.cont5 = Frame(master, padx =20, pady=5)
        self.cont5.pack()
        self.cont6 = Frame(master, padx =20, pady=10)
        self.cont6.pack()
        self.cont7 = Frame(master, pady =15)
        self.cont7.pack()
    
        self.titulo = Label(self.cont1, text="Dados :")
        self.titulo.pack ()
        
        self.lblid = Label(self.cont2, text="Id:")
        self.lblid.pack(side=LEFT)   
        self.txtid = Entry(self.cont2)
        self.txtid.pack(side=LEFT)   
        self.btnBuscar = Button(self.cont2, text="Buscar")
        self.btnBuscar["command"] = self.buscarUsuario
        self.btnBuscar.pack(side=RIGHT)
   
        self.lblnome = Label(self.cont3, text="Nome:")
        self.lblnome.pack(side=LEFT)   
        self.txtnome = Entry(self.cont3)
        self.txtnome.pack(side=LEFT)
   
        self.lblemail= Label(self.cont4, text="E-mail:")
        self.lblemail.pack(side=LEFT)  
        self.txtemail = Entry(self.cont4)
        self.txtemail.pack(side=LEFT)

        self.lblsenha= Label(self.cont5, text="Senha:")
        self.lblsenha.pack(side=LEFT)   
        self.txtsenha = Entry(self.cont5, show = "*")
        self.txtsenha.pack(side=LEFT)
        
        self.bntIns = Button(self.cont6, text="Inserir")
        self.bntIns["command"] = self.inserirUsuario
        self.bntIns.pack (side=LEFT)
   
        self.bntAlt = Button(self.cont6, text="Alterar")
        self.bntAlt["command"] = self.alterarUsuario
        self.bntAlt.pack (side=LEFT)
   
        self.bntEx = Button(self.cont6, text="Excluir")
        self.bntEx["command"] = self.excluirUsuario
        self.bntEx.pack(side=LEFT)
   
        self.lblmsg = Label(self.cont7, text="")
        self.lblmsg.pack()
    def inserirUsuario(self):
        id = self.txtid.get()
        nome = self.txtnome.get()
        senha = self.txtsenha.get()
        email = self.txtemail.get()
        user = Usuario(id, nome, senha, email)   
   
        user.inserirUsuario()
        self.lblmsg["text"] = "Usuário inserido."
    
    def alterarUsuario(self):
        id = self.txtid.get()
        nome = self.txtnome.get()
        senha = self.txtsenha.get()
        email = self.txtemail.get()
        user = Usuario(id, nome, senha, email)   
   
        user.atualizarUsuario()
        self.lblmsg["text"] = "Usuário Atualizado."

    def excluirUsuario(self):
        id = self.txtid.get()
        nome = self.txtnome.get()
        senha = self.txtsenha.get()
        email = self.txtemail.get()
        user = Usuario(id, nome, senha, email)  
        
        user.deletarUsuario()
        self.lblmsg["text"] = "Usuário Excluído."  

    def buscarUsuario(self):
        id = self.txtid.get()
        nome = self.txtnome.get()
        senha = self.txtsenha.get()
        email = self.txtemail.get()
        user = Usuario(id, nome, senha, email)
   
        self.lblmsg["text"] = user.selecionarUsuario(id)
        
        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)
        
        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, user.email)
        
        self.txtsenha.delete(0, END)
        self.txtsenha.insert(INSERT,user.senha)

raiz = Tk()
Aplicacao(raiz)
raiz.mainloop()   
# Não preciso informar o id na hora de inserir
# Informar id correto na hora de alterar / excluir e buscar
  