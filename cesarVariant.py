def cifrado_cesar_personalizado(texto, salto):
    resultado = ""
    for caracter in texto:
        # Verifica si el caracter es una letra
        if caracter.isalpha():
            # Determina si el caracter es mayúscula o minúscula
            inicio = ord('A') if caracter.isupper() else ord('a')
            # Realiza el cifrado César con el salto proporcionado
            resultado += chr((ord(caracter) - inicio + salto) % 26 + inicio)
        else:
            # Si no es una letra, deja el caracter sin modificar
            resultado += caracter
    return resultado

# Solicitar al usuario el texto y el salto
texto_original = input("Ingrese el texto a cifrar: ")
salto = int(input("Ingrese el número de espacios para el cifrado: "))

# Aplicar el cifrado y mostrar el resultado
texto_cifrado = cifrado_cesar_personalizado(texto_original, salto)
print("Texto cifrado:", texto_cifrado)
