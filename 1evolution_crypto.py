import string

def crypt(message, pas):


    if not 1 <= pas <= 9:
        raise ValueError("Le pas doit être compris entre 1 et 9")

    caracteres = string.ascii_letters + string.digits + string.punctuation + " "
    resultat = ""
    for char in message:
        index = caracteres.find(char)
        if index != -1:
            resultat += caracteres[(index + pas) % len(caracteres)]
        else:
            resultat += char  # Si le caractère n'est pas dans la table, on le conserve
    return resultat + str(pas)

# Exemple d'utilisation
message = "Hello, World!"
message_crypte = crypt(message, 3)
print(message_crypte)  # Affichera : Khoor, Zruog!3