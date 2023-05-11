import PySimpleGUI as sg
import io
import os
import csv
import ast
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime


def abrir_img(ruta, ventana):
    if os.path.exists(ruta):
                image = Image.open(ruta)
                image.thumbnail((200, 200))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                ventana["-IMAGE-"].update(data=bio.getvalue())


def generarMetadatos(ruta, csvfile):
    with Image.open(ruta) as img:    
        texto_descriptivo = "-"
        resolucion = "{}x{}".format(*img.size)
        tamaño = str(int(os.path.getsize(ruta) / 1024 )) + 'kb'      
        mimetype = img.format
        lista_tags = str([])
        ultPerfil = "perfilactual"
        ultFecha = str(datetime.now())
    writer = csv.writer(csvfile)
    datos_nuevos = [ruta, texto_descriptivo, resolucion, tamaño, mimetype, lista_tags, ultPerfil, ultFecha]
    writer.writerow(datos_nuevos)
    return datos_nuevos

def buscar_metadatos(ruta):
    if os.path.exists(ruta):
        with open(os.path.join(os.getcwd(), "main_folder", "logs", "metadatos_imagenes.csv"), 'r+') as csvfile: 
            csvreader = csv.reader(csvfile)
            contenido_csv = list(csvreader)
            datos_imagen = [] 
            for linea in contenido_csv:
                if ruta in linea: #si el string de la ruta matchea con el de la ruta de alguna linea, significa que la imagen tiene metadatos correspondientes.
                    datos_imagen.append(linea) #tomo sus datos
            if not datos_imagen:
                return generarMetadatos(ruta, csvfile)
        print(datos_imagen)
        return datos_imagen[(len(datos_imagen) - 1)]

def agregar_log(metadatos):
    # Escribir la lista modificada de vuelta al archivo CSV
    with open(os.path.join(os.getcwd(), "main_folder", "logs", "metadatos_imagenes.csv"), 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(metadatos) 

def agregar_tag(tag, metadatos):
    lista_tags = ast.literal_eval(metadatos[5])
    lista_tags.append(tag)
    lista_tags_tostr = str(lista_tags)
    metadatos[5] = lista_tags_tostr
    metadatos[7] = str(datetime.now())
    agregar_log(metadatos)
    return lista_tags_tostr

def eliminar_tag(tag, metadatos):
    lista_tags = ast.literal_eval(metadatos[5])
    lista_tags.remove(tag[0])
    lista_tags_tostr = str(lista_tags)
    metadatos[5] = lista_tags_tostr
    metadatos[7] = str(datetime.now())
    agregar_log(metadatos)    
    return lista_tags_tostr


def agregar_descripcion(desc, metadatos):
    metadatos[1] = desc
    metadatos[7] = str(datetime.now())
    agregar_log(metadatos)


def ejec_etiquetador():
    print(os.getcwd())
    layout = [  
    [sg.Text("Choose a file: "), sg.Input(key="-RUTAIMAGEN-", enable_events=True), sg.FileBrowse(target="-RUTAIMAGEN-", file_types=[("Archivos PNG", "*.png"), ("Archivos JPEG", "*.jpeg"), ("Archivos JPG", "*.jpg") ])],
    [sg.Image(key="-IMAGE-")], #agregar filtro de mimetypes de imagenes unicamente.
    [sg.Text("Metadatos", font=("Arial", 14)), sg.Multiline(key="-METADATOS-", size=(30, 6), disabled=True)],
    [sg.Listbox(values=[], size=(20,6), key="-TAGSACTUALES-")],
    [sg.Button("Eliminar tag", key="-ELIMINARTAG-")],
    [sg.Text("Tags", font=("Arial", 14)), sg.Input(key="-TAGSINPUT-")], 
    [sg.Button("Agregar tag", key="-AGREGARTAG-")],
    [sg.Text("Descripcion", font=("Arial", 14)), sg.Input(key="-DESCRIPCION-")], 
    [sg.Button("Agregar descripcion", key="-AGREGARDESC-")],
    [sg.Button("Volver", key="-VOLVER-")]
             ]
    
    ventana_etiquetador = sg.Window('Etiquetar imagen', layout, size=(1024, 720), background_color='#0070FF')

    while True:
        events, values = ventana_etiquetador.read()

        match events:
            case "-VOLVER-":
                break
            case sg.WIN_CLOSED:
                break
            case "-RUTAIMAGEN-":
                ruta = values["-RUTAIMAGEN-"] # Toma el valor del espacio input del browser (ruta de la imagen)
                abrir_img(ruta, ventana_etiquetador) 
                metadatos = buscar_metadatos(ruta)
                etiquetas_to_list = ast.literal_eval(metadatos[5])
                ventana_etiquetador["-TAGSACTUALES-"].Update(values= [etiqueta.strip("'") for etiqueta in etiquetas_to_list])
                ventana_etiquetador["-METADATOS-"].Update(value= "\n".join(metadatos))
            case "-AGREGARTAG-":
                tag = values["-TAGSINPUT-"]
                if "-RUTAIMAGEN-":
                    lista_etiquetas = agregar_tag(tag, metadatos)
                    etiquetas_to_list = ast.literal_eval(lista_etiquetas)
                    ventana_etiquetador["-TAGSACTUALES-"].Update(values= [etiqueta.strip("'") for etiqueta in etiquetas_to_list])
                    ventana_etiquetador["-METADATOS-"].Update(value="\n".join(metadatos))
                ventana_etiquetador["-TAGSINPUT-"].Update('')
            case "-ELIMINARTAG-":
                if values["-TAGSACTUALES-"]:
                    eliminar = values["-TAGSACTUALES-"]
                    lista_etiquetas = eliminar_tag(eliminar, metadatos)
                    etiquetas_to_list = ast.literal_eval(lista_etiquetas)
                    ventana_etiquetador["-TAGSACTUALES-"].Update(values= [etiqueta.strip("'") for etiqueta in etiquetas_to_list])
                    ventana_etiquetador["-METADATOS-"].Update(value="\n".join(metadatos))
            case "-AGREGARDESC-":
                if values["-DESCRIPCION-"]: 
                    descripcion = values["-DESCRIPCION-"]
                    agregar_descripcion(descripcion, metadatos)
                    ventana_etiquetador["-METADATOS-"].Update(value="\n".join(metadatos))

    ventana_etiquetador.close()

ejec_etiquetador()
