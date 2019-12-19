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
    g = open("materias_Paralelos.csv","w",encoding='utf8')
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
            g.write(linea[3]+","+linea[4]+","+linea[5]+"\n")
    g.close()
    return diccionariomaterias


def sopacalificacionporcodmateria(codigo,diccionario):
    listacod = diccionario.get(codigo)
    sopa = cargarurl("https://cenacad.espol.edu.ec/index.php/module/Report/action/DetallePar/id_p/"+listacod[0]+"/id_e/"+listacod[1])
    return sopa

def cargarGeneral():
    file = open("preguntas.csv","w")
    dic = procesararchivo("subjects.txt")
    codigo = dic.keys()
    for i in codigo:
        listacod = mostrarpreguntas(i,dic)
        profesor= str(mostrarprofesorporcod(i,dic))
        file.write(profesor+"\n")
        pd.DataFrame.to_csv(listacod,path_or_buf=file,index=False,header=False,sep=";")

def mostrarprofesorporcod(codigo,dic):
    #dic = procesararchivo("subjects.txt")
    sopa = sopacalificacionporcodmateria(codigo,dic)
    tabla = sopa.find('table' ,attrs={'class':'tbl centrado'}) #Buscar nombre de profesor en el html
    encabezado = tabla.find('td')
    text = encabezado.renderContents()
    texto_encabezado = text.strip()
    texto_encabezado = str(texto_encabezado).split('\\n')
    componentes = texto_encabezado[3].rstrip(' <br/>\'')
    componentes = componentes.lstrip('        Profesor: ')
    return(componentes) #Depurado el nombre del profesor


def mostrarpreguntas(codigo, dic):
    sopa = sopacalificacionporcodmateria(codigo,dic)
    data =  sopa.findAll('table')[3].findAll('tr') #Encuentra la tabla donde estan las preguntas con las respuestas
    l = []
    for tr in data:
        cols = tr.findAll('td')
        fila = [tr.text for tr in cols]
        l.append(fila)
    df = pd.DataFrame(l, columns=["No de Pregunta","Contenido", " Media","Desviacion Estandar","Puntaje Obtenido"])
    df = df.drop(df.index[[0,1]])
    col_depurada= df['No de Pregunta'].str.replace('\\n','', regex=True) # Eliminar saltos de linea de la columna de no de pregunta
    df['No de Pregunta'] = col_depurada
    return df

def separarPreguntas(nombre):
    file = open(nombre,"r")
    diccionario = {}
    for linea in file:
        linea = linea.strip().split(';')
        if len(linea)>2:
            lista = []
            media = linea[2]
            desviacion = linea[3]
            lista.append(media)
            lista.append(desviacion)
            pregunta = linea[1]
            if pregunta in diccionario.keys():
                diccionario[pregunta].append(lista)
            else:
                diccionario[pregunta] = lista
    return diccionario


# FICT03509
# FICT03053
# FMAR04564
# EDCOM00281
#mostrarpreguntas('ESTG1028')
#mostrarpreguntas('INDG1022')
#mostrarpreguntas('EDCOM00281')
#mostrarpreguntas('FMAR04564')
#mostrarpreguntas('FICT03509')
#mostrarprofesorporcod('FICT03509')
preguntas = cargarGeneral()
#lista=separarPreguntas("preguntas.csv")
#print(lista)


