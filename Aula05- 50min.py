# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 22:25:41 2016

@author: samara
"""

# Aula 05 - Tutorial - Funções em Python


#	Parte 01 - Definindo funções
# Criar funções 

# Cria produtos a venda
def produtos():
    produtosVenda = {"SmartTV": 1000.00, "DVD": 100.00, "pen-drive": 50.00}
    return produtosVenda

# Comprar produtos
def comprarProduto(opcao):
    carrinho = {}
    prod = produtos()
    print('Produtos disponíveis:')
    print(prod)
    while (opcao!="nao"):
        nomeProduto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))
          
        preco = prod[nomeProduto]        
        carrinho[nomeProduto]=quantidade,preco,preco*quantidade       
        print('carrinho:')
        print(carrinho)
        
        opcao = input("Deseja comprar mais produtos? Digite sim ou nao :")       
    return carrinho

# Mostrar Erro: Comprar produto inexistente    

# calcular total    
def calcularTotal(carrinho):
    total = 0
    for produto in carrinho:
        total = total + carrinho[produto][2]
    print('Total da compra: %f '%(total))
    return total

# CONSOLE chamar todas as funções    
produtos()
opcao = 'sim'
carrinho = comprarProduto(opcao)
calcularTotal(carrinho)

   
#   Parte 02: Definindo módulos

# Salvar PARTE 01 'comprar.py' 
# Rodar (só funções)

# Criar arquivo 'principal.py'

# Importar o modulo 
import comprar

# Criar funcao desconto
def descontoValor(total):
    if total >= 1000:
        print('Você ganhou 20 porcento de desconto')
        desconto = 0.2 * total
    else:
        print('Só há desconto para compras acima de 1000 reais')
        desconto = 0
    return desconto

# Criar função principal
def main():
    opcao = input('Deseja comprar um produto? \n Digite sim ou nao: \n')
    carrinho = comprar.comprarProduto(opcao)
    total = comprar.calcularTotal(carrinho)
    
    desconto1 = descontoValor(total)
    
    total = total - desconto1
    print('Novo total: %f'%(total))
main()






















#   Parte 03: Meu quinto programa

# Alterar o comprar.py
# Criar - Excluir produtos do carrinho
def excluirProdutos(nomeProduto,carrinho):
    del carrinho[nomeProduto]
    
# Alterar o main() do principal.py 
def main():
    opcao = input('Deseja comprar um produto? \n Digite sim ou nao: \n')
    carrinho = comprar.comprarProduto(opcao)
    total = comprar.calcularTotal(carrinho)
    
    excluir = input('Deseja excluir um produto do carrinho? sim ou nao: \n')
    while excluir == 'sim':
        nomeProduto  = input('Digite o produto a ser excluído: ')
        comprar.excluirProdutos(nomeProduto,carrinho)
        total = comprar.calcularTotal(carrinho)
        excluir = input('Deseja excluir mais um produto? sim ou nao: \n')
        
    desconto1 = descontoValor(total)
    total = total - desconto1
    print('Novo total: %f'%(total))   
main()    


# Import math 
import math 

math.floor(total)
math.fsum([total,desconto1])


# Import date
from datetime import date
hoje = date.today()
print(hoje)

aniversario = date(2000, 8, 27)

if hoje.month == aniversario.month:
    print('Mês de aniversário da loja! Desconto de 10% nas compras acima de 1.000')
    


       
     
            