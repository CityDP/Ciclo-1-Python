Arturo = input ()
Mario = input ()
Album = input ()
cont_arturo = 0
cont_mario = 0
for cancion in Album:
    if cancion  in Arturo:
        cont_arturo +=1
    if cancion  in Mario:
        cont_mario +=1
    if cont_arturo > cont_mario:
        print ('A', end='')
    elif cont_arturo < cont_mario:
        print ('M', end='')
    else:
        print('N', end='')