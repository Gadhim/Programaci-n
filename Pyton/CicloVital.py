nombre=input("Hola Guap@, por favor ingresa tu nombre: ")
edad=int(input("Ingresa tu edad por favor: "))
if (edad>=0 and edad<=5):
    print(nombre,"Tienes una edad de",edad,"y perteneces al grupo de primera infancia.")
elif (edad>=6 and edad<=11):
    print(nombre,"Tienes una edad de",edad,"y perteneces al grupo de pre-adolescente.")
elif (edad>=12 and edad<=18):
    print(nombre,"Tienes una edad de",edad,"y perteneces al grupo de adolescente.")
elif (edad>=19 and edad<=26):
    print(nombre,"Tienes una edad de",edad,"y perteneces al grupo de jovenes.")
elif (edad>=27 and edad<=34):
    print(nombre,"Tienes una edad de",edad,"y perteneces al grupo de adultez.")
elif (edad==35):
    print(nombre,"Tienes una edad de",edad,"lo cual significa que eres Máximo Décimo Meridio, Comandante de los ejércitos del norte, General de las legiones fénix, leal servidor del verdadero emperador Marco Aurelio, padre de un hijo asesinado, marido de una mujer asesinada, y alcanzaras tu venganza, en esta vida o en la otra.")
elif (edad>=36 and edad<=59):
    print(nombre,"Tienes una edad de",edad,"y perteneces al grupo de adultez.")
elif (edad>=60 and edad<=125):
    print(nombre,"Tienes una edad de",edad,"y perteneces al grupo de la Vejez.")
elif (edad>=126 and edad<=29999):
    print(nombre,"Tienes una edad de",edad,"por lo que probablemente seas hijo de Chabelo y la Reina de Inglaterra Isabel II.")
else:
    print(nombre,"Tienes una edad de",edad,"y perteneces al Sagrado Imperio de la Humanidad y debes rezar a nuestro santo patron y Dios Verdadero el Dios Emperador Cadaver de La Humanidad.")