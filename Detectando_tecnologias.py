#!/usr/bin/env python 
#_*_coding: utf8 _*_
from Wappalyzer import WebPage ,Wappalyzer

def main():
    wap = Wappalyzer.latest()
    try:
    	web=WebPage.new_from_url("https://www.example.com")
    	tecnologias=wap.analyze(web)
    	for t in tecnologias:
    		print("tecnologia encontrada: {t}".format(t))

    except:
        print("Hubo un error")	




if __name__=='__main__':
        try:
           main()
        except KeyboardInterrupt:
           print("Saliendo del programa")
           exit()        
#NOTA REVISAR EL PROGRAMA Y AVERIGUAR EL WAPPALIZER COMO UTILIZARLO EN PYTHON 3 SOLO FUNCIONA EN PYTHON 2