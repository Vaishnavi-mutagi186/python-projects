def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                result += chr(shifted)
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                result += chr(shifted)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


print("1. Encrypt")
print("2. Decrypt")

choice = input("Choose option (1/2): ")
message = input("Enter message: ")
shift = int(input("Enter shift value: "))

if choice == "1":
    print("Encrypted Message:", encrypt(message, shift))

elif choice == "2":
    print("Decrypted Message:", decrypt(message, shift))

else:
    print("Invalid choice")