from operaciones.entrarnumero.entrarnum import entrarnum
from operaciones.sumar.suma import suma
from operaciones.restar.resta import resta
from operaciones.multiplicar.multiplica import multiplica
from operaciones.dividir.divide import divide

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
