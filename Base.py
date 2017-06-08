import os
import time
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import winsound
from threading import Thread
import threading
class Vagon:
    def __init__(self,next=None, valor=None,prev=None):
        self.next=next
        self.valor=valor
        self.prev=prev
    def __str__(self):
        return self.valor
class Tren:
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

            
tren=Tren()
def cargarimagen(nombre):
    ruta = os.path.join("imagenes",nombre)
    imagen = PhotoImage(file=ruta)
    return imagen
def ayuda():
    #ventana ayuda
    ventana_menu.withdraw()
    ventanaayuda = Toplevel()
    ventanaayuda.title("Ayuda")
    ventanaayuda.geometry("400x300+400+200")
    ventanaayuda.resizable(width=NO,height=NO)
    #canvas de la ayuda
    contenedor_ayuda=Canvas(ventanaayuda,width=400,height=300,bg="#ffffff")
    contenedor_ayuda.place(x=0,y=0)
    #label de ayuda
    ayuda=Label(contenedor_ayuda,bg="#896532",width=400,height=300)
    ayuda.place(x=0,y=0)
    #destruye la ventana y abre la principal
    def regresar():
        ventanaayuda.destroy()
        ventana_menu.deiconify()
    #boton regresar
    botonR=Button(contenedor_ayuda,command=regresar,text="Regresar",width=10,height=3,bg="#ffffff")
    botonR.place(x=1,y=1)
    mainloop()
def simulacion():
    #ventana simulación
    ventana_menu.withdraw()
    ventanasimu = Toplevel()
    ventanasimu.title("Simulacion")
    ventanasimu.geometry("1200x600+75+50")
    ventanasimu.resizable(width=NO,height=NO)
    #canvas de la simulación
    contenedor_simu=Canvas(ventanasimu,width=1200,height=600,bg="#ffffff")
    contenedor_simu.place(x=0,y=0)
    #label de la simulación
    ayuda=Label(contenedor_simu,bg="#896532",width=800,height=700)
    ayuda.place(x=0,y=0)
    #destruye la ventana y abre la principal
    def regresar():
        ventanasimu.destroy()
        ventana_menu.deiconify()
    #boton regresar
    botonR=Button(contenedor_simu,command=regresar,text="Regresar",width=10,height=3,bg="#ffffff")
    botonR.place(x=1,y=1)
    mainloop()
def horarios():
    #ventana horario
    ventana_menu.withdraw()
    ventanahora = Toplevel()
    ventanahora.title("Horarios")
    ventanahora.geometry("400x300+400+200")
    ventanahora.resizable(width=NO,height=NO)
    #canvas del horario
    contenedor_hora=Canvas(ventanahora,width=400,height=300,bg="#ffffff")
    contenedor_hora.place(x=0,y=0)
    #label de horario
    ayuda=Label(contenedor_hora,bg="#896532",width=400,height=300)
    ayuda.place(x=0,y=0)
    combo=ttk.Combobox(contenedor_hora)
    combo.place(x=100,y=0)
    combo["values"]=("6:00","7:00","8:00","9:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00")
    #destruye la ventana y abre la principal
    def regresar():
        ventanahora.destroy()
        ventana_menu.deiconify()
    #boton regresar
    botonR=Button(contenedor_hora,command=regresar,text="Regresar",width=10,height=3,bg="#ffffff")
    botonR.place(x=1,y=1)
    mainloop()
#ventana menu
ventana_menu=Tk()
ventana_menu.title("menu")
ventana_menu.geometry("400x400+400+50")
ventana_menu.resizable(width=NO,height=NO)
#contenedor principal
imagen=cargarimagen("menu.gif")
contenedor_principal=Canvas(ventana_menu,width=400,height=400,bg="#657392")
contenedor_principal.place(x=0,y=0)
#Label de menu
imagen=cargarimagen("menu.gif")
menu=Label(contenedor_principal,image=imagen,bg="#896532",width=500,height=500)
menu.place(x=0,y=0)
#boton Iniciar simulacion
botonhelp=Button(contenedor_principal,command=simulacion,text="iniciar",width=10,height=3,bg="#ffffff")
botonhelp.place(x=80,y=320)
#boton horarios
botonhelp=Button(contenedor_principal,command=horarios,text="Horarios",width=10,height=3,bg="#ffffff")
botonhelp.place(x=310,y=5)
#boton ayuda
botonhelp=Button(contenedor_principal,command=ayuda,text="Ayuda",width=10,height=3,bg="#ffffff")
botonhelp.place(x=230,y=320)
mainloop()
