# Revisar si una condición es mayor a 
balance = 500
if balance > 0:  # si  modificamos >0 a >501, el programa no muestra nada, por que lo toma como falso y lo finaliza. 
    print ('puedes pagar')

# if...Else
balance = 0
if balance > 0:
    print ('Puedes pagar')
else:
    print ('No tienes saldo')

#likes 
likes = 200
if likes == 200:
    print ('Excelente, 200 likes')
    
#likes 2
likes = 199
if likes >= 200:
    print ('Excelente, 200 likes')
else:
    print ('Casi llegas a los 200')

#If con texto
lenguaje = 'Python'
if lenguaje == 'Python':
    print('Excelente decisión')

# if con texto 2
lenguaje = 'PHP'
if not lenguaje == 'Python':  #En otros programas se usaría!= para negar una acción, pero e Python usamos el not después del if
    print('Excelente decisión')

#Evaluar un booleano
usuario_autenticado =  False
# if usuario_autenticado == True / lo pusimos asi solo para el ejempl, en un booleano solo se escribe las ondiciones asi:
if usuario_autenticado: 
    print ('acceso al sistema')
else:
    print ('debes iniciar sesión ')


# Evaluar un elemento de una lista

lenguajes = ['Python', 'Kotlin', 'Java','JavaScript']
if 'PHP' in lenguajes:
    print('PHP si existe')
else:
    print ('No no esta en la lista') #Nos sirve en el caso de un carrito de descuentos, para que el código corra y nos de los productos con descuento.

#if anidados
usuario_autenticado =  True
usuario_admiin = True
if usuario_autenticado:
    if usuario_admiin:
        print('ACCESO TOTAL')
    else: 
        print ('acceso al sistema')
else:
    print ('debes iniciar sesión ')

#ejemplo con elif
ocupación = 'desempleado'
if ocupación == 'estudiante':
    print ('Tienes 50% de descuento')
elif ocupación == 'jubilado':
    print (' tienes 75% de descuento')
elif ocupación == 'desempleado':
    print (' tienes 10% de descuento')
else:
    print('Debes pagar el 100%')

# Operador and

usuario_logueado =  True
usuario_admin = False
if usuario_logueado and usuario_admin:
    print ('Administrador')
elif usuario_logueado:
    print('acceso al sitema')
else:
    print('Debes iniciar sesión')

# Operador or
usuario_logueado =  True
usuario_admin = False
if usuario_logueado or usuario_admin:
    print ('Administrador')
elif usuario_logueado:
    print('acceso al sitema')
else:
    print('Debes iniciar sesión')

# list, iteradorese if en un ejemplo

#1
lenguajes = ['PHP', 'Kotlin', 'Java','JavaScript']
for lenguaje in lenguajes:
    print(lenguaje) #El for va ir iterando en cada uno de los elementos de la lista

# 2
lenguajes = ['Python', 'Kotlin', 'Java','JavaScript']
for lenguaje in lenguajes:
    if lenguaje == 'Python':
        print('Excelente, python')
    else:
        print(lenguaje)

#3
lenguajes = ['Python', 'Kotlin', 'Java','JavaScript']
for lenguaje in lenguajes:
    if lenguaje == 'Python':
        print(lenguaje.upper())
    else:
        print(lenguaje)