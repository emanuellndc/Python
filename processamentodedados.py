import pandas as pd
import re

def verificacao(z):
   lista =[]
   x = z.upper()
   print(x)
   if re.search('LG', x, re.IGNORECASE):
        lista.append('LG')
   elif re.search('MOTOROLA', x, re.IGNORECASE):
        lista.append('MOTOROLA')
   elif re.search('SAMSUNG', x, re.IGNORECASE):
        lista.append('SAMSUNG')
   elif re.search('SONY', x, re.IGNORECASE):
        lista.append('SONY')
   elif re.search('SONY', x, re.IGNORECASE):
        lista.append('SONY')
   elif re.search('ASSUS', x, re.IGNORECASE):
        lista.append('ASSUS')
   elif re.search('APPLE', x, re.IGNORECASE):
        lista.append('APPLE')   
   elif re.search('CONSUL', x, re.IGNORECASE):
        lista.append('CONSUL')
   elif re.search('ELECTROLUX', x, re.IGNORECASE):
        lista.append('ELECTROLUX')
   elif re.search('PHILCO', x, re.IGNORECASE):
        lista.append('PHILCO')
   elif re.search('PANASONIC', x, re.IGNORECASE):
        lista.append('PANASONIC')
   elif re.search('MIDEA', x, re.IGNORECASE):
        lista.append('MIDEA')
   elif re.search('ELGIN', x, re.IGNORECASE):
        lista.append('ELGIN')
   elif re.search('GREE', x, re.IGNORECASE):
        lista.append('GREE')
   elif re.search('GARRIER', x, re.IGNORECASE):
        lista.append('GARRIER')
   elif re.search('AGRATTO', x, re.IGNORECASE):
        lista.append('AGRATTO')
   elif re.search('DAIKIN', x, re.IGNORECASE):
        lista.append('DAIKIN')
   elif re.search('FUJITSU', x, re.IGNORECASE):
        lista.append('FUJITSU')
   elif re.search('KOMECO', x, re.IGNORECASE):
        lista.append('KOMECO')
   elif re.search('FONTAINE', x, re.IGNORECASE):
        lista.append('FONTAINE')
   elif re.search('BRASTEMP', x, re.IGNORECASE):
        lista.append('BRASTEMP')
   elif re.search('VENAX', x, re.IGNORECASE):
        lista.append('VENAX')
   elif re.search('TRAMONTINA', x, re.IGNORECASE):
        lista.append('TRAMONTINA')
   elif re.search('GELOPAR', x, re.IGNORECASE):
        lista.append('GELOPAR')
   elif re.search('FISCHER', x, re.IGNORECASE):
        lista.append('FISCHER') 
   elif re.search('FOGATTI', x, re.IGNORECASE):
        lista.append('FOGATTI') 
   elif re.search('MUELLER', x, re.IGNORECASE):
        lista.append('MUELLER') 
   elif re.search('SUGGAR', x, re.IGNORECASE):
        lista.append('SUGGAR')  
   elif re.search('CASAVITRA', x, re.IGNORECASE):
        lista.append('CASAVITRA')
   elif re.search('NARDELLI', x, re.IGNORECASE):
        lista.append('NARDELLI')
   elif re.search('ATLAS', x, re.IGNORECASE):
        lista.append('ATLAS')
   elif re.search('ESMALTEC', x, re.IGNORECASE):
        lista.append('ESMALTEC')
   elif re.search('PANASONIC', x, re.IGNORECASE):
        lista.append('PANASONIC')
   elif re.search('WANKE', x, re.IGNORECASE):
        lista.append('WANKE')
   elif re.search('COLORMAQ', x, re.IGNORECASE):
        lista.append('COLORMAQ')
   elif re.search('ITATIAIA', x, re.IGNORECASE):
        lista.append('ITATIAIA')
   elif re.search('CADENCE', x, re.IGNORECASE):
        lista.append('CADENCE') 
   elif re.search('SAFANELLI', x, re.IGNORECASE):
        lista.append('SAFANELLI')
   elif re.search('CHAMALUX', x, re.IGNORECASE):
        lista.append('CHAMALUX')
   elif re.search('REALCE', x, re.IGNORECASE):
        lista.append('REALCE')
   elif re.search('CUISINART', x, re.IGNORECASE):
        lista.append('CUISINART')
   elif re.search('BUILT', x, re.IGNORECASE):
        lista.append('BUILT')
   elif re.search('FRANKE', x, re.IGNORECASE):
        lista.append('FRANKE')                  
   elif re.search('EMICOL', x, re.IGNORECASE):
        lista.append('EMICOL')          
   elif re.search('CONSERVEX', x, re.IGNORECASE):
        lista.append('CONSERVEX')
   elif re.search('OSTER', x, re.IGNORECASE):
        lista.append('OSTER')   
   elif re.search('FALMEC', x, re.IGNORECASE):
        lista.append('FALMEC')
   elif re.search('CRISSAIR', x, re.IGNORECASE):
        lista.append('CRISSAIR')                
   elif re.search('METALFRIO', x, re.IGNORECASE):
        lista.append('METALFRIO')
   elif re.search('POSITIVO', x, re.IGNORECASE):
        lista.append('POSITIVO')
   elif re.search('AOC', x, re.IGNORECASE):
        lista.append('AOC')  
   elif re.search('ACER', x, re.IGNORECASE):
        lista.append('ACER')
   elif re.search('BTUS', x, re.IGNORECASE):
        lista.append('BTUS') 
   elif re.search('BTU', x, re.IGNORECASE):
        lista.append('BTUS')     
   elif re.search('DELL', x, re.IGNORECASE):
        lista.append('DELL')
   elif re.search('LENOVO', x, re.IGNORECASE):
        lista.append('LENOVO')
   elif re.search('MOTO', x, re.IGNORECASE):
        lista.append('MOTOROLA')
   elif re.search('SILENTIA', x, re.IGNORECASE):
        lista.append('SILENTIA')
   elif re.search('HP', x, re.IGNORECASE):
        lista.append('HP')
   elif re.search('CADENCE', x, re.IGNORECASE):
        lista.append('CADENCE')   
   elif re.search('ALIENWARE', x, re.IGNORECASE):
        lista.append('ALIENWARE')  
   elif re.search('PHILIPS', x, re.IGNORECASE):
        lista.append('PHILIPS')
   elif re.search('COMPAQ', x, re.IGNORECASE):
        lista.append('COMPAQ')
   elif re.search('PASSE BEM', x, re.IGNORECASE):
        lista.append('PASSE BEM')     
   return lista 


def ṕrocessamentodedados(df):
   for index, row in df.iterrows():
        lista = verificacao(row['name'])
        market = row['market']
        idproduto = row['id']
        for i in lista:
            with open('processamento.txt', 'a') as arq:
                arq.write(str(idproduto)+";"+i+";"+str(market))
                arq.write('\n')
if __name__ == "__main__":
    data1 = pd.read_csv("teste_ped.csv",chunksize=1, iterator=True,error_bad_lines=False, sep=';',encoding = "ISO-8859-1")
    for chunk in data1:
        lista = ṕrocessamentodedados(chunk)
print("Acabou")
