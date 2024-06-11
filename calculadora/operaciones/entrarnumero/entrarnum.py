def entrarnum():
    '''
    Descripción:
    Introduzca un numero real con tratamiento de la entrada
    
    Entrada de datos:
     - Numero real
    
    Saída de datos:
     - El numero entrado con type == float
     
    '''
    while True:
        try:
            num = float(input('Entra un numero: '))
            return num
        except ValueError:
            print('Valor incorecto, intente nuevamente.')