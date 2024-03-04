
from tkinter import filedialog, messagebox
from metodos import Metodos
from Rankin import Ranking

listafiltro=[]
lista=[]
metodo=Metodos

def cargar():
       try:
               file = filedialog.askopenfilename(title="abrir", filetypes=(("csv files","*.csv"),("lfp files", "*.lfp"),("all files", "*.*")))
               metodo.leer_archivo(lista, file)
       except:
               messagebox.showerror("error","El contenido del archivo no es valido o  no has selecionado un archivo")  
dato:Ranking
cargar()
#for dato in lista:
    #print(dato.lenguaje)


rankin=int(input("ingrese el numero N de rankin \n"))
lenguaje=input("ingrese el lenguaje a filtrar \n")
#print(rankin)
def filtro(rankin, lista, lenguaje):
    rank:Ranking
    contador=1
    coma=","
    listafiltro=metodo.filtro(lista,rankin,lenguaje)
    for rank in listafiltro:
        print(contador,",",rank.lenguaje,",",rank.repo_name,coma,rank.stars,coma,rank.forks,coma,rank.last_commit,coma, rank.desciption)
        contador+=1
filtro(rankin,lista,lenguaje)