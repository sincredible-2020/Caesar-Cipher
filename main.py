import string
alphabet = list(string.ascii_lowercase)

print("Welcome to Caesar Cipher")

process = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

message = input("Type your message:\n")
shift = int(input("Type your shift number:\n"))

def encode(message):
    letter = list(message.lower())
    for i in range(len(letter)):
        if letter[i] in alphabet:
            new_index = alphabet.index(letter[i]) + shift
            if new_index > (len(alphabet)-1):
                new_index = new_index - 25
                letter[i] = alphabet[new_index]
            else:
                letter[i] = alphabet[new_index]
    encrypted = ''.join(letter)
    return encrypted

def decode(message):
    letter1 = list(message.lower())
    for j in range(len(letter1)):
        if letter1[j] in alphabet:
            new_index = alphabet.index(letter1[j]) - shift
            if new_index < 0 :
                letter1[j] = alphabet[new_index-1]
            else:
                letter1[j] = alphabet[new_index]
    decrypted = ''.join(letter1)
    return decrypted


if process == "encode":
    print("Here's the encode result: ", encode(message))
elif process == "decode":
    print("Here's the encode result: ", decode(message))


