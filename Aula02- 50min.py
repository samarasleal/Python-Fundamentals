# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 10:44:22 2016

@author: samara
"""

# Aula 02 - Tutorial - Estrutura do programa em Python



#	Parte 01 - Criando Variáveis e Constantes
# Criação de variáveis e tipos

# Programa que cadastra funcionários

DESCONTOS = 100.00 # constante (Python não tem constantes)
GRATIFICACAO = 50.00      # bônus

idade = 14

# Saber tipo da variável
type(idade)

nome = input('Digite seu nome: ') # string
print('Seu nome é %s'%(nome))
type(nome)                       

email = input('Digite seu email: ')
print(email)

salario = input('Digite seu salário: ')
print(salario)
type(salario)   

salarioNovo = salario + GRATIFICACAO - DESCONTOS

# Tipo string não possibilita a realização de cálculos
# Converter salário para real
salario = float(salario)  
type(salario)

salarioNovo = salario + GRATIFICACAO - DESCONTOS

print("Seu salario atualizado é %.f" %(salarioNovo))


 








#	Parte 02 - Utilizando os Operadores
# Operadores de atribuição:
nome = ’Samara’


# Operadores aritméticos: Para realizar cálculos

# Usar o console. Mostrar como limpa o console; ctrl + l

# >>> salario = 600.00
# >>> salario + 50.00
# 650.0
# >>> salario - 100.00
# 500.0
# >>> salario*2
# 1200.0
# >>> salario**2
# 360000.0


# Operadores Relacionais

salario = float(input('Digite seu salário: '))
print(salario)

salario == 500.00

salario != 500.00

salario > 400

salario < 1000


# Operadores Lógicos

nome = input('Digite seu nome: ')
print(nome)

(nome == "Samara") and (salario > 400.00)

(nome == "samara") and (salario > 400.00)

(nome != "Andre") or (salario > 300.00)

DESCONTOS = 50.0

salarioMinimo = 880.0

(nome == "Samara") and ((salario -  DESCONTOS < salarioMinimo)) 






#	Parte 03 – Meu Segundo Programa

# Vamos incluir novas variáveis no nosso programa

salarioMinimo = 880.0

salario = float(input('Digite seu salário: '))

temFilho = input("Você tem filhos? \n (S) - sim \n (N) - não \n")

numeroDeFilho = int(input("Digite o numero de filhos: "))

(temFilho == 'S') and (salario < salarioMinimo)

ajudaFilho = 20.0

salario = salarioMinimo + (ajudaFilho * numeroDeFilho)
print(salario)

# Observe que mesmo para quem não tem filho o código executa o comando que pergunta o numero de filho e calcula a ajuda de filhos
# Seria necessário usar uma condição que calculasse a ajuda filhos só para quem tem filhos. Esse comando é chamado de if (se) e nós veremos na próxima aula como ele funciona.