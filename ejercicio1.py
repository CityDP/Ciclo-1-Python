playlist = {} # Diccionario vacio
playlist['canciones'] = [] # lista vaciia de canciones

# Función principal
def app():
    # agregar playlist
    agregar_playlist = True
    while agregar_playlist:
         nombre_playlist = input (' ¿Cómo deseas nombrar las playlist? \r\n')
         if nombre_playlist:
             playlist['nombre'] = nombre_playlist
             # ya tenemos un nombre, desactivar el true
             agregar_playlist = False
           
             #Mandar llamar la función para agregar canciones
             agregar_canciones()

def agregar_canciones():
    print('Agregar canciones')

app()