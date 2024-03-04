
import pickle
import random
from re import M, X
from sre_parse import CATEGORIES
import xml.etree.ElementTree as ET
import re
from clases import *
from datetime import datetime
from models.productos import Productos
from models.consumos import Consumos
from models.cliente import Clientes    
from models.instancia import Instancias   
from models.factura import Factura  
from utils.db import db
from models.categorias import Categorias
from models.confi import Confi
from models.Pedido import Pedido
from models.factura import Factura
class Metodos:
    def __init__(self) -> None:
        pass
    def formatofecha1(fecha:list):
        cadena=""
        for x in fecha:
            cadena=str(x[0])+"/"+str(x[1])+"/"+str(x[2])+" "+str(x[3])+":"+str(x[4])
        return cadena
    def obtener_fecha(fecha):
        patron1=r'(\d{2})/(\d{2})/(\d{4}) *(\d{2})*:*(\d{2})*'
        patron_nuevo2= re.findall(patron1,fecha)
        return patron_nuevo2
    def incertar_lista_de_listas(lista:list, clase, claseagregar):
        for elemento in lista:
            if elemento.iden==clase.iden:
                elemento.lista_recurso_confi.append(claseagregar)
            else:
                return False



    def leer_xmlconfiguracion(listarecurso:list, archivo,listacategoria:list, listaclientes:list):
        with open(archivo, encoding='utf-8') as file:
            if file.readable():
                    print(True)
                    xml_data= ET.fromstring(file.read())
                    lst_empresas= xml_data.findall('listaRecursos')
                    for recursos in lst_empresas:
                        recurso=recursos.findall("recurso")
                        for recur in recurso:
                            idenrecurso=""
                            recu=Recurso("","","","","",0.0)
                            iden=recur.attrib.values()
                            for x in iden:
                                idenrecurso=x
                                recu.iden=idenrecurso
                            nombrerecurso=recur.find('nombre').text
                            recu.nombre=nombrerecurso
                            abrevaturarecurso=recur.find('abreviatura').text
                            recu.abrebiatura=abrevaturarecurso
                            metrica=recur.find('metrica').text
                            recu.metrica=metrica
                            tiporecurso=recur.find('tipo').text
                            recu.tipo=tiporecurso
                            valorrecurso=recur.find('valorXhora').text
                            recu.valor_hora=float(valorrecurso)
                            Metodos.existe_en_lista(listarecurso,recu)
                    #lectura de lista categoria
                    lst_categoria= xml_data.findall('listaCategorias')
                    for recursos in lst_categoria:
                        categoria=recursos.findall("categoria")
                        for cate in categoria:
                            idencatego1=""
                            catego=Categoria("","","","")
                            idencatego=cate.attrib.values()
                            for x in idencatego:
                                idencatego1=x
                                catego.iden=idencatego1
                            nombrecatego=cate.find('nombre').text
                            catego.nombre=nombrecatego
                            categodescripcion=cate.find('descripcion').text
                            catego.descripcion=categodescripcion
                            cargacatego=cate.find('cargaTrabajo').text
                            catego.cargaTrabajo=cargacatego
                            Metodos.existe_en_lista(listacategoria,catego)
                            #lectura de listas de configuracion por categoria
                            lst_conficatego=cate.findall("listaConfiguraciones")
                            for conficatego in lst_conficatego:
                                lst_conficatego_1=conficatego.findall('configuracion')
                                for conf in lst_conficatego_1:
                                    codconfi=""
                                    conficate=Configuracion("","","")
                                    idconfcatego=conf.attrib.values()
                                    for x in idconfcatego:
                                        codconfi=x
                                        conficate.iden=codconfi
                                    nombreconficate=conf.find('nombre').text
                                    conficate.nombre=nombreconficate
                                    confidescrip=conf.find('descripcion').text
                                    conficate.descripcion=confidescrip
                                    Metodos.existe_en_lista(catego.listaconfi,conficate)
                                    #lectura de lista de recursos de confi
                                    lst_recursoconfi=conf.findall("recursosConfiguracion")
                                    for confirecu in lst_recursoconfi:
                                        lst_confi_recu=confirecu.findall("recurso")
                                        
                                        for recu_lst in lst_confi_recu:
                                            cod_lst_recu=""
                                            clase_recuso=Recurso_confi("",0.0)
                                            id_lst_recu=recu_lst.attrib.values()
                                            for  x in id_lst_recu:
                                                cod_lst_recu=x
                                                clase_recuso.iden=cod_lst_recu
                                            numero_lst_recu=recu_lst.text
                                            clase_recuso.numero=float(numero_lst_recu)
                                            #print(clase_recuso.numero)
                                            Metodos.existe_en_lista(conficate.lista_recurso_confi,clase_recuso)
                    #lectura de lista de clientes
                    lst_cliente=xml_data.findall('listaClientes')
                    for lst_client in lst_cliente:
                        lst_client_us=lst_client.findall("cliente")
                        for cliente in lst_client_us:
                            idcliente=""
                            client=Cliente("","","","","","")
                            cod_cliente= cliente.attrib.values()
                            for x in cod_cliente:
                                idcliente=x
                                client.iden=idcliente
                            nombrecliente=cliente.find('nombre').text
                            client.nombre=nombrecliente
                            usuariocliente=cliente.find('usuario').text
                            client.usuario=usuariocliente
                            clavecliente=cliente.find('clave').text
                            client.clave=clavecliente
                            direccioncliente=cliente.find('direccion').text
                            client.direccion=direccioncliente
                            correocliente=cliente.find('correoElectronico').text
                            client.correo=correocliente
                            Metodos.existe_en_lista(listaclientes,client)
                            lst_instancia=cliente.findall('listaInstancias')
                            for lst_instan in lst_instancia:
                                instancia=lst_instan.findall('instancia')
                                for instan in instancia:
                                    idintsnacia=""
                                    claseintsncia=Instrancia("","","","","","")
                                    codintancia= instan.attrib.values()
                                    for x in codintancia:
                                        idintsnacia=x
                                        claseintsncia.iden=idintsnacia
                                        idconfiintsancia=instan.find('idConfiguracion').text
                                        claseintsncia.idconfi=idconfiintsancia
                                        nombreintancia=instan.find('nombre').text
                                        claseintsncia.nombre=nombreintancia
                                        fechainicio=instan.find('fechaInicio').text
                                        fechalim=Metodos.obtener_fecha(fechainicio)
                                        fechaliminicio=Metodos.formatofecha1(fechalim)
                                        claseintsncia.fecha_inicio=fechaliminicio
                                        estadointancia=instan.find('estado').text
                                        claseintsncia.estado=estadointancia
                                        fechafinal=instan.find('fechaFinal').text
                                        fechaliminicio1=""
                                        try:
                                             fechalim1=Metodos.obtener_fecha(fechafinal)
                                             fechaliminicio1=Metodos.formatofecha1(fechalim1)
                                        except:
                                            print("Error no hay fehca ingresada")
                                       
                                        claseintsncia.fecha_final=fechaliminicio1
                                        Metodos.existe_en_lista(client.listainstancia,claseintsncia)





                     
                        

                      

                       

            else:
                    print(False)

    def leer_xmlconfiguracion_consumo(listaconsumo:list, archivo):
     with open(archivo, encoding='utf-8') as file:
            if file.readable():
                    print(True)
                    xml_data= ET.fromstring(file.read())
                    lst_empresas= xml_data.findall('consumo')
                    for consumo in lst_empresas:
                        clase_consumo = Consumo("","",0.0,"")
                        codigo=consumo.attrib.values()
                        listas=[]
                        for x in codigo:
                            #print("la llvae es:" ,x)
                            
                            listas.append(x)
                        clase_consumo.idencliente=listas[0]
                        #print(confi.iden)
                        clase_consumo.ideninstancia=listas[1]
                        tiempo=consumo.find('tiempo').text
                        clase_consumo.tiempo=tiempo
                        fecha=consumo.find('fechaHora').text
                        clase_consumo.fechahora=fecha
                        listaconsumo.append(clase_consumo)

                       

            else:
                    print(False)
    def existe_o_no_en_la_lista(lista:list, clase):
        encontrado=False
        
        for x in lista:
            if x.iden==clase.iden:
                encontrado=True
                break
        if encontrado==True:
            return True
        else:
            return False
    def existe_en_lista(lista:list, clase):
        encontrado=False
        if not lista:
            lista.append(clase)
        else:
            for x in lista:
                if x.iden==clase.iden:
                    encontrado=True
                    break
            if encontrado==False:
                 lista.append(clase)


    def mostrar_sistema(basedatosproducto:list, basedatoscate:list, basedatoscliente:list, basedatosinstancia:list, basedatosconfi:list, basedatospedido:list):
        canenap="               RECURSOS                 \n"
        cadenar=""
        cadenacategoria="               CATEGORIA                 \n"
        cadenacliente="               CLIENTE                  \n"
        cadenacate=""
        cadenaclient=""
        recurso:Productos
        for recurso in basedatosproducto:
            cadenar=cadenar+"Id de recurso:   "+recurso.idpro+"\n"+"Nombre de recurso:  "+recurso.nombre+"\n"+"Abreviatura:   "+recurso.abrebiatura+"\n"+"Metrica:   "+recurso.metrica+"\n"+"Tipo:    "+recurso.tipo+"\n"+"Valor por Hora:   "+str(recurso.valor_hora)+"\n"+"\n"
        #mostrar datos de categoria
        for categoria in basedatoscate:
            cadenacate=cadenacate+"Id categoria:    "+categoria.iden+"\n"+"Nombre de categoria:  "+categoria.nombre+"\n"+"Descripcion:   "+categoria.descripcion+"\n"+"Carga de trabajo:    "+categoria.cargaTrabajo+"\n"
        for conficate in basedatosconfi:
            cadenacate=cadenacate+"    Id configuracion:    "+conficate.iden+"\n"+"    Nombre:   "+conficate.nombre+"\n"+"    Descripcion:    "+conficate.descripcion+"\n"
        for recursoconfi in basedatospedido:
            cadenacate=cadenacate+"          Id recurso:   "+recursoconfi.iden+"\n"+"          Numero de recursos:   "+str(recursoconfi.numero)+"\n"+"\n"

        for cliente in basedatoscliente:
            cadenaclient=cadenaclient+"Nit:     "+str(cliente.iden)+"\n"+"Nombre:     "+cliente.nombre+"\n"+"Usuario:     "+cliente.usuario+"\n"+"Clave:     "+cliente.clave+"\n"+"Direccion:     "+cliente.direccion+"\n"+"Correo electronico:     "+cliente.correo+"\n"
        for instancia in basedatosinstancia:
            cadenaclient=cadenaclient+"    Id instancia:     "+str(instancia.iden)+"\n"+"    Id configuracion:    "+instancia.idconfi+"\n"+"    Nombre:     "+instancia.nombre+"\n"+"    Fecha de inicio:    "+instancia.fecha_inicio+"\n"+"    Estado:    "+instancia.estado+"\n"+"    Fecha de finalizacion:     "+str(instancia.fecha_final)+"\n"+"\n"


        cadenat=canenap+cadenar+cadenacategoria+cadenacate+cadenacliente+str(cadenaclient)
        return cadenat
    def devolverclase(lista:list,idcliente, idistancia):
        instancia:Instancias
        encontrado=False
        listaprov=[]
        for instancia in lista:
            
           
                if instancia.idcliente==idcliente and instancia.iden==idistancia:
                    listaprov.append(instancia)
                    encontrado=True
                    
                    
        if encontrado==True:
                return listaprov
            
        
    def devolverlistaconfi(idconfi,litacategoria:list):
        #categoria:Categoria
        pedido:Pedido
        listapedidos=[]
        for pedido in litacategoria:
        
                if pedido.idenconfi==idconfi:
                    listapedidos.append(pedido)
        return listapedidos, pedido.idencate
    def devolvervalorrecurso(idrecurso, listarecurso:list):
        recurso:Productos
        for recurso in listarecurso:
            if recurso.idpro==idrecurso:
               
                return recurso
          

    def generar_deuda(listaclientes:list, listarecurso:list, listacategoria:list, listaconsumos:list):
        cliente:Cliente
        consumo:Consumo
        instancia=Instrancia("","","","","","")
        recurso:Recurso
        listarecursoconfi:list
        recursoconfi:Recurso_confi
        tiempo=0.0
        idconfi=""
        idcliente=""
        idcategoria=""
        idistancia=""
        for consumo in listaconsumos:
            idcliente=consumo.idencliente
            idistancia=consumo.ideninstancia
            tiempo=consumo.tiempo
            print("---------------- tiempo-------"+ str(tiempo))
            instancia=Metodos.devolverclase(listaclientes,idcliente,idistancia)
            if instancia !=None:
                idconfi=instancia.idconfi
                print("------------------id confi--------------"+str(idconfi))
                listarecursoconfi, idcategoria=Metodos.devolverlistaconfi(idconfi,listacategoria)
                deudaporrecurso=0.0
                valorrecurso=0.0
                recursonumero=0.0
                deudatotal=0.0
                recursoiden=""
                cadena=""
                for recursoconfi in listarecursoconfi:
                    recursonumero=recursoconfi.numero
                    print("-----------------numero de recursos--------- "+str(recursonumero))
                    recursoiden=recursoconfi.iden
                    print("--------------------------recurso iden-----------"+str(recursoiden))
                    recurso=Metodos.devolvervalorrecurso(recursoiden,listarecurso)
                
                    valorrecurso=recurso.valor_hora
                    print("-------------------------"+ str(valorrecurso))
                    cadena=cadena+"Instancia:   "+idistancia+"\n"+"Consumo por recurso"+"\n"+"id del recurso: "+recursoiden+"\n"+"Cantidad de recursos:   "+str(recursonumero)+"\n"+"Valor del recurso:    "+str(valorrecurso)+"\n"+"Tiempo de consumo:    "+str(tiempo)+"\n"+"\n"
                    deudaporrecurso=float(tiempo)*recursonumero*valorrecurso

                    deudatotal= deudaporrecurso+deudatotal
                print("---------------dEUATA TOTAL --------------"+str(deudatotal))
                for cliente in listaclientes:
                    if cliente.iden==idcliente:
                        clasefactura=Datos_factura(deudatotal, cadena,idcategoria,idconfi)
                        cliente.listadeuda.append(clasefactura)
    def guardar_recursos(listarecursos:list, tipo:str):
         with open(tipo+".pickle", "wb") as file:
             pickle.dump(listarecursos, file)
    def leerrecursos(tipo):
        with open(tipo+".pickle", "rb") as f:
            obj = pickle.load(f)
        return obj
    def devolvertruofalse(lista:list, clase):
        cliente:Cliente
        instancia:Instrancia
        encontrado=False
        for cliente in lista:
            for instancia in cliente.listainstancia:
                if cliente.iden==clase.idencliente and instancia.iden==clase.ideninstancia:
                    encontrado=True
                    break
                    
                    
            if encontrado==True:
                return True
            else:
                return False
    def lista_reporte_categoria(listaclientes:list):
        listaaux=[]
        cliente:Cliente
        datofac:Datos_factura
        for cliente in listaclientes:
            for datofac in cliente.listadeuda:
                listaaux.append(datofac.deudaconsumo)
        return listaaux
    def reporte_categoria(listaclientes:list):
        cliente:Cliente
        datofac:Datos_factura
        listaaux=[]
        listaaux=Metodos.lista_reporte_categoria(listaclientes)
        listaaux.sort(reverse=True)
        dato=0.0
        cadena=""
        for i in range(3):
           dato=listaaux[i]
           for cliente in listaclientes:
                categoria=""
                confi=""
                for datofac in cliente.listadeuda:
                    if datofac.deudaconsumo==dato:
                        categoria=datofac.categoria
                        confi=datofac.idconfi
                        cadena=cadena+"La categoria:   "+categoria+"\n"+"Con id Configuracion:    "+confi+"\n"+"Tiene una ganancia de:    "+str(dato)+"\n"+"\n"
        return cadena
    def esta_ono_confi(lista:list,dato):
        encontrado=False
        if not lista:
            lista.append(dato)
        else:
            for x in lista:
                if x==dato:
                    encontrado=True
                    break
            if encontrado==False:
                 lista.append(dato)
    def lista_aux_confi(listaclientes:list):
        listaconfi=[]
        cliente:Cliente
        datofac:Datos_factura
        listaaux=Metodos.lista_reporte_categoria(listaclientes)
        listaaux.sort(reverse=True)
        dato=0.0
        cadena=""
        for i in range(3):
           dato=listaaux[i]
           for cliente in listaclientes:
                confi=""
                for datofac in cliente.listadeuda:
                    if datofac.deudaconsumo==dato:
                        
                        confi=datofac.idconfi
                        Metodos.esta_ono_confi(listaconfi,confi)
        return listaconfi
    def reporte_recursos(listaclientes:list,listacategoria:list,listarecurso:list): 
        listaaux=Metodos.lista_aux_confi(listaclientes)
        cadenat=""
        for dato in listaaux:
                    print(dato)
                    listarecursoconfi,catego=Metodos.devolverlistaconfi(dato,listacategoria)
                    recursoiden=""
                    cadena=""
                    for recursoconfi in listarecursoconfi:
                        recursoiden=recursoconfi.iden
                        recurso=Metodos.devolvervalorrecurso(recursoiden,listarecurso)
                    
                        cadena=cadena+"Id de recurso:   "+recurso.iden+"\n"+"Nombre de recurso:  "+recurso.nombre+"\n"+"Abreviatura:   "+recurso.abrebiatura+"\n"+"Metrica:   "+recurso.metrica+"\n"+"Tipo:    "+recurso.tipo+"\n"+"Valor por Hora:   "+str(recurso.valor_hora)+"\n"+"\n"
                    cadenat=cadenat+cadena
        return cadenat
    def Generar_factura(listaclientes:list, id):
        numeror =random.randint(0,1000)
        cliente:Cliente
        cadena=""
        cadenatotal=""
        cadenanit=""
        now = datetime.now()
        anio=now.year
        mes=now.month  
        dia=now.day
        hora=now.hour   

        minu=now.minute  
        datofactura=""
        cadena3=""
        cadenanit="Fecha:   "+str(dia)+"/"+str(mes)+"/"+str(anio)+"  "+str(hora)+":"+str(minu)+"\n"+"No.     "+str(numeror)+"\n"+"Nit Cliente: "+id+"\n"
        totaldeuda=0.0
        for datofac in listaclientes:
                if datofac.idencliente==id:
                    datofactura=datofac.deudaconsumo
                    cadena=cadena+datofac.descripcion+"\n"
                    cadena3+="El consumo es:    "+str(datofactura)+"\n"
                    totaldeuda+=datofac.deudaconsumo
        cadenatotal=cadenanit+cadena+cadena3+"Total a pagar:   "+str(totaldeuda)
        return cadenatotal
    def devoloververdaderoofalse(lista:list , iden):
        encontrado=False
        for clase in lista:
            if clase.iden==iden:
                encontrado=True
                break
        if encontrado==True:
            return True
        else:
            return False
    def basedatosrecurso(listarecurso:list):
        recurso:Recurso
        producto:Productos
        
        for recurso in listarecurso:
            producto=Productos(recurso.iden,recurso.nombre,recurso.abrebiatura,recurso.metrica,recurso.tipo,recurso.valor_hora)
            db.session.add(producto)
            db.session.commit()
    
    def basedatosConsumo(listaconsumo:list):
        consumo:Consumo
        consumo1:Consumos   
        for consumo in listaconsumo:
            consumo1=Consumos(consumo.idencliente,consumo.ideninstancia,consumo.tiempo,consumo.fechahora)
            db.session.add(consumo1)
            db.session.commit()
            
    def basedatosClientes(listaclientes:list):
        cliente1:Clientes
        cliente:Cliente
        instancia :Instancias
        instranncia:Instrancia
        factura1:Factura
        for cliente in listaclientes:
            cliente1=Clientes(cliente.iden,cliente.nombre,cliente.usuario,cliente.clave,cliente.direccion,cliente.correo,cliente.deuda)
            db.session.add(cliente1)
            db.session.commit()
            for instranncia in cliente.listainstancia:
                instancia=Instancias(cliente.iden,instranncia.iden,instranncia.idconfi,instranncia.nombre,instranncia.fecha_inicio,instranncia.estado,instranncia.fecha_final)

                db.session.add(instancia)
                db.session.commit()
            for factura in cliente.listadeuda:
                factura1=Factura(cliente.iden,factura.deudaconsumo,factura.descripcion,factura.categoria,factura.idconfi)
                db.session.add(factura1)
                db.session.commit()
    def basedatosCategoria(listacategoria:list):
        categoria:Categoria
        for categoria in listacategoria:
            categoria1=Categorias(categoria.iden,categoria.nombre,categoria.descripcion,categoria.cargaTrabajo)
            db.session.add(categoria1)
            db.session.commit()
            for confi in categoria.listaconfi:
                confi1=Confi(categoria.iden,confi.iden,confi.nombre,confi.descripcion)
                db.session.add(confi1)
                db.session.commit()
                for recursoconfi in confi.lista_recurso_confi:
                    recursoconfi1=Pedido(categoria.iden,confi.iden,recursoconfi.iden,recursoconfi.numero)
                    db.session.add(recursoconfi1)
                    db.session.commit()

    def generar_deudabasedatos(basedatosproducto:list, basedatosclientes:list, basedatosconsumos:list, basedatoscate:list, basedatosinstancia:list, basedatospedido:list, basedatosconfi:list):
            cliente:Cliente
            consumo:Consumos
            instancia=Instrancia("","","","","","")
            recurso:Recurso
            listarecursoconfi:list
            recursoconfi:Recurso_confi
            tiempo=0.0
            idconfi=""
            listaconfi=[]
            idcliente=""
            idcategoria=""
            idistancia=""
            for consumo in basedatosconsumos:
                    idcliente=consumo.idencliente
                    idistancia=consumo.ideninstancia
                    tiempo=consumo.tiempo
                    print("---------------- tiempo-------"+ str(tiempo))
                    listaconfi=Metodos.devolverclase(basedatosinstancia,idcliente,idistancia)
                    idconfi=""
                    idcategoria=""
                    if listaconfi !=None:
                        for instancia in listaconfi:
                            idconfi=instancia.idconfi

                            listarecursoconfi, idcategoria=Metodos.devolverlistaconfi(idconfi,basedatospedido)
                            deudaporrecurso=0.0
                            valorrecurso=0.0
                            recursonumero=0.0
                            deudatotal=0.0
                            recursoiden=""
                            cadena=""
                            for recursoconfi in listarecursoconfi:
                                recursonumero=recursoconfi.numero
                                print("-----------------numero de recursos--------- "+str(recursonumero))
                                recursoiden=recursoconfi.iden
                                print("--------------------------recurso iden-----------"+str(recursoiden))
                                recurso=Metodos.devolvervalorrecurso(recursoiden,basedatosproducto)
                            
                                valorrecurso=recurso.valor_hora
                                print("-------------------------"+ str(valorrecurso))
                                cadena=cadena+"Instancia:   "+idistancia+"\n"+"Consumo por recurso"+"\n"+"id del recurso: "+recursoiden+"\n"+"Cantidad de recursos:   "+str(recursonumero)+"\n"+"Valor del recurso:    "+str(valorrecurso)+"\n"+"Tiempo de consumo:    "+str(tiempo)+"\n"+"\n"
                                deudaporrecurso=float(tiempo)*recursonumero*valorrecurso

                                deudatotal= deudaporrecurso+deudatotal
                            print("---------------dEUATA TOTAL --------------"+str(deudatotal))
                        for cliente in basedatosclientes:
                            if cliente.iden==idcliente:
                                clasefactura=Factura(idcliente,deudatotal,cadena,idcategoria,idconfi)
                                db.session.add(clasefactura)
                                db.session.commit()
                        

                    


                    
                    





           
               
                
            

            
