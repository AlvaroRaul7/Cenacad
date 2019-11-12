import requests

from bs4 import BeautifulSoup

def cargarurl(url):

    # URL = "https://cenacad.espol.edu.ec/index.php/module/Report/action/DetallePar/id_p/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    return soup

def procesararchivo(ruta):

    f = open("subjects.txt", "r")
    diccionariomaterias = {}

    for linea in f:
        linea =linea.strip().split(",")
        listacod = []
        codeidp = linea[7]
        codeide = linea[8]
        listacod.append(codeidp)
        listacod.append(codeide)
        nombremateria = linea[4]
        diccionariomaterias[nombremateria] = listacod


    return diccionariomaterias




diccionario = procesararchivo("subjects.txt")
listahtml = []
for key,value in diccionario.items():
     sopa = cargarurl("https://cenacad.espol.edu.ec/index.php/module/Report/action/DetallePar/id_p/"+value[0]+"/id_e/"+value[1])
     listahtml.append(sopa)



