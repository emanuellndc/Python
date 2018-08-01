# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 22:00:42 2018

@author: Emanuel Carvalho
"""
import requests 
from bs4 import BeautifulSoup
from time import sleep

def urls(qtpaginas):
    lista = []
    for i in range(1,qtpaginas+1):
        lista.append('https://www.kanui.com.br/acessorios-masculinos/bones/?page='+str(i))

    return lista   

def request(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup
    
def getNomes(soup):    
   nomep = soup.find_all('p',class_='product-box-title')
   nomes = [item.get_text() for item in nomep]
   return nomes
    
def getPreço(soup):
    preços = []
    preçoteg = soup.find_all('span', class_='product-box-price-to')
    preços = [item.get_text() for item in preçoteg]
    return preços

class Produto(object):

  def __init__(self, name, preço):
   self.name = name
   self.preço = preço # creates a new empty list for each dog

if __name__ == "__main__":
    
    nome = []
    preços = [] 
    listadadospaginas = []
    html = []
    linkscompletos = []
    linkscompletos = urls(3)
    
    for i in linkscompletos:
        html.append(request(i))
        sleep(1)        
    for item in html:
       nome.append(getNomes(item))
       preços.append(getPreço(item))
       
    print(nome)
    print(preços)
        