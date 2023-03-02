from random import choice
import wikipedia

saludo = [
    "saludo",
    "Hola Humano :)",
    "Holaa",
    "Aqui estoy 👋",
    "3lli0t_04: On \n:b"
]

help = """
Hi, mi nombre es 3lli0t_04 aqui podras aprender a usarme :)
Los comandos disponibles son:

/start - Saludame y veras si estoy vivo.
/help - Invoca este mensaje de ayuda.
/rules - Invoca las reglas de la comunidad.
/list - Enlista a todos los alumnos y su número de lista
/list x - Cambia x por tu número de lista y te da información detallada
/confirm x - Confirma la limpieza del estudiante

Create by: @al3x_argu
Code: github.com/JorgeArguello1999
"""

help_admin = """
Estos son los comandos para los administradores
/insert -> Ingresa un nuevo estudiante de la siguiente manera:
> /insert 1, 3lli0t_04, #reclamos, #veceslimpieza, #date
/update -> Actualiza la información de un estudiante
> /update 1, 3lli0t_04, telegram_user, #reclamos, #veceslimpieza
/delete -> Elimina un estudiante
> /delete 1
"""

rules = """
Objetivos del grupo:

Grupo enfocado en aprender Python practicando y resolviendo problemas desde el nivel mas básico y área relacionada con Python, retos e ideas de programas constantes para practicar y proyectos en grupo.

Reglas:

1.)No insultar a otros miembros
2.)Respetar las opiniones de los demás.
3.)No hacer spam  de offtopic.
4.)Antes de hacer una pregunta investigar.

"""

def definiciones(palabra):
    """ Definiciones de palabras """
    wikipedia.set_lang("es")
        
    try: 
        resumen = wikipedia.summary(palabra, sentences = 1)
        url = (wikipedia.page(palabra).url)
        return (resumen + "\n\nMas info: " + url)
    except: 
        return "No se ha encontrado esta definicion..."

# Function Hi
def send_saludo():
    return choice(saludo) 
