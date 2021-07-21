#!/usr/bin/env python
#_*_coding: utf8 _*_
import requests
from bs4 import BeautifulSoup #sive para que nos acomode mas el texto


def main():
	r=requests.get('https://upem2021ingenieria.herokuapp.com/')#nota  el link solo sirve con el de curso probar mas  numero de curso o clase 77
	soup=BeautifulSoup(r.text,'html5lib')
	for w in soup.find_all('pre'):
		print(w.get_text())




if __name__=='__main__':
	try:
		main()
	except KeyboardInterrupt:
	    print("Saliendo del programa")
	    exit()	
