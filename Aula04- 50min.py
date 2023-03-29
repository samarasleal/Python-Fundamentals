# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 17:25:40 2016

@author: samara
"""

# Aula 04 - Tutorial - Estrutura de dados em Python


#	Parte 01 - Criando Listas e Dicionários
# Criar e acessar valores
listaNomes = ["Talita","Andre","Juliana"]
listaNomes[0]
print(listaNomes)


# Adicionar 
listaFilhos = [] 
listaIdades = []
numeroDeFilho = int(input('Digite o número de filhos'))
for i in range(numeroDeFilho):
    nomeFilho = input('Digite o nome do seu filho  %d :'%(i))
    listaFilhos.append(nomeFilho) 
    while (True):
        try:
            idade = int(input('Digite a idade do seu filho %d :'%(i)))
            listaIdades.append(idade)
            break
        except:
            print('Você deve digitar um valor numérico')    
print(listaFilhos)
print(listaIdades)


# Retirar
# Retirar da lista de dependentes os filhos maiores de 18 anos
for valor in listaIdades:
    if valor >= 18:
        posicao = listaIdades.index(valor)
        listaIdades.remove(valor)
        listaFilhos.pop(posicao)
print("Filhos maiores que 18 anos foram retirados da lista de dependentes")
print(listaFilhos)
print(listaIdades)
   

# Dicionário
dicionarioFilhos = {"Filho": listaFilhos+listaIdades} 
dicionarioFilhos.values()



   
#	Parte 02 - Utilizando Arquivos de dados

# Criar com w (apaga conteúdo)

listaFilhos = ['Maria', 'Andre', 'Joaquim'] 
arquivo = open("filhos.txt","w")
for valor in listaFilhos:
    arquivo.write("%s \n" % valor)
arquivo.close()

# Comando a


# Ler
listaDoArquivo = []
arquivo = open("filhos.txt","r")
for linha in arquivo.readlines():
    print(linha)
#    linha = linha.replace("\n", "")   # mostrar como tirar o \n
    listaDoArquivo.append(linha)
arquivo.close()
print(listaDoArquivo)
































#	Parte 03 -  Meu Quarto Programa 


# Realizar compras na internet

produtosVenda = {"iphone": 400.00, "livro": 40.00, "caneta": 10.00}
print("Produtos disponíveis:")
print(produtosVenda)

# pesquisar por produto
produtosVenda["iphone"]

carrinho = {}
total = 0
opcao = input("Deseja adicionar algum item ao carrinho? Digite sim ou nao:")
while (opcao!="nao"):
    nomeProduto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    
    preco = produtosVenda[nomeProduto]
    
    carrinho[nomeProduto]=quantidade,preco,preco*quantidade
    
    print('carrinho:')
    print(carrinho)
    
    total = total + (preco*quantidade)
    print("Total: %f"%(total))
    
    opcao = input("Deseja comprar mais produtos? Digite sim ou nao :")

print("O total da sua compra foi %f: "%(total))


# Agora vamos pensar que vários usuários vão realizar compras. E, também para gera um boleto para o sistema de cobrança também será necessário calcular o total da compra
# Vocês percebem que várias pessoas acessam ao sistema que calcula o total da compra
# Imagina se cada vez que fosse calcular esse total a gente tivesse que escrever esse trecho de código, vcs concordam comigo que o código ficaria extenso e repetitivo. 
# Para evitar o retrabalho nós criamos as funções (nesse caso a gente criaria a função compra)
