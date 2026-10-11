def stripSpaces(myString):
    new_string = ""
    for char in myString:
        if char != " ":
            new_string += char
    return new_string

# El usuario introduce la frase antes de llamar a la función
phrase_input = input("Introduce una frase: ")
result = stripSpaces(phrase_input)
print(f"La frase sin espacios es: {result}")