
class Nodo:
    def __init__(self,next=None, valor=None,prev=None):
        self.next=next
        self.valor=valor
        self.prev=prev
    def __str__(self):
        return self.valor
class ListaDoble:
    def __init__(self):
        self.head=None
        self.largo=0
        self.tail=None
    def printL(self):
        nodo=self.head
        result="["
        if nodo==None:
            result="[]"
        while nodo!=None:
            result+=str(nodo.__str__())
            nodo=nodo.next

            if nodo!=None:
                result+=","
            if nodo==None:
                result+="]"
        print (result)
    def appe(self,value):
        self.largo+=1
        if self.head==None:
            self.head=Nodo(valor=value)
            self.tail=self.head
        else:
            temp=self.tail
            nodo=Nodo(valor=value)
            temp.next=nodo
            nodo.prev=temp
            self.tail=nodo


    def rprintL(self):
        nodo=self.tail
        result="["
        if nodo==None:
            result=="[]"
        while nodo!=None:
            result+=str(nodo.__str__())
            nodo=nodo.prev
            if nodo!=None:
                result+=","
            elif nodo ==None:
                result+="]"
        print (result)

    def dele(self,valor):
        self.largo-=1
        nodo=self.head
        if self.largo<=-1:
            None
            self.largo=0
        elif self.largo>-1:
            if nodo.valor==valor:
                self.head=nodo.next  
            while nodo.valor!=valor:
                temp=nodo.next 
                if temp.valor==valor:
                     nodo.next=temp.next
                     break
                else:
                    nodo=nodo.next

    def insert(self,valores,pos):
        if pos>self.largo:
            return "Fuera de lista"
        nodo=self.head
        i=0
        while i!=pos-1:
            
            nodo=nodo.next
            i+=1
        self.largo+=1
        
        new=Nodo(valor=valores)
        new.next=nodo.next
        nodo.next=new
        
            
lista=ListaDoble()
        
            
