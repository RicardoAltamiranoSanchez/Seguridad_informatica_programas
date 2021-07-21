#!/usr/bin/env python 
#!*_*coding: utf8_*_
import os
import subprocess

a=open(os.devnull,'w');#devnull es un archivo si fondo lo abrimos para enviar la informacion ahi
p=subprocess.call(['ping','1.1.1.1'],stdout=a,stderr=subprocess.STDOUT)
#call es para llamar una ejecucion que vamos hacer se separa con comas
#STDOUT ES LA SALIDA ESTANDAR ES ELCOMANDO QUE SE EJECUTA CORRECAMENTE 
#STDERR ES EL ESTANDAR ERROR STDOUT IGUAL ES UN POZO SIN FONDO COMO OS.DEVNULL
if p==0:
	print("Se ejecuto correctamente")
else:
   print("No se ejecuto correctamente")	