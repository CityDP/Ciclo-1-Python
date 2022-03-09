lenguajes = [ 'Pyton', 'kotlin', 'Java',  'JavaScript']

print(lenguajes)

# Los arrays (lists) comienzan en la posisicón 0
print (lenguajes[2])

# Para ordenar los leguajes alfabeticamente usamos
lenguajes.sort()
print(lenguajes)

# Acceder a un elemento dentro de un texto
aprendiendo = f'estoy aprendiendo{lenguajes[3]}'
print (aprendiendo)

# Modificando valores de un list (arreglo), esto es muy util en los carritos de compras
lenguajes [2]='php'
print (lenguajes)

# Agregar elementos a un list (arreglo)
lenguajes.append('Ruby')
print (lenguajes)

#  Eliminar elemento de un list 1
del lenguajes [1]
print(lenguajes)

#  Eliminar elemento de un list 2
lenguajes.pop() # Eliminar el ultimo elemento 
print (lenguajes)

# Eliminar con pop una posición especifica
lenguajes.pop(0)
print(lenguajes)

# Eliminar por nombres
lenguajes.reove('php')
print (lenguajes)


