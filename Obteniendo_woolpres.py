#!/usr/bin/env python
#_*_coding: utf8_*_
import request
from bs4 import BeautifulSoup #sive para que nos acomode mas el texto
import argparse
parser=argparse.ArgumentParser(description="Buscando tecnologia woorlpress")
parser.add_arguments('-u','--url',help="indique la url")
parser=parser.parse_args()
def main():
	url=""
	cabecera={'User-Agent':'Firefox'}
	peticion=request.get(url=url,headers=cabecera)
	soup=BeautifulSoup(peticion.text,'html5lib')
    for v in soup.find_all('meta'):
    	if v.get('name')=='generator':
    		version=get.get('content')
    		print(version)


if __name__=='__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Saliendo del programa")
		exit()
		
