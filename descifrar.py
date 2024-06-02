def decrypt_caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char
    return result

# Solicitar al usuario el texto cifrado y el salto utilizado para cifrar
cipher_text = input("Ingrese el texto cifrado: ")
shift_decrypt = int(input("Ingrese el número de espacios para descifrar: "))

# Aplicar el descifrado y mostrar el resultado
decrypted_text = decrypt_caesar_cipher(cipher_text, shift_decrypt)
print("Texto descifrado:", decrypted_text)
