#!/usr/bin/env python
#_*_coding: utf8_*_
import requests
from bs4 import BeautifulSoup

def main():
	resultado=requests.get('https://www.example.com')
	soup=BeautifulSoup(resultado.text,'html5lib')
	for w in soup.find_all('pre'):
		print(w.get_text())

if __name__=='__main__':
     
     try:
     	main()

     except KeyboardInterrupt:
         print('Saliendo del programa')
         exit()	