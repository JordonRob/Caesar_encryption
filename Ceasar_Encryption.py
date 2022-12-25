alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def caesar(direction, text, shift):
    cipher_text = ""

    for letter in text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = position + shift
            if new_position > 25:
                new_position -= 26
        elif direction == "decode":
            new_position = position - shift
            if new_position < 0:
                new_position += 26

        cipher_text += alphabet[new_position]
    print(f"Here is the {direction}d result of {text}:  {cipher_text}")

    

caesar(direction, text, shift)

