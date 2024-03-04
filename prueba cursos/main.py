from tkinter import filedialog
from clase_curso import *
from metodos import*
from PyQt5 import QtCore
from PyQt5 import QtWidgets, uic

#iniciar aplicacion
app = QtWidgets.QApplication([])

#cargar ventanas
menu = uic.loadUi("menu.ui")
agregar_c =uic.loadUi("agregar_curso.ui")
gestion = uic.loadUi("gestion.ui")
eliminar= uic.loadUi("eliminar.ui")
editar=uic.loadUi("editar_curso.ui")
mostar=uic.loadUi("mostrar.ui")
contarui=uic.loadUi("contar.ui")
#inicializa la lista y metodos
lista=[]
metodo = metodos
def cargar():
       try:
               file = filedialog.askopenfilename(title="abrir", filetypes=(("csv files","*.csv"),("lfp files", "*.lfp"),("all files", "*.*")))
               metodo.leer_archivo(lista, file)
       except:
               messagebox.showerror("error","El contenido del archivo no es valido o  no has selecionado un archivo")  
      
menu.setWindowFlag(QtCore.Qt.FramelessWindowHint)
agregar_c.setWindowFlag(QtCore.Qt.FramelessWindowHint)
gestion.setWindowFlag(QtCore.Qt.FramelessWindowHint)
eliminar.setWindowFlag(QtCore.Qt.FramelessWindowHint)
editar.setWindowFlag(QtCore.Qt.FramelessWindowHint)
mostar.setWindowFlag(QtCore.Qt.FramelessWindowHint)
contarui.setWindowFlag(QtCore.Qt.FramelessWindowHint)

def cerrar_v():
       menu.close()
def ir_gestion():
       menu.hide()
       gestion.show()
def ir_conar():
       menu.hide()
       contarui.show()
#metodos de la ventana gestion
def ir_ingresarcurso():
       gestion.hide()
       agregar_c.show()
def ir_de_gestion_a_menu():
       gestion.hide()
       menu.show()
def ir_de_gestion_a_eliminar():
       gestion.hide()
       eliminar.show()
def ir_de_gestion_a_editar():
       gestion.hide()
       editar.show()
def ir_de_gestion_a_mostrar():
       gestion.hide()
       mostar.show()
#metodos de la ventana agregar curso
def ir_de_agregarcurso_a_gestion():
       agregar_c.hide()
       gestion.show()
#metodos de la ventana eliminar
def ir_de_eliminar_a_gestion():
       eliminar.hide()
       gestion.show()
#metodos de editar
def ir_de_editar_a_gestion():
       editar.hide()
       gestion.show()
#metodos de mostrar
def ir_de_mostrar_a_gestion():
       mostar.hide()
       gestion.show()
#metodos de contar
def ir_de_contar_a_menu():
       contarui.hide()
       menu.show()

#metodo agregar curso de la ventana agregar
def agregar_curso_agregar():
       #QlineEdit de agregar curso
       codigo_agregar=agregar_c.lineEdit_codigo.text()
       if codigo_agregar=='':
              int_codigo_agregar=0
       else:
              try:
                     int_codigo_agregar=int(codigo_agregar)
              except:
                    messagebox.showerror("error","has escrito un paremetro fuera del tipo") 
              

       nombre_agregar= agregar_c.lineEdit_nombre.text()
       requisito_agregar=agregar_c.lineEdit_requisito.text()
       try:
              opcion_agregar=int(agregar_c.lineEdit_opcion.text())
              if opcion_agregar==1 or opcion_agregar==0 :
                     oblii=opcion_agregar
              else:
                  messagebox.showinfo("info","la opcion es 0 o 1")   
              semestre_agregar=int(agregar_c.lineEdit_semestre.text())
              creditos_agregar=int(agregar_c.lineEdit_creditos.text())
              estado_agregar=int(agregar_c.lineEdit_estado.text())
              if estado_agregar==1 or estado_agregar==0 or estado_agregar==-1:
                     est=estado_agregar
              else:
                     messagebox.showinfo("info","la opcion es 0 o 1 0 -1")
       except:
              messagebox.showerror("error","has escrito un paremetro fuera del tipo") 

       try:
              curso_agregar= curso(int_codigo_agregar,nombre_agregar,requisito_agregar, oblii, semestre_agregar, creditos_agregar, est )
              metodo.igresar_curso(lista, curso_agregar)
              messagebox.showinfo("mensaje", "curso agregado con exito")
       except:
              messagebox.showerror("error","has escrito un paremetro fuera del tipo")
#metodo que elimina el curso de la lista
def eliminar_eliminar():
       try:
              codigo_eliminar= int(eliminar.lineEdit_codigo.text())
              metodo.eliminar_elemento(lista, codigo_eliminar) 
              messagebox.showinfo("mensaje", "curso eliminado con exito")
              eliminar.lineEdit_codigo.setText("")
       except:
              messagebox.showerror("error","has escrito un paremetro fuera del tipo")
#metodo que muestra un curso en especifico de la lista
def mostrar_a_():
       
       try:
              codigo_mostrar = int(editar.lineEdit.text()) 
              metodo.mostrar_enLineEdit(lista, codigo_mostrar,editar)
                  
             
       except :
              messagebox.showerror("error","has escrito un paremetro fuera del tipo o el codigo no existe")
#metodo que edita un curso en la lista
def editar_a():
       try: 
              existe=False
              codigo_editar = int(editar.lineEdit.text())
              metodo.editar_lista(lista,codigo_editar,editar)
              
            
       except:
              messagebox.showerror("error","has escrito un paremetro fuera del tipo o el codigo no existe")
                   
#metodo que llena los elementoss de una tabla con los elemmentos de la lista
def llenar_tabla():
       try:
              mostar.tble.setColumnWidth(1,300)
              mostar.tble.setColumnWidth(2,250)
              row=0
       
              mostar.tble.setRowCount(len(lista))
              for x in lista:
                     if len(str(x.codigo))==1:
                            numero1=""
                            numero1=str(x.codigo)
                            numerot=str("00")
                            numeroq=numerot+numero1
                            mostar.tble.setItem(row, 0, QtWidgets.QTableWidgetItem(numeroq))
                            
                     elif len(str(x.codigo))==2:
                            numero2=""
                            numero2=str(x.codigo)
                            numeror=str("0")
                            numere4=numeror+numero2
                            mostar.tble.setItem(row, 0, QtWidgets.QTableWidgetItem(numere4))
                            
                     else:
                           mostar.tble.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x.codigo))) 
                          
                     mostar.tble.setItem(row, 1, QtWidgets.QTableWidgetItem(x.curso))
                     mostar.tble.setItem(row, 2, QtWidgets.QTableWidgetItem(x.requisito))
                     mostar.tble.setItem(row, 3, QtWidgets.QTableWidgetItem(str(x.obligatorio)))
                     mostar.tble.setItem(row, 4, QtWidgets.QTableWidgetItem(str(x.semestre)))
                     mostar.tble.setItem(row, 5, QtWidgets.QTableWidgetItem(str(x.creditos)))
                     mostar.tble.setItem(row, 6, QtWidgets.QTableWidgetItem(str(x.estado)))
                     row=row+1

       
       except:
               messagebox.showerror("error","no se pueden mostrar elmentos vacios")

def editar_labels():
       try:
               metodo.contar_creditos_aprobados(lista, contarui)
               metodo.contar_creditos_cursando(lista, contarui)
               metodo.contar_creditos_pendientes(lista, contarui)
       except:
              messagebox.showerror("error","no se pueden contar elmentos vacios")
      
def editar_label_semestre():
     try:

       numsem = contarui.lineEdit_numsem.text()
       if numsem == '':
              numint=0
       else:
          numint=int(numsem)   
       metodo.contar_creditos_porSemestre(lista,contarui, numint)
     except:
       messagebox.showerror("error","no se pueden contar elmentos vacios")
def editar_label_semestreN():

       try:
           numN=int(contarui.lineEdit_numseN.text())
           encontrado=False
           for x in lista:
              if x.semestre==numN:
                     encontrado=True
                     break
           if encontrado==True:
                     metodo.contar_creditos_porSemestreN(lista,contarui,numN)
                     messagebox.showinfo("info","semestre correcto")
           else:
              messagebox.showerror("error","el semestre no existe en la lista")
       except:
              messagebox.showerror("error","no se pueden contar elmentos vacios")
     
      

    
  
           

#botones menu principal
menu.bt_cargar.clicked.connect(cargar)
menu.bt_cerrar.clicked.connect(cerrar_v)
menu.bt_gestionar.clicked.connect(ir_gestion)
menu.bt_contar.clicked.connect(ir_conar)
#botones gestion
gestion.bt_agregar.clicked.connect(ir_ingresarcurso)
gestion.bt_regresar.clicked.connect(ir_de_gestion_a_menu)
gestion.bt_eliminar.clicked.connect(ir_de_gestion_a_eliminar)
gestion.bt_editar.clicked.connect(ir_de_gestion_a_editar)
gestion.bt_listar.clicked.connect(ir_de_gestion_a_mostrar)
#botones agregar curso
agregar_c.bt_regresar.clicked.connect(ir_de_agregarcurso_a_gestion)

agregar_c.btn_agregar.clicked.connect(agregar_curso_agregar)
#botones eliminar curso
eliminar.bt_regresar.clicked.connect(ir_de_eliminar_a_gestion)
eliminar.btn_eliminar.clicked.connect(eliminar_eliminar)
#botones de editar
editar.pushButton.clicked.connect(mostrar_a_)
editar.bt_regresar.clicked.connect(ir_de_editar_a_gestion)
editar.btn_editar.clicked.connect(editar_a)
#botones de mostrar
mostar.bt_regresar.clicked.connect(ir_de_mostrar_a_gestion)
mostar.btn_mostrar.clicked.connect(llenar_tabla)
#botones de contar
contarui.btn_actualizar.clicked.connect(editar_labels)
contarui.btn_validar.clicked.connect(editar_label_semestre)
contarui.bt_regresar.clicked.connect(ir_de_contar_a_menu)
contarui.btn_validarN.clicked.connect(editar_label_semestreN)
menu.show()
app.exec()

