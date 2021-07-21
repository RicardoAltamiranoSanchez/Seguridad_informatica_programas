#!/usr/bin/env python
#_*_coding: utf8 _*_
import requests
from bs4 import BeautifulSoup #sive para que nos acomode mas el texto
def main():
	agent={'User-Agent':'Firefox'}
	peticion=requests.get(url="https://upem2021ingenieria.herokuapp.com/",headers=agent)
	soup=BeautifulSoup(peticion.text,'html5lib')
	for enlaces in soup.find_all('link'):
		if '/wp-content/themes/' in enlaces.get('href'):
			the=enlaces.get('href')
			the=the.split('/')
			if 'themes' in the:
				pos=the.index('themes')
				themes=the[pos+1]
				print("Temas encontrados:{}".format(themes))


if __name__=='__main__':
	try:
		main()
	except KeyboardInterrupt:
	    print("Saliendo del programa")
	    exit()	
