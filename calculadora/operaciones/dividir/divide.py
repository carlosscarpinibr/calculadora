def divide(numA,numB):
    '''
        - Descripción:
            Recibe dos numeros reales y los divide.
            Si el divisor es cero retorna un mensaje de error. 
        - Entrada de datos:
            Dos numeros reales de la función
        - Salida de datos:
            La multiplicación de dos numeros reales
    '''
    if numB == 0:
        print('No es posible dividir un numero por cero.')
    else:
        div = numA/numB
        print(f'El resultado de la división es: {div:.3f}')