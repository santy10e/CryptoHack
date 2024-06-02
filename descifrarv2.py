def decrypt_caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char
    return result

# Solicitar al usuario el texto cifrado
cipher_text = input("Ingrese el texto cifrado: ")

# Definir la secuencia de números de espacios
shift_values = range(1, 26)  # Ejemplo: del 1 al 10

# Iterar sobre la secuencia y aplicar el descifrado para cada número de espacios
for shift_decrypt in shift_values:
    decrypted_text = decrypt_caesar_cipher(cipher_text, shift_decrypt)
    print(f"Texto descifrado con {shift_decrypt} espacios:", decrypted_text)
