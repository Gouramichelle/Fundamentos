nombre = input("ingrese su nombre")
opcion = int(input("si quiere calcular area presione 1, \n si quiere calcular el perimetro presione 2"))

if opcion == 1:
    calculare= int(input ("escoje una figura de las siguiente: \n 1-triangulo \n 2-Rectangulo \n 3-cuadrado \n 4- circulo "))
    if calculare == 1:
        basetriang= int(input("ingrese base"))
        alttriang= int(input("ingrese altura"))
        print(  nombre,"el area del triangulo es: ",{basetriang * alttriang/2})
    elif calculare== 2:
        recta= int(input("ingrese el primer lado del rectangulo"))
        rectb= int(input("ingrese elsegundo lado del rectangulo"))
        print(nombre,"el area del rectangulo es: ", {recta*rectb})
    elif calculare== 3:
        cuadra= int(input("ingrese un lado del cuadrado"))
        print(nombre, "el area del cuadrado es: ",{cuadra**2})
    elif calculare== 4:
        rad= int(input("ingrese el radio del circulo"))
        print(nombre, "el area del circulo es: ",{rad * rad * 3.1416})
elif opcion == 2:
    calculper= int(input("escoje una figura de las siguiente: /n 1-triangulo /n 2-Rectangulo /n 3-cuadrado /n 4- circulo "))

    if calculper == 1:
        basetriang2= int(input("ingrese base"))
        alttriang2= int(input("ingrese altura 1"))
        alttriang22= int(input("ingrese altura 2"))

        print(  nombre,"el perimetro del triangulo es: ",{basetriang2+alttriang2+alttriang22})
    elif calculper== 2:
        recta2= int(input("ingrese el primer lado del rectangulo"))
        rectb2= int(input("ingrese elsegundo lado del rectangulo"))
        rectc= int(input("ingrese el tercer lado del rectangulo"))
        rectd= int(input("ingrese el cuarto lado del rectangulo"))
        print(nombre,"el area del rectangulo es: ", {recta2+rectb2+rectc+rectd})
    elif calculper== 3:
        cuadra2= int(input("ingrese un lado del cuadrado"))
        print(nombre, "el area del cuadrado es: ",{cuadra2*4})
    elif calculper== 4:
        rad2= int(input("ingrese el radio del circulo"))
        print(nombre, "el area del circulo es: ",{2 * rad2 * 3.1416})