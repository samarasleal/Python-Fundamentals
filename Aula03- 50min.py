# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 13:44:54 2016

@author: samara
"""
# Aula 03 - Tutorial – Comandos em Python


#	Parte 01 - Utilizando comandos de decisão
# Comandos  de decisão (if) 

nome = input("Digite seu nome: ")
senha = input('Digite sua senha: ')
salario = float(input('Digite seu salário: '))
salarioMinimo = 880.0
ajudaFilho = 20.0
temFilho = input("Você tem filhos? \n (S) - sim \n (N) - não \n")

if (temFilho == "S"):
    numeroDeFilho = int(input("Digite o numero de filhos: "))
    if (salario < salarioMinimo):
        salario = salarioMinimo + (ajudaFilho * numeroDeFilho)

print('Seu salarário é: %f'%(salario))


# Comando else

# Alterar o código acima incluindo o comando else = senão

if (temFilho == "S"):
    numeroDeFilho = int(input("Digite o numero de filhos: "))
    if (salario < salarioMinimo):
        salario = salarioMinimo + (ajudaFilho * numeroDeFilho)
    else:
        salario = salario + (ajudaFilho * numeroDeFilho)
else: 
    print ('Você não tem filhos, seu salário não será atualizado.')
print('Seu salarário é: %f'%(salario))














#	Parte 02 - Utilizando comandos de repetição e tratando erros
# Comandos de repetição (while)

nome = input("Digite seu nome: ")
senha = input('Digite sua senha: ')

while (nome == senha) or (len(senha)==0):
    print("A senha deve ser diferente do nome. E deve ser informada!")
    senha = input('Digite outra sua senha: ')

print('Senha cadastrada com sucesso.')


# Tratamento de erros

temFilho = input("Você tem filhos? \n (S) - sim \n (N) - não \n")

while (temFilho == "S"):
    try:
        numeroDeFilho = int(input("Digite o numero de filhos: "))
        break
    except:
        print('Você deve digitar um valor numérico')


# While com incremento

if (temFilho == "S"):
    # índice
    i = 0 
    while i < numeroDeFilho:
        nomeFilho = input('Digite o nome do seu filho  %d'%(i))
        print(nomeFilho)
        # incremento 
        i = i + 1 

# mostrar loop infinito e como matar o processo
        
















#	Parte 03 - Meu Terceiro Programa

# Função range

range(10) # gera número de 0 a 9

numeroDeFilho = int(input("Digite o numero de filhos: "))
range(numeroDeFilho) # gera de 0 ate a quantidade de filhos


# Comando For 

for i in range(numeroDeFilho):
    nomeFilho = input('Digite o nome do seu filho  %d :'%(i))
    while (True):
        try:
            idade = int(input('Digite a idade do seu filho %d :'%(i)))
            break
        except:
            print('Você deve digitar um valor numérico')    
    print(nomeFilho)
    print(idade)


# Ao imprimir o valor de nomeFilho e idade só o do último filho irá aparecer
# por que você não esta salvando os últimos valores digitados e esta sobreescrevendo as variáveis.
# Para salvá-lo é necessário usar uma lista ou arquivo que veremos na próxima aula

print(nomeFilho)
print(idade)



