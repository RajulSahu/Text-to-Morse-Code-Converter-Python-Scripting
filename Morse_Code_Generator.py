MORSE_CODE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
}


def encryptor(text):
    encrypted = ""
    for letter in text:
        if letter != " ":
            encrypted = encrypted + MORSE_CODE_DICT.get(letter) + " "
        else:
            encrypted = encrypted + " "
    print(encrypted)


def decryptor(text):
    key_list = list(MORSE_CODE_DICT.keys())
    val_list = list(MORSE_CODE_DICT.values())
    space_found = 0
    morse = ""
    normal = ""
    for letter in text:
        if letter != " ":
            morse += letter
            space_found = 0
        else:
            space_found += 1
            if space_found == 2:
                normal = normal + " "
            else:
                normal = normal + key_list[val_list.index(morse)]
                morse = ""
    print(normal)


print("\n\n\t\tThe Morse Code Generator!")
ch = input("Enter 'E' to Encrypt or Enter 'D' to Decrypt : ")
if ch == "E":
    text_to_encrypt = input("Enter the text to Encrypt : ").upper()
    encryptor(text_to_encrypt)
elif ch == "D":
    text_to_decrypt = input("Enter the text to Encrypt : ").upper()
    decryptor(text_to_decrypt)
