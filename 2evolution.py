import unittest

def affiche(n1, n2):


    result = []
    for i in range(n1, n2 + 1):
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
    def test_affiche_5_10(self):
    
        output = affiche(5, 10)
        expected_output = "BuzzFizz78FizzBuzz"
        self.assertEqual(output, expected_output)

    def test_affiche_10_16(self):

        output = affiche(10, 16)
        expected_output = "Buzz11Fizz1314FrisBee16"
        self.assertEqual(output, expected_output)

    def test_affiche_1_1(self):

        output = affiche(1, 1)
        self.assertEqual(output, "1")

    def test_affiche_inverse(self):
        
        output = affiche(10, 5)
        self.assertEqual(output, "")

if __name__ == '__main__':
    unittest.main()