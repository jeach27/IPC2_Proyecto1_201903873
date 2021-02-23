
class Lista:
    def __init__(self, codigo, nombre, n, m):
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
        if self.size == 0:
            self.head = Nodo(Lista = valor )
            self.head.next = self.head
        else:
            new_nodo = Nodo(Lista = valor, next = self.head.next)
            self.head.next = new_nodo
        self.size +=1

    def imprimir (self):
        if self.head is None:
            return
        Nodo = self.head
        print('\n'+Nodo.Lista.codigo)
        while Nodo.next != self.head:
            Nodo = Nodo.next
            print( '\n'+Nodo.Lista.codigo)

    def imprimir1 (self):
        if self.head is None:
            return
        Nodo = self.head
        print(Nodo.Lista.codigo , end = "=>")
        while Nodo.next != self.head:
            Nodo = Nodo.next
            print( Nodo.Lista.codigo  , end = "=>")

    
