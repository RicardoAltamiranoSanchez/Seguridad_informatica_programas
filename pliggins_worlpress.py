#!/usr/bin/env python
#_*_coding: utf8 _*_
#Esta bien el codigo pero volverlo hacer maldito pyhton solo jode 
#con su tabulacion de mierda
import requests
from progress.bar import Bar
from os import path
def main():
	if path.exists('users_password.txt'):
		w=open('users_password.txt','r')
		w=w.read().split('/n')
		url="https://upem2021ingenieria.herokuapp.com/"
	    lista=[]
	    progreso=Bar("Espere....",max=len(w))
	    for pluggin in w:
	    	progreso.next()
	    	try:
	    		p=requests.get(url=url+'/'+pluggin)
	    		if p.status_code==200:
	    			final=url+'/'+pluggin
	    			lista.append(final.split('/')[-2])

	    	except:
	    	    pass

	    b.finish()
	    for pluggin in lista:
	        print('Pluggins encontrados:{}'.format(pluggin))	    	
	else:
	print("No se encuentra la lista")    	


if __name__=='__main__':
       try:
          main()
        except KeyboardInterrupt:
          print("Saliendo del programa")
          exit()  	