import os
import re
import time

mode = str(input("""M A D E B Y L O G I X # 4 2 2 4

Choose mode:
1 - Encode
2 - Decode

M A D E B Y L O G I X # 4 2 2 4\n"""))

if mode == "1" or "Encode" or "encode":
    chars = str(input("Enter chars to encode:\n"))
    key = int(input("Enter key:\n"))

    open('DONT DELETE ME.txt', 'w').close()

    with open("DONT DELETE ME.txt", "a") as file:
        for char in chars:
            charc = ord(char)
            charc = charc + key
            charc = str(charc)
            file.write(charc)
            file.write(", ")

    with open("DONT DELETE ME.txt", 'rb+') as filehandle:
        filehandle.seek(-2, os.SEEK_END)
        filehandle.truncate()

    with open("DONT DELETE ME.txt", "r") as file:
        print(file.read())

elif mode == "2" or "Decode" or "decode":
    key = int(input("Enter key:\n"))
    encoded = str(input("Encoded text (numbers):\n"))
    decode = [int(s) for s in re.findall(r'\b\d+\b', f'{encoded}')]
    for int in decode:
        int = int - key
        a = chr(int)
        print("\n", a, end = "")
