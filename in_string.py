def check_vowels():
    # Código a implementar utilizando input.
    #31/3/2025
    #TP3 - Rozas Miguel Agustin - Introduccion a la programacion 1
    # Ejercicio 1
    nombre = input()
    vocales = ['a','e','i','o','u']
    print("Contiene a:", vocales[0] in nombre.lower())
    print("Contiene e:", vocales[1] in nombre.lower())
    print("Contiene i:", vocales[2] in nombre.lower())
    print("Contiene o:", vocales[3] in nombre.lower())
    print("Contiene u:", vocales[4] in nombre.lower())
# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
