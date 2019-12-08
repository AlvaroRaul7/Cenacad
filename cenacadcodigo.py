import requests
import pandas as pd
from bs4 import BeautifulSoup



def cargarurl(url):

    #URL = "https://cenacad.espol.edu.ec/index.php/module/Report/action/DetallePar/id_p/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    return soup

def procesararchivo(ruta):

    f = open("subjects.txt", "r", encoding="utf8")
    diccionariomaterias = {}

    for linea in f:
        linea =linea.strip().split(",")
        anioTermino = linea[1]
        if anioTermino=="2018" or anioTermino=="2019":
            listacod = []
            codeidp = linea[7]
            codeide = linea[8]
            listacod.append(codeidp)
            listacod.append(codeide)
            codmateria = linea[3]
            diccionariomaterias[codmateria] = listacod


    return diccionariomaterias


def sopacalificacionporcodmateria(codigo,diccionario):
    listacod = diccionario.get(codigo)
    sopa = cargarurl("https://cenacad.espol.edu.ec/index.php/module/Report/action/DetallePar/id_p/"+listacod[0]+"/id_e/"+listacod[1])
    return sopa



def mostrarprofesorporcod(codigo):
    dic = procesararchivo("subjects.txt")
    sopa = sopacalificacionporcodmateria(codigo,dic)
    print(sopa)
    tabla = sopa.find('table' ,attrs={'class':'tbl centrado'}) #Buscar nombre de profesor en el html
    encabezado = tabla.find('td')
    text = encabezado.renderContents()
    texto_encabezado = text.strip()
    print(texto_encabezado) #Falta depurar la cabecera para mostrar el nombre completo del profesor


def mostrarpreguntas(codigo):
    dic = procesararchivo("subjects.txt")
    print(dic)
    sopa = sopacalificacionporcodmateria(codigo,dic)
    data =  sopa.findAll('table')[3].findAll('tr') #Encuentra la tabla donde estan las preguntas con las respuestas
    l = []
    for tr in data:
        cols = tr.findAll('td')
        fila = [tr.text for tr in cols]
        l.append(fila)
    df = pd.DataFrame(l, columns=["No de Pregunta","Contenido", " Media","Desviacion Estandar","Puntaje Obtenido"])
    df = df.drop(df.index[[0,1]])
    col_depurada= df['No de Pregunta'].str.replace('\\n',' ', regex=True) # Eliminar saltos de linea de la columna de no de pregunta
    df['No de Pregunta'] = col_depurada
    print(df)

# FICT03509
# FICT03053
# FMAR04564
# EDCOM00281
#mostrarpreguntas('ESTG1028')
mostrarpreguntas('INDG1022')
#mostrarpreguntas('EDCOM00281')
#mostrarpreguntas('FMAR04564')
#mostrarpreguntas('FICT03509')
#mostrarprofesorporcod('FICT03509')




