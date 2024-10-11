import unittest

def affiche(n):

    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FrisBee")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return ''.join(result)

class TestFizzBee(unittest.TestCase):
    def test_affiche_15(self):
        """Teste l'affichage jusqu'à 15."""
        output = affiche(15)
        expected_output = "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee"
        self.assertEqual(output, expected_output)

    def test_affiche_100(self):
     
        output = affiche(100)
        
        expected_output = "..."  
        self.assertEqual(output, expected_output)

    def test_affiche_0(self):

        output = affiche(0)
        self.assertEqual(output, "")

    def test_affiche_negatif(self):

        output = affiche(-5)
        self.assertEqual(output, "")

if __name__ == '__main__':
    unittest.main()