import json

concierto = input()   #ingresar los concieros que se áran y su valor
conciertos = json.loads(concierto)
Steven_quiere= input ()    # ingresar los conciertos a los que quiere asistir
quiere = Steven_quiere

print ( conciertos)
print ( quiere)  

# ver si lo que quiere steven esta en la programacion de conciertos 
for quiere in conciertos:
  # imprimir la cantidad que steven debe ahorrar
  valor=0
  if quiere == conciertos:
    valor +=conciertos.value()
    print (valor)
    # imprimir los concierto a los que steven puede asistir  
  if quiere == conciertos:
    print (quiere)
  else:  
    print (' ')