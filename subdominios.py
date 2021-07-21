#!/usr/bin/env python
#_*_coding: utf8_*_
import dns.resolver
from os import path

def main():
	if path.exists('subdominios(1).txt'):
		wordlist=open('subdominios(1).txt','r')
		wordlist=wordlist.read().split('\n')
		lista=[]
		for l in wordlist:
			try:
			   a=dns.resolver.resolve('{}.upem2021ingenieria.herokuapp.com'.format(l),'A')
			   lista.append('{}.google.com'.format(l))
			except:
			   pass
		if len(lista)>0:
			print('Posible subdominios {}'.format(len(lista)))
			for q in lista:
				print(q)


	else:
	   print("No existe el archivo")		




if __name__=='__main__':
	try:
		main()
	except KeyboardInterrupt:
	    print("Saliendo del programa")
	    exit()	
