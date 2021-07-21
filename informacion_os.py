#!/usr/bin/env python
#!*_*coding: utf8_*_
from subprocess import check_output
import subprocess

a=check_output('pwd',stderr=subprocess.STDOUT)#en check_output indicamos el comando que va realizar y si hay erro lo mandamos al pozo sin fondo
n=open('escaneo.txt','w+')#Creamos un archivo y lo ponemos en modo de escritura w si no existe que lo cree w+
n.write(str(a))#Escribimos lo que obtuvimos con check lo ponemos en un archivo de texto
print('Ya te robe')
n.close()