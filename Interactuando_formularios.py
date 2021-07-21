#!/usr/bin/env python 
#_*_coding: utf8_*_
import mechanize
import argparse
from bs4 import BeautifulSoup #sive para que nos acomode mas el texto

parser=argparse.ArgumentParser(description="Busqueda en la web")
parser.add_argument('-b','--buscar',help='Necesita el nombre de que buscar')
parser=parser.parse_args()

def main():
	if parser.buscar:
		bus=mechanize.Browser()
		bus.set_handle_robots(False)
		bus.set_handle_equiv(False)
		bus.addheaders=[('User-Agent','Firefox')]
		bus.open('https://www.google.com')
		#for n in bus.forms():#Localizamos los formularios disponibles
		#	print(n)
		bus.select_form(nr=0)#sSeleccionamos el formulario 
		bus['q']=parser.buscar#Buscamor en q por que es de texcontrol 
		bus.submit()
		#print(bus.response().read())
		p=BeautifulSoup(bus.response().read(),'html5lib')#Es para nos acomode mejor el codigo obtenido o informacion
		for link in p.find_all('a'):#Obtenemos todo que inicie con la a de url
			u=link.get('href')##nos muestra los link de salida a otra pagina
			u=u.replace('/url?q=','')#Remplazamos este elemento para tener un mejor entendimiento 
			print(u)

	else:
	   print("Digite la palabra a buscar")	





if __name__=='__main__':
    try:
       main()
    except KeyboardInterrupt:
       print("Saliendo del programa")
       exit()   	