""" 
    Universidad de las Fuerzas Armadas ESPE Sede Santo Domingo de los Colorados
    Departamento Ciencias de la Computación
    Ingeniería en Tecnologías de la Información
    
    Autores: José Ruiz
             Brandon Perengueza
    Materia: Inteligencia Artificial

    Programación del Agente Inteligente
    Agente: Agrobot E-Series cosechador de fresas

"""

#Se define la función que pertence a la zona 1
def Zona_1():
    """ Se inicializa la zona_1
        Para cada localización su objetivo es tener el estado en 0 
        Se indica que 0 es la fruta aun verde y 1 que la fruta esta totalmente madura lista para cosechar
        Se inicializa en el costo 0
    """
    zona_1 = {'A': '0'}
    costo = 0
    #Nombre de la zona
    print("\nZona 1 Poste - Reproducción de Fresas \n")
    #Variable de la zona 1 que permitira ingresar por consola al usuario
    localizacion_A = input("Digite si las fresas de la zona estan cosechadas (0) o si las fresas estan por cosechar (1) : ") 
    #Objetivo alcanzar del zona 1
    print("Objetivo en alcanzar: " + str(zona_1))
        #Se condiciona la localizacion que tomara el valor del usuario y ejecutara la acción determinada 
        #para el robot si realiza una accion aumentara el costo caso contrario se mantendra con su
        #valor inicial   
    if localizacion_A == '1':
            #La zona se encuentra cosechada
            print("La zona 1 se encuentra en estado de cosecha.")
            # Marcara completado la cosecha
            zona_1['A'] = '0'
            costo += 1 #Aumenta el costo del agrobot
            #Imprime el mensaje de exito junto con el nuevo costo
            print("La zona 1 ya ha sido cesechada con exito.")
            print("Costo actual: " + str(costo))
            
    else:
        #La zona de cultivo se encuentra cosechada. Por lo tanto no se realiza ninguna acción
        print("La zona 1 se encuentra en estado de crecimiento de las fresas.")
        print("Costo actual: " "("+ str(costo)+")")
    #Se imprimira el resultado de la zona de cultivo seleccionado, alcanzo el objetivo con el costo.    
    print("Estado de la zona 1: ")
    print(zona_1)
    print("Medición del rendimiento: " + str(costo))

#******************************************************************************************************************
#Se define la función que pertence a la zona 2
def Zona_2():
    """ Se inicializa la zona_2
        Para cada localización su objetivo es tener el estado en 0 
        Se indica que 0 es la fruta aun verde y 1 que la fruta esta totalmente madura lista para cosechar
        Se inicializa en el costo 0
    """
    zona_2 = {'B': '0'}
    costo = 0
    #Nombre de la zona
    print("\nZona 2 Peripa - Reproducción de Fresas \n")
    #Variable de la zona 2 que permitira ingresar por consola al usuario
    localizacion_B = input("Digite si las fresas de la zona estan cosechadas (0) o si las fresas estan por cosechar (1) : ") 
    #Objetivo alcanzar del zona 2
    print("Objetivo en alcanzar: " + str(zona_2))
        #Se condiciona la localizacion que tomara el valor del usuario y ejecutara la acción determinada 
        #para el robot si realiza una accion aumentara el costo caso contrario se mantendra con su
        #valor inicial 
    if localizacion_B == '1':
            #La zona se encuentra cosechada
            print("La zona 2 se encuentra en estado de cosecha.")
            #Aumenta el costo del agrobot
            zona_2['B'] = '0'
            costo += 1 #Imprime el mensaje de exito junto con el nuevo costo 
            print("La zona 2 ya ha sido cesechada con exito.")
            print("Costo actual: " + str(costo))
            
    else:
        #La zona de cultivo se encuentra cosechada. Por lo tanto no se realiza ninguna acción
        print("La zona 2 se encuentra en estado de crecimiento de las fresas.")
        print("Costo actual: " "("+ str(costo)+")")
    #Se imprimira el resultado de la zona de cultivo seleccionado, alcanzo el objetivo con el costo.     
    print("Estado de la zona 2: ")
    print(zona_2)
    print("Medición del rendimiento: " + str(costo))

#******************************************************************************************************************
#Se define la función que pertence a la zona 3
def Zona_3():
    """ Se inicializa la zona_3
        Para cada localización su objetivo es tener el estado en 0 
        Se indica que 0 es la fruta aun verde y 1 que la fruta esta totalmente madura lista para cosechar
        Se inicializa en el costo 0
    """
    zona_3 = {'C': '0'}
    costo = 0
    #Nombre de la zona
    print("\nZona 3 Chiguilpe - Reproducción de Fresas \n")
    #Variable de la zona 3 que permitira ingresar por consola al usuario
    localizacion_C = input("Digite si las fresas de la zona estan cosechadas (0) o si las fresas estan por cosechar (1) : ") 
    #Objetivo alcanzar del zona 3
    print("Objetivo en alcanzar: " + str(zona_3))
        #Se condiciona la localizacion que tomara el valor del usuario y ejecutara la acción determinada 
        #para el robot si realiza una accion aumentara el costo caso contrario se mantendra con su
        #valor inicial 
    if localizacion_C == '1':
            #La zona se encuentra cosechada
            print("La zona 3 se encuentra en estado de cosecha.")
            #Aumenta el costo del agrobot
            zona_3['C'] = '0'
            costo += 1 #Imprime el mensaje de exito junto con el nuevo costo 
            print("La zona 3 ya ha sido cesechada con exito.")
            print("Costo actual: " + str(costo))
            
    else:
        #La zona de cultivo se encuentra cosechada. Por lo tanto no se realiza ninguna acción
        print("La zona 3 se encuentra en estado de crecimiento de las fresas.")
        print("Costo actual: " "("+ str(costo)+")")
    #Se imprimira el resultado de la zona de cultivo seleccionado, alcanzo el objetivo con el costo.    
    print("Estado de la zona 3: ")
    print(zona_3)
    print("Medición del rendimiento: " + str(costo))

#******************************************************************************************************************
#Se define la función que pertence a la zona 4
def Zona_4():
    """ Se inicializa la zona_4
        Para cada localización su objetivo es tener el estado en 0 
        Se indica que 0 es la fruta aun verde y 1 que la fruta esta totalmente madura lista para cosechar
        Se inicializa en el costo 0
    """
    zona_4 = {'D': '0'}
    costo = 0
    #Nombre de la zona
    print("\nZona 4 Otongo - Reproducción de Fresas \n")
    #Variable de la zona 4 que permitira ingresar por consola al usuario
    localizacion_D = input("Digite si las fresas de la zona estan cosechadas (0) o si las fresas estan por cosechar (1) : ") 
    #Objetivo alcanzar del zona 4
    print("Objetivo en alcanzar: " + str(zona_4))
        #Se condiciona la localizacion que tomara el valor del usuario y ejecutara la acción determinada 
        #para el robot si realiza una accion aumentara el costo caso contrario se mantendra con su
        #valor inicial 
    if localizacion_D == '1':
            #La zona se encuentra cosechada
            print("La zona 4 se encuentra en estado de cosecha.")
            #Aumenta el costo del agrobot
            zona_4['D'] = '0'
            costo += 1 #Imprime el mensaje de exito junto con el nuevo costo
            print("La zona 4 ya ha sido cesechada con exito.")
            print("Costo actual: " + str(costo))
            
    else:
        #La zona de cultivo se encuentra cosechada. Por lo tanto no se realiza ninguna acción
        print("La zona 4 se encuentra en estado de crecimiento de las fresas.")
        print("Costo actual: " "("+ str(costo)+")")
    #Se imprimira el resultado de la zona de cultivo seleccionado, alcanzo el objetivo con el costo.    
    print("Estado de la zona 4: ")
    print(zona_4)
    print("Medición del rendimiento: " + str(costo))

#******************************************************************************************************************

#Se define la función que pertence a la zona 5
def Zona_5():
    """ Se inicializa la zona_5
        Para cada localización su objetivo es tener el estado en 0 
        Se indica que 0 es la fruta aun verde y 1 que la fruta esta totalmente madura lista para cosechar
        Se inicializa en el costo 0
    """
    zona_5 = {'E': '0'}
    costo = 0
    #Nombre de la zona
    print("\nZona 5 Naranjos - Reproducción de Fresas \n")
    #Variable de la zona 5 que permitira ingresar por consola al usuario
    localizacion_E = input("Digite si las fresas de la zona estan cosechadas (0) o si las fresas estan por cosechar (1) : ") 
    #Objetivo alcanzar del zona 5
    print("Objetivo en alcanzar: " + str(zona_5))
        #Se condiciona la localizacion que tomara el valor del usuario y ejecutara la acción determinada 
        #para el robot si realiza una accion aumentara el costo caso contrario se mantendra con su
        #valor inicial 
    if localizacion_E == '1':
            #La zona se encuentra cosechada
            print("La zona 5 se encuentra en estado de cosecha.")
            #Aumenta el costo del agrobot
            zona_5['E'] = '0'
            costo += 1 #Imprime el mensaje de exito junto con el nuevo costo 
            print("La zona 5 ya ha sido cesechada con exito.")
            print("Costo actual: " + str(costo))
            
    else:
        #La zona de cultivo se encuentra cosechada. Por lo tanto no se realiza ninguna acción
        print("La zona 5 se encuentra en estado de crecimiento de las fresas.")
        print("Costo actual: " "("+ str(costo)+")")
    #Se imprimira el resultado de la zona de cultivo seleccionado, alcanzo el objetivo con el costo.    
    print("Estado de la zona 5: ")
    print(zona_5)
    print("Medición del rendimiento: " + str(costo))

#******************************************************************************************************************
#Se define la función que pertence a la zona 6
def Zona_6():
    """ Se inicializa la zona_6
        Para cada localización su objetivo es tener el estado en 0 
        Se indica que 0 es la fruta aun verde y 1 que la fruta esta totalmente madura lista para cosechar
        Se inicializa en el costo 0
    """
    zona_6 = {'F': '0'}
    costo = 0
   #Nombre de la zona
    print("\nZona 6 Congoma - Reproducción de Fresas \n")
    #Variable de la zona 6 que permitira ingresar por consola al usuario
    localizacion_F = input("Digite si las fresas de la zona estan cosechadas (0) o si las fresas estan por cosechar (1) : ") 
    #Objetivo alcanzar del zona 6
    print("Objetivo en alcanzar: " + str(zona_6))
        #Se condiciona la localizacion que tomara el valor del usuario y ejecutara la acción determinada 
        #para el robot si realiza una accion aumentara el costo caso contrario se mantendra con su
        #valor inicial 
    if localizacion_F == '1':
            #La zona se encuentra cosechada
            print("La zona 6 se encuentra en estado de cosecha.")
            #Aumenta el costo del agrobot
            zona_6['F'] = '0'
            costo += 1 #Imprime el mensaje de exito junto con el nuevo costo
            print("La zona 6 ya ha sido cesechada con exito.")
            print("Costo actual: " + str(costo))
            
    else:
        #La zona de cultivo se encuentra cosechada. Por lo tanto no se realiza ninguna acción
        print("La zona 6 se encuentra en estado de crecimiento de las fresas.")
        print("Costo actual: " "("+ str(costo)+")")
    #Se imprimira el resultado de la zona de cultivo seleccionado, alcanzo el objetivo con el costo.    
    print("Estado de la zona 6: ")
    print(zona_6)
    print("Medición del rendimiento: " + str(costo))

#******************************************************************************************************************

#Se define la función que pertence a la zona 7
def Zona_7():
    """ Se inicializa la zona_1
        Para cada localización su objetivo es tener el estado en 0 
        Se indica que 0 es la fruta aun verde y 1 que la fruta esta totalmente madura lista para cosechar
        Se inicializa en el costo 0
    """
    zona_7 = {'G': '0'}
    costo = 0
    #Nombre de la zona
    print("\nZona 7 Mapali - Reproducción de Fresas \n")
    #Variable de la zona 7 que permitira ingresar por consola al usuario
    localizacion_G = input("Digite si las fresas de la zona estan cosechadas (0) o si las fresas estan por cosechar (1) : ") 
    #Objetivo alcanzar del zona 7
    print("Objetivo en alcanzar: " + str(zona_7))
        #Se condiciona la localizacion que tomara el valor del usuario y ejecutara la acción determinada 
        #para el robot si realiza una accion aumentara el costo caso contrario se mantendra con su
        #valor inicial 
    if localizacion_G == '1':
            #La zona se encuentra cosechada
            print("La zona 7 se encuentra en estado de cosecha.")
            #Aumenta el costo del agrobot
            zona_7['G'] = '0'
            costo += 1 #Imprime el mensaje de exito junto con el nuevo costo
            print("La zona 7 ya ha sido cesechada con exito.")
            print("Costo actual: " + str(costo))
            
    else:
        #La zona de cultivo se encuentra cosechada. Por lo tanto no se realiza ninguna acción
        print("La zona 7 se encuentra en estado de crecimiento de las fresas.")
        print("Costo actual: " "("+ str(costo)+")")
    #Se imprimira el resultado de la zona de cultivo seleccionado, alcanzo el objetivo con el costo.    
    print("Estado de la zona 7: ")
    print(zona_7)
    print("Medición del rendimiento: " + str(costo))

#******************************************************************************************************************

opcion=1
while opcion != 8:
    """ Se define el programa del robot estableciendo un meno con 7 opciones correspondientes a las zonas de cultivo
        Se inicializa con la variable opcion=1
        Con el bucle while se condiciona que si es diferente de ocho ingresa algunas de las opciones
    """
    print("\n\t**** AGROBOT SERIE E ****\n")
    #Se muestra las opciones
    print('1. Zona 1 Poste\n2. Zona 2 Peripa\n3. Zona 3 Chiguilpe\n4. Zona 4 Otongo\n5. Zona 5 Naranjos\n6. Zona 6 Congoma\n7. Zona 7 Mapali\n8.Salir')
    #El usuario ingresa la opción
    opcion = int(input('\nDigite la zona que desea supervisar: '))
    #Llama a las funciones ya determinadas
    if opcion == 1:
        Zona_1()
    elif opcion == 2:
        Zona_2()
    elif opcion == 3:
        Zona_3()
    elif opcion == 4:
        Zona_4()
    elif opcion == 5:
        Zona_5()
    elif opcion == 6:
        Zona_6()
    elif opcion == 7:
        Zona_7()
    elif opcion == 8:
        #Opción para salir del programa del agrobot E-Series
        print('\nAPAGANDO AGROBOT E-SERIES.....\n')
        print('.............\n')
        print('...ADIOS!!\n')
    else:
        #Mensaje de error al escoger un número erroneo que no se encuentra en el menu
        print("\nDIGITE UNA OPCION VALIDA DEL AGROBOT E-SERIES")  