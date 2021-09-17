# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 13:06:25 2021

@author: david
"""
#El objetivo de este codigo es analizar datos de Lifestore mediante funciones 
#basicas de python como, condicionales, ciclos for, while, listas y comparaciones
#el uso de pandas,dataframes y demas funciones es solamente para imprimir en consola los datos de manera mas ordenada

from lifestore_file import lifestore_sales, lifestore_searches, lifestore_products
import pandas as pd #solo para visualizar mejor los datos en consola

pd.set_option('display.max_columns', None) #Visualizar todas las columnas en pantalla
pd.set_option('max_colwidth', 25)          #Restringe el maximo numero de caracteres por columna

cuentas= [['admin','admin'],['hola','123'],['hola2','1234']] #Cuentas ya registradas
inicio_sesion=0
intentos=0
opcion=''
count_menu=0

#Ciclo while para iniciar sesion
while inicio_sesion!=1 and intentos<3:
    estado=input('Tienes cuenta de usuario? y/n:')
    if estado=='y':
        usuario=input('Ingrese su nombre de usuario:')
        contrasena=input('Ingrese su contrasena:')
    
        #ciclo for para verificar que la cuenta exista
        for cuenta in cuentas:
            if usuario==cuenta[0] and contrasena==cuenta[1]:
                inicio_sesion=1
                print('Inicio Exitoso')
        
        #condicional para indicar que la cuenta no existe
        if inicio_sesion==0:
            print('Usuario o contrasena incorrectos')
            intentos+=1
            print('Te quedan ' +str(3-intentos) +' intentos' + ' posibles')
    
    #Condicion para crear una nueva cuenta    
    elif estado=='n':
        
        usuario_nuevo=input('Ingrese un nombre de usuario:')
            
        verificar=True
        reintento=0
        #ciclo while para verificar la contrasena
        while verificar and reintento<3:
            contrasena_nueva=input('Ingrese una contrasena:')
            verificar_contrasena=input('Ingrese nuevamente la contrasena:')
            if contrasena_nueva!=verificar_contrasena:
                verificar=True
                reintento+=1
                print('La contrasena no coincide')
            else:
                cuentas.append([usuario_nuevo,contrasena_nueva])
                print('Registro exitoso, por favor inicia sesion')
                verificar=False
                
    #Si se ingresa otra opcion que no se n/y regresa respuesta invalida            
    else:
        print('Respuesta no valida')
        count_menu+=1
        print(count_menu)
        if count_menu>3:
            print('Haz hecho muchos intentos')
            break

    
##El codigo siguiente antes del while de opciones lo dejamos fuera de las opciones ya que 
##necesitamos varias listas como variables globales y a partir de 
##ellas generar nuevas listas dependiendo la opcion    
    
#Contamos el numero de ventas por producto
num_ventas=0
productos_vendidos=[] # [id_producto,nom_producto,categoria,num_ventas]    
for producto in lifestore_products:
    for venta in lifestore_sales:
        if '2020' in venta[3]:    #con esta condicion eliminamos los datos inservibles de otros años
            if producto[0]==venta[1]:
                num_ventas+=1
    if num_ventas !=0:
        productos_vendidos.append([producto[0],producto[1],producto[3],num_ventas])
        num_ventas=0
        
#Tenemos un ciclo for anidado el cual compara los id de los productos en las listas
#lifestore_sale y lifestore_products contando cuantas veces  aparece en las ventas


#Ordenamos la lista de forma descendente partiendo del producto con mayor ventas
productos_vendidos_ordenados=[]
   
while productos_vendidos:
    maximo=productos_vendidos[0][3]
    lista_actual=productos_vendidos[0]
    for producto in productos_vendidos:
        if producto[3]>maximo:
            maximo=producto[3]
            lista_actual=producto
    productos_vendidos_ordenados.append(lista_actual)
    productos_vendidos.remove(lista_actual)    

#Contamos el numero de busquedas por producto
num_busqueda=0
productos_buscados=[] # [id_producto,nom_producto,categoria,num_busquedas]    
for producto in lifestore_products:
    for busqueda in lifestore_searches:
        if producto[0]==busqueda[1]:
            num_busqueda+=1
    if num_busqueda !=0:
        productos_buscados.append([producto[0],producto[1],producto[3],num_busqueda])
        num_busqueda=0
        
#Ordenamos la lista de forma descendente partiendo del producto con mayor ventas
productos_buscados_ordenados=[]
                            
while productos_buscados:
    maximo=productos_buscados[0][3]
    lista_actual=productos_buscados[0]
    for busqueda in productos_buscados:
        if busqueda[3]>maximo:
            maximo=busqueda[3]
            lista_actual=busqueda
    productos_buscados_ordenados.append(lista_actual)
    productos_buscados.remove(lista_actual)      
    
#Lista de las categorias
#Filtramos las categorias que hay en lifestore_products
categorias=[]
for i in lifestore_products:
    if i[3] not in categorias:
        categorias.append(i[3])
        
        
#Realizamos un promedio del puntaje obtenido en las reseñas por producto
num_resenas=0
suma_puntaje=0
devoluciones=0
productos_resena=[] # [id_producto,nom_producto,num_resenas,puntaje,devoluciones]    
for producto in lifestore_products:
    for resena in lifestore_sales:
        if '2020' in resena[3]:    
            if producto[0]==resena[1]:
                suma_puntaje+=resena[2]
                num_resenas+=1
                if resena[4]==1:
                    devoluciones+=1
    if num_resenas !=0:
        productos_resena.append([producto[0],producto[1],num_resenas,float("{0:.2f}".format(suma_puntaje/num_resenas)),devoluciones])
        num_resenas=0
        suma_puntaje=0
        devoluciones=0
                
productos_con_resena_ordenados=[]
   
while productos_resena:
    maximo=productos_resena[0][3]
    lista_actual=productos_resena[0]
    for producto in productos_resena:
        if producto[3]>maximo:
            maximo=producto[3]
            lista_actual=producto
    productos_con_resena_ordenados.append(lista_actual)
    productos_resena.remove(lista_actual)  

#Filtramos en que meses hay ventas
meses=[]
for i in lifestore_sales:
    if i[3][3:5] not in meses: #tomamos la cadena de caracteres que representa el mes
        meses.append(i[3][3:5])

#ordenamos los meses
meses_ordenados=[]        
while meses:
    minimo=meses[0]
    lista_actual=meses[0]
    for mes in meses:
        if mes<minimo:
            minimo=mes
            lista_actual=mes
    meses_ordenados.append(lista_actual)
    meses.remove(lista_actual) 
    
#generamos una lista de los ingresos mensuales, las ventas, devoluciones y el costo de las devoluciones
ingresos_mes=0
num_ventas_mes=0
devoluciones=0
costo_devoluciones=0
ingresos_mensuales=[] # [mes,# ventas, ingresos,devoluciones,costo_devoluciones]    
for mes in meses_ordenados:
    for producto in lifestore_products:
        for venta in lifestore_sales:
            if '2020' in venta[3]:    #Quita los datos de otros anos que no sirven
                if mes==venta[3][3:5]: #compara si el mes se encuentra en el elemento de lifestore_sales
                    if venta[1]==producto[0]: #compara los id de lifestore_sales y lifestore_products
                        ingresos_mes+=producto[2]  #Vamos sumando el valor de los productos para obtener los ingresos por mes
                        num_ventas_mes+=1 #contamos el numero de ventas
                        if venta[4]==1: # si el valor de devolucion es 1 la contabilizamos y sumamos su valor 
                            devoluciones+=1
                            costo_devoluciones+=producto[2]
                            
    if num_ventas_mes !=0:
        ingresos_mensuales.append([mes,num_ventas_mes,ingresos_mes,devoluciones,costo_devoluciones])
        ingresos_mes=0
        num_ventas_mes=0
        costo_devoluciones=0
        devoluciones=0
    
print()


#En esta parte se inicia el ciclo while para mostrar el menu de opciones y dependiendo que
#opcion se elige se imprime en pantalla la informacion correspondiente
#despues de elegir la opcion se despliega nuevamente el menu hasta oprimir s para salir
while opcion!='s':   
    
    if inicio_sesion==1:
        print("""Elige una opcion:
        1. Productos vendidos
        2. Productos con mas ventas
        3. Productos con menos ventas
        4. Productos sin ventas
        5. Productos buscados
        6. Productos con mas busquedas
        7. Productos con menores busquedas
        8. Productos no buscados
        9. Productos vendidos por categorias
        10. Productos buscados por categorias
        11. Productos con mejores reseñas
        12. Productos con peores reseñas
        13. Ingresos y ventas mensuales
        14. Ingresos y ventas anual
        15. Meses con mayores ventas
        16. Meses con menores ventas
        17. Productos a retirar
        Oprima s para salir""")
        opcion=input('Opcion:')
        print('\n')
    
    #Productos vendidos ordenados del producto mas vendido al menos vendido  
    if opcion=='1':
         
        print('Productos Vendidos')
        #usamos dataframes para imprimir en patalla mejor los resultados
        datos=pd.DataFrame(productos_vendidos_ordenados) 
        datos.columns=['id_producto','Nombre','Categoria','# ventas'] #asignamos a cada columna un nombre
        print(datos) #imprimimos los datos en pantalla
        print('\n') #salto de linea
        
    #Productos con mas ventas    
    elif opcion=='2':
        print('Productos con mas ventas')
        #Hacemos una nueva lista con los productos con ventas mayores a 5    
        productos_con_mayores_ventas=[i for i in productos_vendidos_ordenados if i[3]>5]
        
        datos=pd.DataFrame(productos_con_mayores_ventas) 
        datos.columns=['id_producto','Nombre','Categoria','# ventas']
        print(datos)
        print('\n')
    
    #Productos con menores ventas     
    elif opcion=='3':
        print('Productos con menos ventas')
        #Hacemos una nueva lista con los productos con ventas menores a 5    
        productos_con_menos_ventas=[i for i in productos_vendidos_ordenados if i[3]<=5]
        
        datos=pd.DataFrame(productos_con_menos_ventas) 
        datos.columns=['id_producto','Nombre','Categoria','# ventas']
        print(datos)
        print('\n')

    #Productos sin ventas
    elif opcion=='4':
        print('Productos sin ventas')
        # obtenemos una lista de los id de los productos que se vendieron
        id_vendidos=[producto[1] for producto in lifestore_sales] 
        #comparando el id de todos los productos con los id de los que se vendieron obtenemos los productos que no se vendieron
        productos_sin_venta=[[i[0],i[1],i[3],0] for i in lifestore_products if i[0] not in id_vendidos]
               
        datos=pd.DataFrame(productos_sin_venta) 
        datos.columns=['id_producto','Nombre','Categoria','# ventas']
        print(datos)
        print('\n')
    
    #Productos buscados
    elif opcion=='5':
        print('Productos buscados')
        datos=pd.DataFrame(productos_buscados_ordenados) #para presentar los datos
        datos.columns=['id_producto','Nombre','Categoria','# busquedas']
        print(datos)  
        print('\n')
        
    #Productos con mayores busquedas
    elif opcion=='6':
        print('Productos con mayores busquedas')
        #Hacemos una nueva lista con los productos con busquedas meayores a 5    
        productos_con_mayores_busquedas=[i for i in productos_buscados_ordenados if i[3]>5]
        
        datos=pd.DataFrame(productos_con_mayores_busquedas) 
        datos.columns=['id_producto','Nombre','Categoria','# busquedas']
        print(datos)    
        print('\n')
    
    #Productos con menores busquedas
    elif opcion=='7':
        print('Productos con menores busquedas')
        #Hacemos una nueva lista con los productos con busquedas menores a 5    
        productos_con_menos_busquedas=[i for i in productos_buscados_ordenados if i[3]<=5]
        
        datos=pd.DataFrame(productos_con_menos_busquedas) 
        datos.columns=['id_producto','Nombre','Categoria','# busquedas']
        print(datos)
        print('\n')
        
    #Productos sin busquedas
    elif opcion=='8':
        print('Productos sin busquedas')
        # obtenemos una lista de los id de los productos que se buscaron
        id_buscados=[busqueda[1] for busqueda in lifestore_searches] 
        #comparando el id de todos los productos con los id de los que se buscaron obtenemos los productos que no se buscaron
        productos_sin_busqueda=[[i[0],i[1],i[3],0] for i in lifestore_products if i[0] not in id_buscados]
               
        datos=pd.DataFrame(productos_sin_busqueda) 
        datos.columns=['id_producto','Nombre','Categoria','# busquedas']
        print(datos)
        print('\n')
        
    #Productos vendidos por categorias    
    elif opcion=='9':
        print('Productos vendidos por categorias')
        
        #Se genera una lista de lista por compresion, corriendo un ciclo for por cada categoria
        # y posteriormente comparar si dicha categoria se encuentra en los productos vendidos ordenados
        
        productos_vendidos__por_categorias=[[i for i in productos_vendidos_ordenados  if i[2]==categorias[j]]\
                                            for j in range(0,len(categorias))]
            
        for i in range(0,len(categorias)):
            data_categoria=pd.DataFrame(productos_vendidos__por_categorias[i]) 
            data_categoria.columns=['id_producto','Nombre','Categoria','# ventas']
            data_categoria=data_categoria.drop(['Categoria'],axis=1)
            print(categorias[i])
            print(data_categoria)
            print('\n')
    
    #Productos buscados por categorias    
    elif opcion=='10':
        print('Productos buscados por categorias')
        
        #Funciona de la misma manera que el de ventas, solo removemos la categoria sin productos
        productos_buscados_por_categorias=[[i for i in productos_buscados_ordenados  if i[2]==categorias[j]]\
                                  for j in range(0,len(categorias))]
        productos_buscados_por_categorias.remove([])
            
        for i in categorias:
            for j in productos_buscados_por_categorias:
                if i in j[0]:        
                    data_categoria=pd.DataFrame(j) 
                    data_categoria.columns=['id_producto','Nombre','Categoria','# busquedas']
                    data_categoria=data_categoria.drop(['Categoria'],axis=1)
                    print(j[0][2])
                    print(data_categoria)
                    print('\n')
     
    #Productos con las mejores resenas
    elif opcion=='11':
        print('Productos con las mejores reseñas')
         
        #Hacemos una nueva lista con los productos con un puntaje mayor o igual a 4.5    
        productos_con_mejores_resenas=[i for i in productos_con_resena_ordenados if i[3]>=4.5]
        datos=pd.DataFrame(productos_con_mejores_resenas) 
        datos.columns=['id_producto','Nombre','#reseñas','Puntaje','# Devoluciones']
        print(datos)
        print('\n')
        
        
    #Productos con las peores resenas
    elif opcion=='12':
        print('Productos con las peores reseñas')
         
        #Hacemos una nueva lista con los productos con un puntaje menor a 4.5    
        productos_con_peores_resenas=[i for i in productos_con_resena_ordenados if i[3]<4.5]
        datos=pd.DataFrame(productos_con_peores_resenas) 
        datos.columns=['id_producto','Nombre','#reseñas','Puntaje','# Devoluciones']
        print(datos)
        print('\n')
        
    #Ingresos y ventas mensuales    
    elif opcion=='13':
        print('Ingresos y ventas mensuales')
    
        datos=pd.DataFrame(ingresos_mensuales) 
        datos.columns=['mes','# ventas','Ingresos','Devoluciones','Costo devolucion']
        datos['mes']=datos['mes'].replace(['01','02','03','04','05','06','07','08','09'],['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre'])
        print(datos)
        print('\n')
        
    #Ingreso y ventas anual    
    elif opcion=='14':
        print('Ingresos y ventas anual')
        
        ventas=0
        ingresos=0
        devoluciones=0
        costos=0
        for i in ingresos_mensuales:
            ventas+=i[1]
            ingresos+=i[2]
            devoluciones+=i[3]
            costos+=i[4]
        anual=[[ventas,ingresos,devoluciones,costos]]
        
        datos=pd.DataFrame(anual) 
        datos.columns=['# ventas','Ingresos','Devoluciones','Costo devolucion']
        print(datos)
        print('\n')
        
    #meses con mayores ventas
    elif opcion=='15':
        print('Meses con mayores ventas')
        #Lista con meses con ventas mayores o iguales a 30
        meses_con_mejores_ventas=[i for i in ingresos_mensuales if i[1]>=30]
        datos=pd.DataFrame(meses_con_mejores_ventas) 
        datos.columns=['mes','# ventas','Ingresos','Devoluciones','Costo devolucion']
        datos['mes']=datos['mes'].replace(['01','02','03','04','05'],['enero','febrero','marzo','abril','mayo'])
        print(datos)
        print('\n')
        
    #meses con menores ventas
    elif opcion=='16':
        print('Meses con menores ventas')
        
        #Hacemos una nueva lista con los meses con ventas menores a 30   
        meses_con_menores_ventas=[i for i in ingresos_mensuales if i[1]<30]
        datos=pd.DataFrame(meses_con_menores_ventas) 
        datos.columns=['mes','# ventas','Ingresos','Devoluciones','Costo devolucion']
        datos['mes']=datos['mes'].replace(['06','07','08','09'],['junio','julio','agosto','septiembre'])
        print(datos)
        print('\n')
     
    #productos a retirar    
    elif opcion=='17':
        print('Productos a retirar')
        #Lista de los id de los productos que consideramos se deben retirar
        id_productos_retirar=[9,13,14,16,17,19,20,23,24,26,27,30,31,32,34,35,36,37,38,39,40,41,43,45,46,52,53,55,56,58,59,60,75,76,77,78,79,80,81,82,83,62,63,64,65,68,69,70,71,72,73,86,87,88,90,91,92,93,95,96]

        productos_retirar=[]
        for i in id_productos_retirar:
            for j in lifestore_products:
                if i==j[0]:
                    productos_retirar.append([j[0],j[1],j[3]])
                    
        datos=pd.DataFrame(productos_retirar) 
        datos.columns=['Id_producto','Nombre','categoria']
        print(datos)
        print('\n')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        