##### SPYDER #####

# Abrir o Workbench
# create database sistemaX;

# Abrir o Spyder
# Criar a classe Banco: Criar uma conexão entre o servidor de banco de dados mysql e o python
# para poder utilizar um banco de dados cadastrado e fazer manipulações desse banco de dados
# com a linguagem SQL dentro do código em Python

import pymysql

class Banco:
    
    # Cria uma conexão com o banco de dados e salva na variável conexao
    def __init__(self):
        self.conexao = pymysql.connect(host="localhost", user="root", passwd="", db="sistemaX")
        # self.conexao = pymysql.connect(host="localhost", user="root", passwd="1234", db="sistemaX")
        # db = sistemaX : base de dados que criamos (se não tivermos criado antes no workbench vai dar erro)        
        self.criarTabela()
        
    def criarTabela(self):       
        # Criar um objeto cursos e salvar na variável c
        c = self.conexao.cursor()
        # A partir do cursor c executamos as funções da biblioteca pymysql
        
        # a funcão execute: Executa uma querie (um comando na linguage sql)
        c.execute("""CREATE TABLE if not exists usuario(
                    id INT NOT NULL AUTO_INCREMENT,
                    nome VARCHAR(45) NOT NULL,
                    senha VARCHAR(45) NOT NULL,
                    email VARCHAR(45) NOT NULL,
                    PRIMARY KEY (id))""")
        # Commit: enviar as alterações para o banco de dados            
        self.conexao.commit()
        # Fechar a conexao
        self.conexao.close

# Verificar no workbench se a tabela foi criada.
# Guardem este arquivo pois vamos utilizá-lo na próxima aula de laboratório.    