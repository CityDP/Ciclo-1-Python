pregunta = 'agrega un numero y te diré si es par o no \r\n'
pregunta += '(Escribe "cerrar" para salir de la aplicación) \r\n'
preguntar = True

while preguntar :
    # Mezclar con los operadores 
    numero = input (pregunta)
    
    if numero == 'cerrar':
        preguntar =  False
    else: 
        numero = int (numero)
        if numero % 2 == 0:
            print(f'El número {numero} es par')
        else:
            print (f' El número {numero} es impar')