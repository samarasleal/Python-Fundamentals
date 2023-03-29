# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 22:39:09 2016

@author: samara
"""
# Aula 06 – Introdução a Orientação a Objetos

#	Parte 01 - Classes e Objetos
# Orientação a Objetos: Conjunto de objetos que trabalham juntos, interagindo para realizar uma tarefa
# Objetos: Elementos do mundo real (estado e comportamento)
# Classes: Conjunto de objetos que possuem atributos e métodos em comum.
# A Classe serve com modelo para criar objetos.

class Pessoa:
    # Método construtor da classe
    def __init__(self, nome, idade):
        # Self: primeiro argumento dos métodos e serve para fazer referência a própria instância que o método se aplica
        # Mesmo se não informá-lo, ele esta implícito.
        self.nome = nome
        self.idade = idade
    def obterIdade(self):
        return self.idade
    def faixaEtaria(self):
        if (self.idade < 12):
            print('Criança')
        elif (12 <= self.idade <= 17):
            print('Adolescente')
        else:
            print('Adulto')

# Informações sobre a classe: dir(Pessoa)

# Criando objetos
Laura = Pessoa('Laura',20)
Laura.idade = 21
Laura.obterIdade()
Laura.faixaEtaria()

# Usando listas de objetos
listaPessoas = [Laura]
listaPessoas.append(Fernando)
listaPessoas[0].idade = 34
Laura.idade
print(listaPessoas)
print(listaPessoas[0].nome)

# Mostrar erros
Pedro = Pessoa('Pedro','Pedro', 12)
Fernando.obterIdade(34)

#	Parte 02 - Princípios da Orientação a Objetos
# Encapsulamento: Proteger a classe de acessos indevidos. Esconder detalhes internos
# Copiar a classe Pessoa da PARTE 01  ->  Colocar '__' antes dos atributos (PRIVADOS)
class Pessoa:
    # Método construtor da classe
    def __init__(self, nome, idade):
        # Self: primeiro argumento dos métodos e serve para fazer referência a própria instância que o método se aplica
        # Mesmo se não informá-lo, ele esta implícito.
        self.__nome = nome
        self.__idade = idade
    def obterIdade(self):
        return self.__idade
    def faixaEtaria(self):
        if (self.__idade < 12):
            print('Criança')
        elif (12 <= self.__idade <= 17):
            print('Adolescente')
        else:
            print('Adulto')

    # CONSOLE: Não é possível alterar os valores dos atributos(PRIVADOS)
    Laura = Pessoa('Laura',20)
    Laura.__idade = 3
    Laura.idade = 3
    Laura.obterIdade()          

    # Para isso usar métodos GET e SET
    def getIdade(self):
        return self.__idade
    def getNome(self):
        return self.__nome
        
    def setIdade(self, idade):
        self.__idade = idade
    def setNome(self, nome):
        self.__nome = nome

    # CONSOLE
    Laura = Pessoa('Laura',20)
    Laura.setIdade(17)
    Laura.getIdade()   
    
    # Função property
    idade = property(fget=getIdade, fset=setIdade)
    nome = property(fget=getNome, fset=setNome)
    
    #CONSOLE
    Laura = Pessoa('Laura',20)
    Laura.idade = 8
    Laura.idade   
#	Parte 03 - Princípios da Orientação a Objetos
# Processo em que uma classe herda atributos e métodos da outra classe. 
# A partir da herança, os objetos podem compartilhar métodos e atributos;


# Copiar a classe Pessoa da PARTE 02
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
    def faixaEtaria(self):
        if (self.__idade < 12):
            print('Criança')
        elif (12 <= self.__idade <= 17):
            print('Adolescente')
        else:
            print('Adulto')
    
    def getIdade(self):
        return self.__idade
    def getNome(self):
        return self.__nome
        
    def setIdade(self, idade):
        self.__idade = idade
    def setNome(self, nome):
        self.__nome = nome
    
    idade = property(fget=getIdade, fset=setIdade)
    nome = property(fget=getNome, fset=setNome)
        
# Criar classe PessoaFisica que herda de Pessoa            
class PessoaFisica(Pessoa):
    def __init__(self, CPF, nome, idade):
        Pessoa.__init__(self, nome, idade)
        self.CPF = CPF

# Criar classe PessoaJuridica que herda de Pessoa
class PessoaJuridica(Pessoa):
    def __init__(self, CNPJ, nome, idade):
        Pessoa.__init__(self, nome, idade)
        self.CNPJ = CNPJ

# CONSOLE
Fabio = PessoaFisica(31554678, 'Fabio',32)
Fabio.idade = 36
Fabio.getIdade()