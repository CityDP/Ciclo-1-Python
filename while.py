numero = 0  # Un error es, no poner el incremento, si dejamos solo el 0 se va generar un loop ∞ que puede tardar hasta que finalice toda la memoria.


# while numero <= 10:
#     print (numero)
#     numero += 1 #Incremento para evitar el loop ∞ 

# if dentro del while

while numero <= 10:
    if numero == 5:
        print ('CINCOOOO!!')
    else:
        print(numero)
    numero += 1 