print("Select mode: encrypt or decrypt\n")
prompt_mode = input("e/d: ").lower()
message = input("Enter message to encrypt: ").lower()
shift = int(input("Enter shift value: "))


def message_dec(message, shift):
    if prompt_mode == "d":
        d_message = ""
        for char in message:
            if char.islower():
                d_message += chr((ord(char) - shift - 97) % 26 + 97)
            else:
                d_message += char
    return d_message


print(message_dec(message, shift))
