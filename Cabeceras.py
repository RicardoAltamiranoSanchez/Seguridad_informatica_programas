#!/usr/bin/env python 
#_*_coding: utf8 _*_
import requests
import argparse
#Definimos las opciones disponible seria como un menu de opciones como en git pero sin el menu
parser=argparse.ArgumentParser(description="Dectetor de cabeceras") #Definimos el argumento solamente y para que sirve
parser.add_argument('-t','--target',help="Objetivo")#Definimos los argumento de como lo vamos a iniciar
parser=parser.parse_args()#de decimos que ya esta listo


def main():
	if parser.target:
		try:
			url=requests.get(url=parser.target)
			cabeceras=dict(url.headers)
			for x in cabeceras:
				print(x+" :"+cabeceras[x])
		except Exception as e:
			print("No se puedo conecar tipo de error:{}".format(e))
		
	else:
	    print("Debemos especificar algo que debes escanear")	

if __name__=='__main__':
       try:
          main()	
       except KeyboardInterrupt:
           print('Saliendo del programa')
           exit() 