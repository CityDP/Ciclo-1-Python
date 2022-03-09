playlist = {} # Diccionario vacio
playlist['canciones'] = [] # lista vaciia de canciones

def app():
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input (' ¿Cómo deseas nombrar las playlist? \r\n')
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False

            agregar_canciones()
def agregar_canciones():
    print ('agreegar canciones')
app()


