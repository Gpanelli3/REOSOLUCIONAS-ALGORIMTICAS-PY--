def alfabeto():
    abecedario='abcdefghijklmnopqrstuvxyz'
    frase=input('ingresar una frase')
    contador=0
    
    for i in range(0, len(frase)):
        for letra in abecedario:
            if frase[i] in letra:
                contador+=1
                    
    print(f'la ocurrencia en el abecedario de la frase {frase} es: {contador}')


def posinega():
    num=0

    while num != '*':
        num=input('ingresar un numero que se analizara si es positivo o negativo. \n si quiere salir ingrese * \n')
        if num>'0':
            print('es positivo')
        elif num<'0':
            print('es negativo')	
        else:
            print('es igual a cero')
    print('salio del programa \n ')
    


def enteros():
    nums=1
    acum=[]
    total=0
    contador=0

    while nums!=0:
        nums=int(input('\n ingresar numeros enteros. \n Cuando termine, ingrese cero para salir'))
        acum.append(nums)
        contador+=1
    
    for i in acum:
        total+=i
        promedio=total/(contador-1)
    print(f'\n la sumatoria de los numeros ingresados es {total}. \n Y el promedio es: {promedio}')


def suma():
    contador=[]
    acum=0
    ingreso=int(input('ingresar un numero, y se sumaran todos sus digitos'))

    for i in range(0,ingreso):
        contador.append(i)
    contador.append(ingreso)

    for i in contador:
        acum+=i
    print(f'\nel resultado de la sumatoria de los numeros del {ingreso} es: {acum}')



def menu():
    opcion=input('MENU EJERCICIOS\n 1-OCURRENCIA EN ALFABETO \n 2-NUMEROS NEGATIVOS O POSITIVOS\n 3-CALCULAR SUMATORIA Y PROMEDIO\n 4- MOSTRAR SUMATORIA DE SUS DIGITOS \n 5-SALIR')
    while opcion=='1' or opcion=='2' or opcion=='3' or opcion=='4':
    

        if opcion=='1':
            alfabeto()
            opcion=input('\n MENU EJERCICIOS\n 1-OCURRENCIA EN ALFABETO \n 2-NUMEROS NEGATIVOS O POSITIVOS\n 3-CALCULAR SUMATORIA Y PROMEDIO\n 4- MOSTRAR SUMATORIA DE SUS DIGITOS \n 5-SALIR')
            
        elif opcion=='2':	
            posinega()
            opcion=input('\n MENU EJERCICIOS\n 1-OCURRENCIA EN ALFABETO \n 2-NUMEROS NEGATIVOS O POSITIVOS\n 3-CALCULAR SUMATORIA Y PROMEDIO\n 4- MOSTRAR SUMATORIA DE SUS DIGITOS \n 5-SALIR')

        elif opcion=='3':
            enteros()
            opcion=input('\n MENU EJERCICIOS\n 1-OCURRENCIA EN ALFABETO \n 2-NUMEROS NEGATIVOS O POSITIVOS\n 3-CALCULAR SUMATORIA Y PROMEDIO\n 4- MOSTRAR SUMATORIA DE SUS DIGITOS \n 5-SALIR')
        elif opcion == '4':
            suma()
            opcion=input('\n MENU EJERCICIOS\n 1-OCURRENCIA EN ALFABETO  \n 2-NUMEROS NEGATIVOS O POSITIVOS\n 3-CALCULAR SUMATORIA Y PROMEDIO\n 4- MOSTRAR SUMATORIA DE SUS DIGITOS \n 5-SALIR')
        else:
            break

menu()
print('usted salio')
