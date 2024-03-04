from clase_curso import*
class metodos:
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
        with open(ruta, encoding='utf-8') as f :
            reader = csv.reader(f)
            messagebox.showinfo("mensaje","se leyo correctamente el archivo")
            filas =""
            requisito=[]
            for row in reader :
                    
                    
                    try:
                        curs = row[1]
                        codigo = row[0]
                        requisito = row[2]
                        obligatorio  = int(row[3])

             
                        semestre  = int(row[4])
                        creditos  = int(row[5])
                        estado  = int(row[6])
                        cur = curso(codigo, curs, requisito, obligatorio, semestre, creditos, estado )
                        igresar_curso(lista, cur)
                        messagebox.showinfo("mensaje","se agrego el contenido del archivo correctamente a la lista")
                    except:
                          messagebox.showerror("error","has escrito un paremetro fuera del tipo") 
                    
                    
                    
                        
    
    def mostrar_enLineEdit(lista, codigo, ventana):
         numero=int(codigo)
         existe = False
         encontrado=False
         if not lista:
           
            messagebox.showerror("error","no se puede editar elementos vacios ")
         else:   
                for x in lista:
                    nux=int(x.codigo)
                
                        
                    if nux == numero:
                        existe = True
                        if len(str(x.codigo))==1:
                            
                            ventana.lineEdit_codigo.setText(str("00")+str(x.codigo))
                        elif len(str(x.codigo))==2:
                            ventana.lineEdit_codigo.setText(str("0")+str(x.codigo))
                        else:
                            ventana.lineEdit_codigo.setText(str(x.codigo))

                        ventana.lineEdit_nombre.setText(str(x.curso))
                            
                        ventana.lineEdit_requisito.setText(str(x.requisito))
                        
                        numo=str(x.obligatorio)
                       
                        ventana.lineEdit_obli.setText(numo)
                        
                        ventana.line_semestre.setText(str(x.semestre))
                        ventana.line_creditos.setText(str(x.creditos))
                        ventana.line_estado.setText(str(x.estado))
                        
                           
                        break 

                if existe == False:
                    messagebox.showerror("error","el codigo del curso que desea editar no esta en la lista")

    def editar_lista(lista, codigo, ventana):
         numero=int(codigo)
         existe = False
         encontrado=False
         listarequi=[]

         codigosimi=int(ventana.lineEdit_codigo.text())
         nombre=ventana.lineEdit_nombre.text()
         requi=ventana.lineEdit_requisito.text()
         op= int(ventana.lineEdit_obli.text())
         if op==1 or op==0:
            op1=op
         else:
             messagebox.showinfo("info","la opcion es 0 o 1")
         sem= int(ventana.line_semestre.text())
         cre= int(ventana.line_creditos.text())
         estado= int(ventana.line_estado.text())
         if estado==1 or estado==0 or estado==-1:
            estado1=estado
         else:
            messagebox.showinfo("info","la opcion es 0 o 1 o -1")
         calase4= curso(codigosimi, nombre, requi, op1, sem, cre, estado1)
         if not lista:
           
            messagebox.showerror("error","no se puede editar elementos vacios ")
         else:   
                for y in lista:
                    nux=int(y.codigo)
                    
                    if nux==codigosimi:
                            lista.remove(y) 
                            existe=True 
                            break

                if existe==True or existe==False:
                    for x in lista:
                        nu1=int(x.codigo)
                        if nu1 == numero:
                            encontrado = True
                            
                                
                            x.set_codigo(int(ventana.lineEdit_codigo.text()))
                            x.set_curso(ventana.lineEdit_nombre.text())
                            listarequi=ventana.lineEdit_requisito.text()
                            x.set_requisito(listarequi)
                            oblik=int(ventana.lineEdit_obli.text())
                            if oblik==1 or oblik==0:
                                oblis=oblik
                            else:
                                messagebox.showinfo("info","la opcion es 0 o 1 ")
                            x.set_obligatorio(oblis)
                                
                            x.set_semestre(int(ventana.line_semestre.text()))
                            x.set_creditos(int(ventana.line_creditos.text()))
                            est= int(ventana.line_estado.text())
                            if est==1 or est==0 or est==-1:
                                est1=est
                            else:
                                messagebox.showinfo("info","la opcion es 0 o 1 o -1")
                            x.set_estado()
                            messagebox.showinfo("info", "curso editado con exito")
                            break
               
                    
                if encontrado == False:
                    lista.append(calase4)
                    messagebox.showinfo("info", "curso editado con exito")
                
    def contar_creditos_aprobados(lista, ventana):
         existe=False
         cre=0
         cred=0
         if not lista:
           
            messagebox.showerror("error","no se puede contar creditos vacios ")
         else: 
            for x in lista:

               if x.estado==0:
                 existe=True
                 cre=x.creditos
                 cred= cre+cred
             
            ventana.label_apro.setText(str(cred))
            if existe==False:
              ventana.label_apro.setText(str(cred))  
    
    def contar_creditos_cursando(lista, ventana):
         existe=False
         cre=0
         cred=0
         if not lista:
           
            messagebox.showerror("error","no se puede contar creditos vacios ")
         else: 
            for x in lista:

               if x.estado==1:
                 existe=True
                 cre=x.creditos
                 cred= cre+cred
             
            ventana.label_cursando.setText(str(cred))
            if existe==False:
              ventana.label_cursando.setText(str(cred)) 

    def contar_creditos_pendientes(lista, ventana):
         existe=False
         cre=0
         cred=0
         if not lista:
           
            messagebox.showerror("error","no se puede contar creditos vacios ")
         else: 
            for x in lista:

               if x.estado==-1 and x.obligatorio==1:
                 existe=True
                 cre=x.creditos
                 cred= cre+cred
             
            ventana.label_pendiente.setText(str(cred))
            if existe==False:
              ventana.label_pendiente.setText(str(cred))   

    def contar_creditos_porSemestre(lista, ventana, numero):
         existe=False
         creapro=0
         credapro=0
         crecur=0
         credcur=0
         crepen=0
         credpen=0
         if not lista:
           
            messagebox.showerror("error","no se puede contar creditos vacios ")
         else: 
            for x in lista:

               if x.estado==0 and x.semestre==numero:
                 existe=True
                 creapro=x.creditos
                 credapro= creapro+credapro
               if x.estado==1 and x.semestre==numero:
                 existe=True
                 crecur=x.creditos
                 credcur= crecur+credcur
               if x.estado==-1 and x.semestre==numero and x.obligatorio==1:
                 existe=True
                 crepen=x.creditos
                 credpen= crepen+credpen
             
             
            ventana.label_sempen.setText(str(credpen))
            ventana.label_semcurs.setText(str(credcur))
            ventana.label_semapro.setText(str(credapro))
            if existe==False:
              ventana.label_sempen.setText(str(credpen))
              ventana.label_semcurs.setText(str(credcur))
              ventana.label_semapro.setText(str(credapro))   

    def contar_creditos_porSemestreN(lista, ventana, numero):
         existe=False
         creapro=0
         credapro=0
 
         if not lista:
           
            messagebox.showerror("error","no se puede contar creditos vacios ")
         else: 
            while numero >= 1:

                for x in lista:

                        if x.obligatorio==1 and x.semestre==numero:
                            existe=True
                            creapro=x.creditos
                            
                            credapro= creapro+credapro
                           
              
                numero=numero-1
               
              
             
            ventana.label_semN.setText(str(credapro))
            if existe==False:
              ventana.label_semN.setText(str(credapro))
       
                            
               
    
