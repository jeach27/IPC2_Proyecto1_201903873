
class Lista:
    def __init__(self, codigo):
        self.codigo = codigo
        
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
        print(Nodo.Lista.codigo , end = "\n")
        while Nodo.next != self.head:
            Nodo = Nodo.next
            print( Nodo.Lista.codigo  , end = "\n")

    
