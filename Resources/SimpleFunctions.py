from random import choice

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
/list_st x - Cambia la 'x' por tu número de lista para ver infromación detallada

Create by: @al3x_argu
Code: github.com/JorgeArguello1999
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

# Function Hi

def send_saludo():
    return choice(saludo) 
