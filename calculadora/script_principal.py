from operaciones.entrarnumero.entrarnum import entrarnum
from operaciones.sumar.suma import suma
from operaciones.restar.resta import resta
from operaciones.multiplicar.multiplica import multiplica
from operaciones.dividir.divide import divide


#Funcion Entrada
# funciones


#def entrarnum():
#   while True:
#        try:
#            num = float(input('Entra un numero: '))
#            return num
#        except ValueError:
#            print('Valor incorecto, intente nuevamente.')

# def entra_num2():
#     while True:
#         try:
#             num2 = float(input('Entra el segundo numero: '))
#             return num2
#         except ValueError:
#             print('Valor incorecto, intente nuevamente.')
    

#def sumar(numA,numB):
#    suma = numA + numB
#    return suma

#def restar(numA,numB):
#    resta = numA - numB
#    return resta

#def multiplicar(numA,numB):
#    multi = numA * numB
#    return multi

#def dividir(numA,numB):
#    if numB == 0:
#        print('No es posible dividir un numero por cero.')
#    else:
#        div = numA/numB
#        print(f'El resultado de la división es: {div:.3f}')
    
        

#Función principal

def principal():
    prompt= '''
                Menu Calculadora
            Selecione una operación:\n
                1. Sumar
                2. Restar
                3. Multiplicar
                4. Dividir
                0. Salir
'''
    opcion = 0
    while opcion != '0':
        print(prompt)
        opcion = (input())
        if opcion == '1':
            print('Sumar:')
            #num1 = entrarnum()
            #num2 = entrarnum()
            print(f'El resultado de la suma es: {suma(entrarnum(),entrarnum())}')
        elif opcion == '2':
            print('Restar:')
            print(f'El resultado de la resta es: {resta(entrarnum(),entrarnum())}')
        elif opcion == '3':
            print('Multiplicar:')
            print(f'El resultado de la multiplicación es: {multiplica(entrarnum(),entrarnum())}')
        elif opcion == '4':
            print('Dividir:')
            divide(entrarnum(),entrarnum())
        elif opcion == '0':
            print('Fin del programa')
        else:
            print('Opción invalida')



# Llama principal()
principal()
