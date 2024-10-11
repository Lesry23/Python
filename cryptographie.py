import string

def crypt(message, shift=1):

    caracteres = string.ascii_letters + string.digits + string.punctuation + " "
    resultat = ""
    for char in message:
        index = caracteres.find(char)
        if index != -1:
            resultat += caracteres[(index + shift) % len(caracteres)]
        else:
            resultat += char  # Si le caractère n'est pas dans la table, on le conserve
    return resultat

# Exemple d'utilisation
message = "Hello, World!"
message_crypte = crypt(message, 3)
print(message_crypte)  # Affichera : Khoor, Zruog!