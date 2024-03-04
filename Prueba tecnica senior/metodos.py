import csv
from tkinter import messagebox

from Rankin import Ranking


class Metodos :

 
    def leer_archivo(lista: list, ruta):
        with open(ruta, encoding='utf-8') as f :
            reader = csv.reader(f)
            messagebox.showinfo("mensaje","se leyo correctamente el archivo")
            filas =""
            requisito=[]
            for row in reader :
                    
                    
                    try:
                        rankin = row[0]
                        item = row[1]
                        nombre = row[2]
                        stars  = row[3]
                        forks =  row[4]
                        lenguaje=row[5]
                        repo_url =  row[6]
                        username =  row[7]
                        issues = row[8]
                        last_commit = row[9]
                        desciption = row[10]

             
                      
                        rank = Ranking(rankin, item, nombre, stars, forks,lenguaje, repo_url, username, issues, last_commit,desciption )
                        lista.append(rank)
                        #messagebox.showinfo("mensaje","se agrego el contenido del archivo correctamente a la lista")
                    except:
                          messagebox.showerror("error","has escrito un paremetro fuera del tipo") 
    def filtro_nuemro(lista:list, numero):
        contador=0
        listafiltro=[]
        for dato in lista:
            
            if contador==numero:
                
                break
            else:
                listafiltro.append(dato)
            

            contador+=1
        return listafiltro


    def filtro(lista:list, numero, lenguaje):
        listaprov=[]
        lista_filtro=[]
        rank:Ranking
        for rank in lista:
            if rank.lenguaje==lenguaje:
                listaprov.append(rank)
        #for ele in listaprov:
           # print(ele.lenguaje)
        lista_filtro= Metodos.filtro_nuemro(listaprov,numero)
        return lista_filtro

       


