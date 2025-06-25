def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char 
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)  

def main():
    print("=== Caesar Cipher Program ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()

    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter E or D.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return

    if choice == 'e':
        encrypted = caesar_encrypt(message, shift)
        print("Encrypted message:", encrypted)
    else:
        decrypted = caesar_decrypt(message, shift)
        print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()
