#!/usr/bin/env python
#_*_coding: utf8_*_
import dns.resolver 

def main():
	try:
		arreglo=['A','NS','MD','MF','CNAME','SOA','MB','MG','MR','NULL','WKS','PTR','HINFO','MINFO','MX'
		,'TXT','AXFR','MAILB','MAILA']
		for a in arreglo:
			c=dns.resolver.query('www.google.com',a)
			
			for q in c:
                
				print(q)

		   
	except:
	    print("No  encontro nada")	
  
    

if __name__=='__main__':

	   try:
	   	  main()
	   except KeyboardInterrupt:
	       print("Saliendo del programa")
	       exit()  
