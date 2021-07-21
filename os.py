#!/usr/bin/env python
#_*_coding: utf8_*_

import os

print('Ruta especifica'+os.getcwd())#Obtenemos la ruta especifica donde estamos
os.chdir('/home/hacker/Desktop')#Nos movemos a una ruta especifica con chdir
print('Ruta nueva'+os.getcwd())
print(os.listdir(os.getcwd()))#Enlistamos todo donde pusimos la ruta 
#print(os.mkdir('Nueva_Carpeta'))#Creamos una nueva carpeta
#os.rmdir('Nueva_Carpeta')#Eliminamos la carpeta
#os.rename('COMANDOS.txt','Comandos_linux.txt')#Renombramos un archivo de texto
print(os.stat('Comandos_linux.txt'))#Vemos informacion de quien lo hizo o grupo varias cosas mas
os.system('ping 8.8.8.8');#Usamos la terminal o controladamos para hacer algo