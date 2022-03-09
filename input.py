nombre = input ('Cuál es tu nombre: \r\n') # \r\n los usamos parea crear un salto de linea
print(f'Hola {nombre}')

#  Leer datos que serán números
edad = input ('Cual es tu edad')
# convertir edad (string) a int
edad = int(edad) # las entradas de datos, siempre vienen como strings, si vas a trabajar con números debes convertirlos a int, float y viceversa. 

if edad >=18:
    print (' Ya puedes votar')
else: 
    print ('aún no puedes votar')

# Mezclar con los operadores 
numero = input ('agrega un numero y te diré si es par o no \r\n')
numero = int (numero)

if numero % 2 == 0:
    print(f'El número {numero} es par')
else:
    print (f' El número {numero} es impar')