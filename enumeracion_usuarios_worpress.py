#!/usr/bin/env python
#_*_coding: utf8 _*_
#SE utiliza solo con worpress bueno tecnologias sobre ellas
import json
import urllib
def main():
	url=urllib.urlopen("https://upem2021ingenieria.herokuapp.com/")
	for u in json.loads(url.read()):
		usuarios=u['slug']
	print(usuarios)	
 



if __name__=='__main__':
     try:
         main()
     except KeyboardInterrupt:
         print("Saliendo del programa")
         exit()    s