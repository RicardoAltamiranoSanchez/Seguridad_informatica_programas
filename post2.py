#!/usr/bin/env python 
#_*_coding: utf8 _*_
import requests
import argparse
from os import path
parser=argparse.ArgumentParser(description="Subida de archivos")
parser.add_argument('-f','--file',help="Indicamos el archivo")
parser=parser.parse_args()
def main():
	if parser.file:
		if path.exists(parser.file):
			archivo=open(parser.file,'rb')
			headers={'User-Agent':'Firefox'}
			peticion=requests.post(url="https://curso--python-0-prueba-pentest1.000webhostapp.com/",files={"uploaded_file":archivo},headers=headers)
			if parser.file in peticion.text:
				print(peticion.text)
				print("Archivo subo con exito")
			else:
			 print("No se pudo subir el archivo")	

		else:
		 print("No se pudo subir el archivo")	
	else:
	 print("Debes subir un archivo")	
	
   



if __name__=='__main__':
	main()
