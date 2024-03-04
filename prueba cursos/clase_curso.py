import csv
from tkinter import messagebox


class curso :
    def __init__(self, codigo, curso, requisito, obligatorio, semestre, creditos, estado) :

        self.codigo = codigo
        self.curso = curso
        self.requisito = requisito
        self.obligatorio = obligatorio
        self.semestre = semestre
        self.creditos = creditos
        self.estado = estado

    def set_codigo(self, nuevo_codigo):
        self.codigo = nuevo_codigo
    def set_curso(self, nuevo_curso):
        self.curso = nuevo_curso
    def set_requisito(self, nuevo_requisito):
        self.requisito = nuevo_requisito
    def set_obligatorio(self, nuevo_obligatorio):
        self.obligatorio = nuevo_obligatorio
    def set_semestre(self, nuevo_semestre):
        self.semestre = nuevo_semestre
    def set_creditos(self, nuevo_creditos):
        self.creditos = nuevo_creditos
    def set_estado(self, nuevo_estado):
        self.estado = nuevo_estado    



def igresar_curso ( lista,  curso):
    numero=int(curso.codigo)
    existe = False

    if not lista:
        lista.append(curso)
        
    else:   
            for x in lista:
                nux=int(x.codigo)
               
                    
                if nux == numero:
                    existe = True
                    lista.remove(x)
                    lista.append(curso)
                    break 

            if existe == False:
                lista.append(curso)

def eliminar_elemento (lista, codigo): 
    numero=int(codigo)
    existe = False

    if not lista:
        messagebox.showerror("error","no se puede eliminar elementos vacios ")
    else:   
            for x in lista:
                nux=int(x.codigo)
               
                    
                if nux == numero:
                    existe = True
                    lista.remove(x)
                    break 

            if existe == False:
                 messagebox.showerror("error","el codigo del curso que desea eleminar no esta en la lista")           
              
                    
         
      


    
def leer_archivo(lista, ruta):
    with open(ruta) as f:
        reader = csv.reader(f, delimiter=",")
        messagebox.showinfo("mensaje","se leyo correctamente el archivo")
        filas =""
        for row in reader :
            codigo = row[0]
            curs = row[1]
            requisito = row[2]
            obligatorio  = int(row[3]) 
            semestre  = int(row[4])
            creditos  = int(row[5])
            estado  = int(row[6])
            cur = curso(codigo, curs, requisito, obligatorio, semestre, creditos, estado )
            try:
                igresar_curso(lista, cur)
                messagebox.showinfo("mensaje","se agrego el contenido del archivo correctamente a la lista")
            except:
                messagebox.showerror("error","error al leer el archivo porfavor ingrese valores validos")

#leer_archivo(lista,'cursos.csv')   
    
       
   
  
#k=0
#curso1 = curso("101", "fisica", 25, 1, 2, 4, 1)
#try: 
#    igresar_curso(lista, curso1)
#    messagebox.showinfo("mensaje","se agrego el curso correctamente a la lista")
#except:
#    messagebox.showerror("error","el codigo del curso ingresado no es valido ")


#print (lista[1].creditos)



#eliminar_elemento(lista, 101)
#while k < len(lista):       
#        print(lista[k].codigo, lista[k].curso, lista[k].requisito, lista[k].obligatorio, lista[k].semestre, lista[k].creditos, lista[k].estado)
#        k+=1
#num =len(lista)
#print ("el numero es : ", num)
