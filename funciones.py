#como crear una funcón
def informacion(): # 1. definmos la función
    print('soy Paola')  # esta indentado, pertenece a la función
print('soy Diana')  #no esta indnetado, no perteece a la función

informacion() #2. llamamos la función

# Funciones con parámetros y argumentos
def informacion (nombre):
    print ('soy {nombre }') # al correr el codigo nos muestra soy {nobre}
    print (f'soy {nombre}') # agregamos la f y ahora si nos va a mostrar los nombres

informacion ('Pedro')
informacion ('Itzel')
informacion ('Juan')

# ejemplo 2 de Funciones con parámetros y argumentos

def informacion (nombre, puesto):
    print (f'soy {nombre} y soy {puesto}')
informacion ('Pedro', 'programador')
informacion ('Itzel', 'diseñadora')
informacion ('Juan', 'no hace nada')

# Funciones que retornan valores
def informacion(nombre):
    return nombre # usamos el return, para procesar la informacón antes de mostrarla. 
empleado = informacón ('juan')
print(empleado)
 