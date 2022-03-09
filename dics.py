#Creando un diccionario simple
cancion ={
    'artista': 'metalica', # llave y valor
    'cancion': 'enter Sandman',
    'lanzamiento' : 1992,
    'likes': 300
}
print(cancion)

#Acceder a los elementos del diccionario
print(cancion['artista'])

#Mezclar con un string
artista = cancion['artista']
print(f'estoy escuchando {artista}')

#Agregar nuevos valores
cancion['playlist']='Heavy Metal'
print(cancion)

# Reemplazar valor existente
cancion['cancion']='Seek & Destroy'
print(cancion)

# Eliminar valor
del cancion['lanzamiento']
print (cancion)