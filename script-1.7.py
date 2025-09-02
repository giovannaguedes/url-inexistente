#!/usr/bin/python3
import requests

site = requests.get ("http://nome do site aqui.com.br")
status = site.status_code

if (status == 200):
	print("Pagina Existe")
else:
	print("pagina Inexistente" )
