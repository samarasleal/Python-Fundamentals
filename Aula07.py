# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 22:11:05 2016

@author: samara
"""
import math
def calcularMedia(listaNotas,qtde):
    media = math.fsum(listaNotas)/qtde
    return media
    
def aprovado(media):
    if media >= 6:
        print('aprovado')
    else:
        print('reprovado')
        
listaNotas = [4,5,2,9]
qtde = 4
media = calcularMedia(listaNotas,qtde)
aprovado(media)
    