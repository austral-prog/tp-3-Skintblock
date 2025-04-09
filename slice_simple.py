def slice_simple():
    texto = "Awesome"
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.
    #31/3/2025
    #TP3 - Rozas Miguel Agustin - Introduccion a la programacion 1
    # Ejercicio 2
    first_three = texto[0:3]
    middle_text = int(len(texto)/2)
    middle_three = texto[middle_text-1:middle_text+2]
    first_four = texto[0:4]
    last_three = texto[-3:]
    print(first_three.lower())
    print(middle_three.lower())
    print(first_four.lower() + last_three.lower())


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
