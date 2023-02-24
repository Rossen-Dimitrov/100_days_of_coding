from caesar_art import logo


def caesar(text, sift, direction):
    encrypted_msg = ''
    for char in text:
        if char in alphabet:
            for i in range(len(alphabet)):
                if char == alphabet[i]:
                    if direction == "encode":
                        if i + shift >= len(alphabet):
                            i = i + shift - len(alphabet)
                            encrypted_msg += alphabet[i]
                        else:
                            encrypted_msg += alphabet[i + shift]
                        break
                    elif direction == "decode":
                        encrypted_msg += alphabet[i - shift]
                        break
        else:
            encrypted_msg += char
    print(f"Here is the {direction}d {encrypted_msg}")


print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


while True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(text, shift, direction)

    restart = input(" Do you want to restart the cipher program?\n"
                    "Type 'yes' if you want to go again. Otherwise type 'no'.")
    if restart == "yes":
        caesar(text, shift, direction)
    elif restart == "no":
        break
