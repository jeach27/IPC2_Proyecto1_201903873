import sys
import tkinter
from tkinter import filedialog
import lista
from xml.dom import minidom

def leerArchivo():
    archivo = filedialog.askopenfilename(title = 'Cargar Archivo', filetypes = (('xml files','*.xml'),('all files','*.')))
    return archivo  


class proyect:
        
    def menu(self):
        general = lista.ListaCircular()
        while True:
            print('\n----------------Menú principal--------------------')
            print('\n> Elija una opcion')
            print('\n1.Cargar Archivo\n2.Procesar Archivo\n3.Escribir Archivo Salida\n4.Mostrar Datos Estudiantes\n5.Generar Gráfica\n6.Salir')
            n=input('\n> Ingrese valor\n')
            if n=='1':
                j = leerArchivo()
                archivo = minidom.parse(j)
                matrizz = archivo.getElementsByTagName('matriz')
                for matriz in matrizz:
                    nombre = matriz.getAttribute('nombre')
                    n = int(matriz.getAttribute('n'))
                    m = int(matriz.getAttribute('m'))
                    mat = lista.Lista(lista.ListaCircular(),nombre,n,m)
                    for i in range(n):
                        parcial = lista.Lista(lista.ListaCircular(),None,i,None)
                        for k in range(m):
                            x = matriz.getElementsByTagName('dato')[i*m+k]
                            e = x.firstChild.data
                            entera = lista.ListaCircular()
                            entera.insertar(lista.Lista(e,None,None,k))
                            parcial.codigo = entera
                            parcial.codigo.imprimir1()
                        mat.codigo.insertar(parcial)
                    general.insertar(mat)
                print('hola') 
              
                
                print('\n--> El archivo fue cargado correctamente\n')  
                            
            elif n=='2': 
                print('-------------------Procesar Archivo------------------\n')
                           
            elif n=='3': 
                print('-------------------Escribir Archivo-------------------\n')
                            
            elif n=='4':
                print('----------------Datos Estudiantiles---------------------')
                print('\nCarné: 201903873')
                print('Nombre: Joaquin Emmanuel Aldair Coromac Huezo')
                print('Curso: Introducción a la Programación y Computación 2')
                print('Carrera: Ingenieria en Ciencias y Sistemas')
                print('5to Semestre')
                
            elif n=='5':
                print('----------------Generar Gráfica-------------------------')
                        
            elif n=='6':
                print('-----------------------Salir-----------------------------')
                
                print('\n----> Pulsa una tecla para salir\n')
                input("")
                sys.exit()
                    
            else:
                print ("No has pulsado una opción correcta")

      