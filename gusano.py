#!/usr/bin/env python 
#*_*conding: utf8_*_

import shutil
import sys
#sys arg se crea una lista de todos los argumentos que depasemos el nombre del archivo siempre va ir en la posicion 0 del archivo




def main():
    if len(sys.argv) >=2:
        for n in range(0,int(sys.argv[1])):
        	shutil.copy(sys.argv[0],sys.argv[0]=str(n)+'.py')
    else:
    	print('Falta argumentos')
  

if __name__=='__main__':
       try:
          main()
        except KeyboardInterrupt:
            exit()
            print("Saliendo del programa")     	