Camila Giraldo Ramirez
Sebastian Ocampo Grajales

numeros_ingles = {'1':'one','2':'two','3':'three'}

def crear_registro():
    clave = input('Ingrese la clave del registro: ')
    valor = input('Ingrese el valor del registro: ')
    numeros_ingles[clave] = valor
    print(f'Registro creado: Clave: {clave}, Valor: {valor}')

def imprimir_registros():
    print('\nRegistros:')
    for clave, valor in numeros_ingles.items():
        print(f'Clave: {clave}, Valor: {valor}')

def eliminar_registro():
    clave = input('Ingrese la clave del registro a eliminar: ')
    if clave in numeros_ingles:
        del numeros_ingles[clave]
        print(f'Registro con clave {clave} eliminado.')
    else:
        print('La clave ingresada no existe en la base de datos.')

def editar_registro():
    clave = input('Ingrese la clave del registro a editar: ')
    if clave in numeros_ingles:
        nuevo_valor = input('Ingrese el nuevo valor para el registro: ')
        numeros_ingles[clave] = nuevo_valor
        print(f'Registro con clave {clave} editado. Nuevo valor: {nuevo_valor}')
    else:
        print('La clave ingresada no existe en la base de datos.')


while True:
    print('\nMenú:')
    print('1. Crear registro')
    print('2. Imprimir registros')
    print('3. Eliminar registro')
    print('4. Editar registro')
    print('5. Salir')

    opcion = input('Seleccione una opción: ')

    if opcion == '1':
        crear_registro()
    elif opcion == '2':
        imprimir_registros()
    elif opcion == '3':
        eliminar_registro()
    elif opcion == '4':
        editar_registro()
    elif opcion == '5':
        print('Saliendo del programa. ¡Hasta luego!')
        break
    else:
        print('Opción no válida. Por favor, seleccione una opción válida.')
