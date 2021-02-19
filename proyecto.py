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
                    parcial = lista.ListaCircular()
                    entera = lista.ListaCircular()
                    nombre = matriz.getAttribute('nombre')
                    n = matriz.getAttribute('n')
                    m = matriz.getAttribute('m')
                    y = int(n)*int(m)
                    entera.insertar(lista.Lista(nombre))
                    entera.insertar(lista.Lista(n))
                    entera.insertar(lista.Lista(m))
                    entera.imprimir()
                    for dat in range(0, y):
                        entera1 = lista.ListaCircular()
                        x = archivo.getElementsByTagName('dato')[dat]
                        e = x.firstChild.data
                        entera1.insertar(lista.Lista(e))
                        parcial.insertar(lista.Lista(entera1))
                        entera1.imprimir()
                        
                    parcial.insertar(lista.Lista(entera))
                    general.insertar(lista.Lista(parcial))
                    
                


                      
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

      