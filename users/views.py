from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(emi):
    respuesta = f"""<html>
			<body> 
		<p> Código de muestra del modelo de usuario </p>
     		<p> Este proyecto de muestra no tiene interfaz de usuario; 
			se trata de jugar con modelos de datos. </p>
     		<p> Si ha creado una cuenta de superusuario, puede visitar las páginas 
			<a href="/admin"> Administrador </a>. </p>
     		<p> Este código de muestra está disponible en
     		<a href="https://github.com/csev/dj4e-samples">https://github.com/csev/dj4e-samples </a> </p>
     			</body> 
		</html>"""
    return HttpResponse(respuesta)
