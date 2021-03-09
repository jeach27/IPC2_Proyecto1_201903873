import sys
import tkinter
from tkinter import filedialog
import lista
from xml.dom import minidom
import os
import xml.etree.cElementTree as ET

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

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8').decode('utf8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

class proyect:
        
    def menu(self):
        general = lista.ListaCircular()
        cambiada = lista.ListaCircular()
        salida = lista.ListaCircular()
        posic = lista.ListaCircular()
        while True:
            print('\n----------------Menú principal--------------------')
            print('\n> Elija una opcion')
            print('\n1.Cargar Archivo\n2.Procesar Archivo\n3.Escribir Archivo Salida\n4.Mostrar Datos Estudiantes\n5.Generar Gráfica\n6.Salir')
            n=input('\n> Ingrese valor\n')
            if n=='1':
                print('----------------------Cargar Archivo------------------------')
                j = input('Ingrese ruta de archivo\n')
                archivo = minidom.parse(j)
                matrizz = archivo.getElementsByTagName('matriz')
                for matriz in matrizz:
                    nombre = matriz.getAttribute('nombre')
                    n = int(matriz.getAttribute('n'))
                    m = int(matriz.getAttribute('m'))
                    mat = lista.Lista(lista.ListaCircular(),nombre,n,m,None)
                    for i in range(n):
                        palabra=''
                        parcial = lista.Lista(palabra,None,i,None,None)
                        entera = lista.ListaCircular()
                        for k in range(m):
                            x = matriz.getElementsByTagName('dato')[i*m+k]
                            e = x.firstChild.data
                            entera.insertar(lista.Lista(e,None,None,k,None))
                        pal = entera.palabra()
                        parcial.codigo = pal
                        #print(parcial.codigo)
                        mat.codigo.insertar(parcial)
                    general.insertar(mat)
                    
                for matt in matrizz:
                    name = matt.getAttribute('nombre')
                    N = int(matt.getAttribute('n'))
                    M = int(matt.getAttribute('m'))
                    mate = lista.Lista(lista.ListaCircular(),name,N,M,None)
                    for h in range(N):
                        palabras = ''
                        parciales = lista.Lista(palabras,None,h,None,None)
                        enteras = lista.ListaCircular()
                        for q in range(M):
                            y = matt.getElementsByTagName('dato')[h*M+q]
                            z = y.firstChild.data
                            enteras.insertar(lista.Lista(z,None,None,q,None))
                        pala = enteras.palabra()
                        parciales.codigo = pala
                        mate.codigo.insertar(parciales)
                    cambiada.insertar(mate)

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
                            e = matrizBinaria(filaa)
                            nodo1.Lista.codigo = e
                            #print(nodo1.Lista.codigo)
                            nodo1 = nodo1.next
                        nodo = nodo.next

                    nodo = cambiada.head
                    pos = lista.ListaCircular()
                    for _ in range(cambiada.size):
                        nam = nodo.Lista.nombre
                        #print(nam)
                        print('<Calculando posiciones>')
                        
                        nodo1 = nodo.Lista.codigo.head
                        for _ in range(nodo.Lista.codigo.size):
                            fil = nodo1.Lista.codigo
                            if fil == 0:
                                nodo1 = nodo1.next
                            else:
                                posiciones = lista.ListaCircular()
                                nodo2 = nodo.Lista.codigo.head
                                for _ in range(nodo.Lista.codigo.size):
                                    fill = nodo2.Lista.codigo
                                    if fil == fill:
                                        if _ != posiciones.ultimo():
                                            if fill != '0':
                                                posiciones.insertar(lista.Lista(str(_),nam,None,None,None))
                                                nodo2.Lista.codigo = '0'
                                    nodo2 = nodo2.next
                                
                                if posiciones.size != 0:
                                    #posiciones.imprimir1()
                                    pos.insertar(lista.Lista(posiciones,nam,None,None,None))
                                nodo1 = nodo1.next
                        nodo = nodo.next
                        posic.insertar(lista.Lista(pos, nam, None, None,None))
                        

                    nodo = general.head
                    nodop = posic.head
                    for _ in range(general.size):
                        nomb = nodo.Lista.nombre
                        nombr = nodop.Lista.nombre
                        if nomb == nombr:
                            print('<Realizando Suma de Tuplas>')
                            nodo2 = nodo.Lista.codigo.head
                            nodo2p = nodop.Lista.codigo.head
                            for _ in range(nodo.Lista.codigo.size):
                                pass
                                 
                            nodo = nodo.next
                            nodop = nodop.next
                        else:
                            nodo = nodo.next

            elif n=='3': 
                print('-------------------Escribir Archivo-------------------\n')
                if general.head is None:
                    print('No se a cargado ningun archivo')
                else:
                    matrices = ET.Element('matrices')
                    nodo = general.head
                    nodop = posic.head
                    for _ in range(posic.size):
                        name = nodo.Lista.nombre
                        columnas = nodo.Lista.m
                        filas = nodo.Lista.n
                        posiciones = nodop.Lista.codigo.size
                        matriz = ET.SubElement(matrices, 'matriz', nombre=name, n=str(filas), m=str(columnas), g=str(posiciones))
                        nodo = nodo.next
                        nodop = nodop.next    
                        '''nodo1 = nodo.Lista.codigo.head
                        for _ in range(nodo.Lista.codigo.size):
                            filaa = nodo1.Lista.codigo
                            fila = nodo1.Lista.n
                            #print(filaa + str(fila))
                            nodo1 = nodo1.next'''
                        
                    arbol = prettify(matrices)
                    f = open('salida.xml','w')
                    f.write(arbol)
                    f.close()
                    print('Archivo de salida = '+'salida.xml')
                            
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

      