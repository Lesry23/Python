import string
import unittest

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
            resultat += char 
    return resultat + str(pas)

def decrypt(message):

    pas = int(message[-1])
    message = message[:-1]  
    caracteres = string.ascii_letters + string.digits + string.punctuation + " "
    resultat = ""
    for char in message:
        index = caracteres.find(char)
        if index != -1:
            resultat += caracteres[(index - pas) % len(caracteres)]
        else:
            resultat += char 
    return resultat


class TestCryptDecrypt(unittest.TestCase):
    def test_crypt_decrypt(self):
        message = "Hello, World!"
        pas = 3
        message_crypte = crypt(message, pas)
        message_decrypte = decrypt(message_crypte)
        self.assertEqual(message, message_decrypte)

if __name__ == "__main__":
    unittest.main()