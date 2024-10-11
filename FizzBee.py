import unittest
import  affiche

class testfizzbee(unittest.TestCase):
        def test_affiche(self):
            output = affiche()
            excepted_output = "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee"
            self.assertEqual(output[:45], excepted_output)
if __name__ == '__main__':
        unittest.main()

def affiche():
    result = []
    for i in range (1, 101):
        if i % 15 == 0:
            result.append("FrisBee")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return ''.join(result)
