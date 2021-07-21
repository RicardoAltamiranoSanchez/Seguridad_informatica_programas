#!/usr/bin/env python 
#*_*conding: utf8_*_
#obteniendo los banners de los servidores atraves de socket
import socket
def main():
	s=socket.socket()
	try:
		s.connect(('upem2021ingenieria.herokuapp.com',21))
		banner=s.recv(1024)
		print(banner)
	except:	
		print('Hubo un error')
  


if __name__=='__main__':
   
   try:
      main()
   except KeyboardInterrupt:
    	print('Saliendo del programa')
      	
