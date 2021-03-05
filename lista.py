
class Lista:
    def __init__(self, codigo, nombre, n, m, g):
        self.codigo = codigo
        self.nombre = nombre
        self.n = n
        self.m = m
        
class Nodo:
    def __init__(self, Lista=None, next = None):
        self.Lista = Lista
        self.next = next

class ListaCircular:
    def __init__(self, head=None):
        self.head = head
        self.size = 0
    
    def insertar(self, valor):
        new_nodo = Nodo(Lista = valor, next = self.head)
        if self.size == 0:
            self.head = new_nodo
            new_nodo.next = self.head
        else:
            cur = self.head
            while cur.next is not self.head:
                cur = cur.next
            cur.next = new_nodo
            new_nodo.next = self.head
        self.size +=1

    def palabra(self):
        if self.head is None:
            return
        aux = self.head
        palabra=''
        palabra = palabra + aux.Lista.codigo
        while aux.next != self.head:
            aux = aux.next
            palabra = palabra + aux.Lista.codigo
            
        return palabra
       
    def imprimir(self):
        if self.head is None:
            return
        Nodo = self.head
        print('\n'+Nodo.Lista.codigo)
        while Nodo.next != self.head:
            Nodo = Nodo.next
            print( '\n'+Nodo.Lista.codigo)

    def imprimir1(self):
        if self.head is None:
            return
        Nodo = self.head
        print('\n'+Nodo.Lista.codigo , end = "=>")
        while Nodo.next != self.head:
            Nodo = Nodo.next
            if Nodo.next == self.head:
                print(Nodo.Lista.codigo+'\n')
            else:
                print( Nodo.Lista.codigo  , end = "=>")
    
    def ultimo(self):
        if self.head is None:
            return
        Nodo = self.head
        while Nodo != self.head:
            if Nodo.next == self.head:
                return Nodo.Lista.codigo

    def eliminar(self, dato):
        if self.head is None:
            return
        elif dato == self.head.Lista.codigo:
            Nodo = self.head
            while Nodo.next != self.head:
                Nodo = Nodo.next
            Nodo.next = self.head.next
            self.head = self.head.next
        else:
            Nodo = self.head
            pre = None
            while Nodo.Lista.codigo != dato:
                pre = Nodo
                Nodo = Nodo.next
            pre.next = Nodo.next


    



    
