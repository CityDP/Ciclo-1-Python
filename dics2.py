#Iniciar un diccionario vacío 
jugador = {}
print (jugador)

# Se une un jugador
jugador ['nombre'] = 'Juan'
jugador ['puntaje'] = 0
print  ( jugador)

#Incrementando el puntaje
jugador[ 'puntaje' ] = 200
print (jugador)

# Acceder a un valor
print ( jugador.get( 'consola', 'no existe ese valor'))

# Iterar en el diccionario
for llave, valor in jugador.items():
    #print(llave) #De la misma forma que se itera en la lista se puede iterar en el diccionario y en el objeto también es posible.
    print (valor)
    
# Eliminar jugador y puntaje 
del jugador[ 'nombre']
del jugador ['puntaje']
print (jugador)