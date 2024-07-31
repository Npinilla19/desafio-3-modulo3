# Sentencias condicionales e iterativas (II)

Este compilado contiene tres proyectos que contemplan el uso de sentencias condicionales e iterativas en diferentes modalidades.

## Fuerza bruta


Este programa evalúa una contraseña ingresada por el usuario y calcula la cantidad de intentos necesarios para adivinarla carácter por carácter utilizando un enfoque de fuerza bruta con letras minúsculas.

### Descripción

El programa realiza los siguientes pasos:
1. Solicita al usuario que ingrese una contraseña.
2. Utiliza un bucle anidado para adivinar cada carácter de la contraseña.
3. Cuenta la cantidad de intentos necesarios para adivinar la contraseña completa.
4. Muestra la cantidad de intentos y la contraseña evaluada.

## Requisitos

- Python 3.x

## Uso

1. Clona este repositorio o descarga el archivo `password_evaluator.py`.
2. Ejecuta el script:
    ```sh
    python fuerza_bruta.py
    ```
3. Ingresa la contraseña cuando se te solicite.
4. El programa mostrará la cantidad de intentos necesarios para adivinar la contraseña.

## Ejemplo

```sh
Ingrese la contraseña a evaluar: ********
Cantidad de intentos: 36, contraseña a evaluar: abc