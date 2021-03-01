import sys
import tkinter
from tkinter import filedialog
import lista
from xml.dom import minidom
import os

def leerArchivo():
    archivo = filedialog.askopenfilename(title = 'Cargar Archivo', filetypes = (('xml files','*.xml'),('all files','*.')))
    return archivo  

def matrizBinaria(fila):
    for i in range(1,10):
        fila = fila.replace(str(i),'1')
    return fila

def crearNodo(identificador, nombre , shape):
    return identificador + '[label="'+ nombre +'",shape="'+ shape +'"]\n'

def unirNodo(NodoA ,NodoB):
    return NodoA + '->' + NodoB + '\n'

def ReconstruirFila(fila):
    nueva = list()
    for letra in fila:
        nueva.append(letra)
    retorno = " | ".join(nueva)
    final = '{ { '+ retorno +' } }'
    return final

class proyect:
        
    def menu(self):
        general = lista.ListaCircular()
        cambiada = lista.ListaCircular()
        while True:
            print('\n----------------Menú principal--------------------')
            print('\n> Elija una opcion')
            print('\n1.Cargar Archivo\n2.Procesar Archivo\n3.Escribir Archivo Salida\n4.Mostrar Datos Estudiantes\n5.Generar Gráfica\n6.Salir')
            n=input('\n> Ingrese valor\n')
            if n=='1':
                print('----------------------Cargar Archivo------------------------')
                j = input('Ingrese ruta de archivo')
                archivo = minidom.parse(j)
                matrizz = archivo.getElementsByTagName('matriz')
                for matriz in matrizz:
                    nombre = matriz.getAttribute('nombre')
                    n = int(matriz.getAttribute('n'))
                    m = int(matriz.getAttribute('m'))
                    mat = lista.Lista(lista.ListaCircular(),nombre,n,m)
                    for i in range(m):
                        palabra=''
                        parcial = lista.Lista(palabra,None,i,None)
                        entera = lista.ListaCircular()
                        for k in range(n):
                            x = matriz.getElementsByTagName('dato')[i*m+k]
                            e = x.firstChild.data
                            entera.insertar(lista.Lista(e,None,None,k))
                        pal = entera.palabra()
                        parcial.codigo = pal
                        #print(parcial.codigo)
                        mat.codigo.insertar(parcial)
                    general.insertar(mat)

                for matri in matrizz:
                    Name = matri.getAttribute('nombre')
                    N = int(matri.getAttribute('n'))
                    M = int(matri.getAttribute('m'))
                    matt = lista.Lista(lista.ListaCircular(),Name,N,M)
                    for i in range(M):
                        palabras=''
                        parciales = lista.Lista(palabras,None,i,None)
                        enteras = lista.ListaCircular()
                        for k in range(N):
                            y = matri.getElementsByTagName('dato')[i*M+k]
                            p = y.firstChild.data
                            enteras.insertar(lista.Lista(p,None,None,k))
                        pal = enteras.palabra()
                        parciales.codigo = pal
                        #print(parcial.codigo)
                        matt.codigo.insertar(parcial)
                    cambiada.insertar(matt)
                    

                print('\n--> El archivo fue cargado correctamente\n')  
            
            elif n=='2': 
                print('-------------------Procesar Archivo------------------\n')
                
                if cambiada.head is None:
                    print('No se a cargado ningun archivo')
                else:
                    
                    nodo = cambiada.head
                    for _ in range(cambiada.size):
                        name = nodo.Lista.nombre
                        columnas = nodo.Lista.m
                        filas = nodo.Lista.n
                        print('<Calculando Matriz Binaria>')
                        nodo1 = nodo.Lista.codigo.head
                        for _ in range(nodo.Lista.codigo.size):
                            filaa = nodo1.Lista.codigo
                            fila = nodo1.Lista.n
                            e = matrizBinaria(filaa)
                            nodo1.Lista.codigo = e
                            nodo1 = nodo1.next
                        nodo = nodo.next
      
            elif n=='3': 
                print('-------------------Escribir Archivo-------------------\n')
                if general.head is None:
                    print('No se a cargado ningun archivo')
                else:
                    nodo = general.head
                    for _ in range(general.size):
                        name = nodo.Lista.nombre
                        columnas = nodo.Lista.m
                        filas = nodo.Lista.n
                        print(name + str(columnas) + str(filas))
                        nodo1 = nodo.Lista.codigo.head
                        for _ in range(nodo.Lista.codigo.size):
                            filaa = nodo1.Lista.codigo
                            fila = nodo1.Lista.n
                            print(filaa + str(fila))
                            nodo1 = nodo1.next
                        nodo = nodo.next
                            
            elif n=='4':
                print('----------------Datos Estudiantiles---------------------')
                print('\nCarné: 201903873')
                print('Nombre: Joaquin Emmanuel Aldair Coromac Huezo')
                print('Curso: Introducción a la Programación y Computación 2')
                print('Carrera: Ingenieria en Ciencias y Sistemas')
                print('5to Semestre')
                
            elif n=='5':
                print('----------------Generar Gráfica-------------------------')
                if general.head is None:
                    print('No se a cargado ningun archivo')
                else:
                    print('--------------Matrices---------------')
                    nodo = general.head
                    for _ in range(general.size):
                        nombre = nodo.Lista.nombre
                        print(str(_+1)+'. '+nombre)
                        nodo = nodo.next
                    
                    graficar = input('Ingrese valor de matriz a graficar\n')
                    if int(graficar) > general.size:
                        print('No has pulsado una opcion correcta\n')
                    else:
                        file = open('grafo.dot','w')
                        file.write('digraph G{\n')
                        file.write('A[label="Matrices", shape="circle"]\n')

                        nodo = general.head
                        for _ in range(general.size):
                            name = nodo.Lista.nombre
                            n = nodo.Lista.n
                            m = nodo.Lista.m
                            if graficar == str(_+1):
                                file.write(crearNodo(str(nodo),str(name),"circle"))
                                if n == m:
                                    file.write(crearNodo(str(n)+str(m),"n="+str(n)+" "+"m="+str(m),"box"))
                                else:
                                    file.write(crearNodo(str(n),"n="+str(n),"box"))
                                    file.write(crearNodo(str(m),"m="+str(m),"box"))
                            nodo = nodo.next

                        nodo = general.head
                        for _ in range(general.size):
                            name = nodo.Lista.nombre
                            n = nodo.Lista.n
                            m = nodo.Lista.m
                            if graficar == str(_+1):
                                nodo1 = nodo.Lista.codigo.head
                                for _ in range(nodo.Lista.codigo.size):
                                    filaa = nodo1.Lista.codigo
                                    fila = nodo1.Lista.n
                                    file.write(crearNodo(str(fila)+str(m)+str(n),ReconstruirFila(filaa),"Mrecord"))
                                    nodo1 = nodo1.next
                            nodo = nodo.next

                        nodo = general.head
                        for _ in range(general.size):
                            n = nodo.Lista.n
                            m = nodo.Lista.m
                            if graficar == str(_+1):
                                file.write(unirNodo("A",str(nodo)))
                                if n == m:
                                    file.write(unirNodo(str(nodo),str(n)+str(m)))
                                else:
                                    file.write(unirNodo(str(nodo),str(n)))
                                    file.write(unirNodo(str(nodo),str(m)))
                            nodo = nodo.next
                            
                        nodo = general.head
                        for _ in range(general.size):
                            n = nodo.Lista.n
                            m = nodo.Lista.m
                            if graficar == str(_+1):
                                nodo1 = nodo.Lista.codigo.head
                                for _ in range(nodo.Lista.codigo.size):
                                    filaa = nodo1.Lista.codigo
                                    fila = nodo1.Lista.n
                                    if _ == 0:
                                        file.write(unirNodo(str(nodo), str(fila)+str(m)+str(n)))
                                    else:
                                        anterior = fila-1
                                        file.write(unirNodo(str(anterior)+str(m)+str(n),str(fila)+str(m)+str(n)))
                                    nodo1 = nodo1.next
                            nodo = nodo.next
                            
                        file.write('}')
                        file.close()
                        os.system('dot -Tpng grafo.dot -o grafo.jpg')
                        os.startfile('grafo.jpg')    

            elif n=='6':
                print('-----------------------Salir-----------------------------')
                
                print('\n----> Pulsa una tecla para salir\n')
                input("")
                sys.exit()
                    
            else:
                print ("No has pulsado una opción correcta")

      