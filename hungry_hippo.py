#!/usr/bin/python3
#DONE
import unittest
# --------------------------------------------------------------
class HungryHippo:
    '''
    Implement the __init__ function for a HungryHippo class, where
    each HungryHippo has a string "colour" that is an argument
    to its __init__ function. Additionally, each HungryHippo should have
    an int "grass_eaten" that starts at 0.

    Then create an instance method eat_grass(g) which adds an integer g 
    to the HungryHippo's grass_eaten.

    Then, implement the method below.
    '''
    def __init__(self, colour) :
        # GIVEN CODE
        self.colour = colour
        self.grass_eaten = 0

    def eat_grass(self, g):
        self.grass_eaten+=g

def hungriest_hippo1(list_of_hippos):
    '''
    Assumes list_of_hippos is a nonempty list of Hungry_Hippo objects.
    Changes the colour of the HungryHippo who has eaten the most grass
    to the string "green", and returns the HungryHippo who
    has eaten the least grass.

    For example, imagine you create a HungryHippo h1 with colour "blue"
    (via the syntax: h1 = HungryHippo("blue"), a HungryHippo h2 with 
    colour "purple", and a HungryHippo h3 with colour "turquoise". Then you 
    call h1.eat_grass(2), and h2.eat_grass(3). When you call the method 
    hungriest_hippo([h1, h2, h3]), it should change h2's colour 
    to "green", and return h3.
    '''
    fattestIndex=0
    fattestAmount=0
    for i in range(len(list_of_hippos)):
        if list_of_hippos[i].grass_eaten>fattestAmount:
            fattestAmount= list_of_hippos[i].grass_eaten
            fattestIndex=i

    list_of_hippos[fattestIndex].colour="green"

    skinnyAmount= fattestAmount
    skinnyIndex=0
    for i in range(len(list_of_hippos)):
        if list_of_hippos[i].grass_eaten <= skinnyAmount:
            skinnyAmount= list_of_hippos[i].grass_eaten
            skinnyIndex = i

    return list_of_hippos[skinnyIndex]

def hungriest_hippo(list_of_hippos):
    '''
    Assumes list_of_hippos is a nonempty list of Hungry_Hippo objects.
    Changes the colour of the HungryHippo who has eaten the most grass
    to the string "green", and returns the HungryHippo who
    has eaten the least grass.
    '''

    grass_amounts= [list_of_hippos[i].grass_eaten for i in range(len(list_of_hippos))]
    least_eater= min(grass_amounts)
    least_eater_index = grass_amounts.index(min(grass_amounts))
    greatest_eater = max(grass_amounts)
    greatest_eater_index = grass_amounts.index(max(grass_amounts))
    list_of_hippos[greatest_eater_index].colour="green"
    
    
    return list_of_hippos[least_eater_index]





# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        h1 = HungryHippo("blue")
        self.assertEqual(h1.colour, "blue")
        self.assertEqual(h1.grass_eaten, 0)
    def test2(self):
        h1 = HungryHippo("blue")
        h1.eat_grass(3)
        self.assertEqual(h1.grass_eaten, 3)
    def test3(self):
        h1 = HungryHippo("blue")
        h1.eat_grass(3)
        h1.eat_grass(2)
        self.assertEqual(h1.grass_eaten, 5)
    def test4(self):
        h1 = HungryHippo("blue")
        h2 = HungryHippo("purple")
        h3 = HungryHippo("turquoise")
        h1.eat_grass(4)
        h2.eat_grass(5)
        self.assertEqual(hungriest_hippo([h1, h2]), h1)
    def test5(self):
        h1 = HungryHippo("blue")
        h2 = HungryHippo("purple")
        h3 = HungryHippo("turquoise")
        h1.eat_grass(4)
        h2.eat_grass(5)
        ans = hungriest_hippo([h1, h2, h3])
        self.assertEqual(h2.colour, "green")
    def test6(self):
        h1 = HungryHippo("blue")
        h2 = HungryHippo("purple")
        h3 = HungryHippo("turquoise")
        h1.eat_grass(6)
        h2.eat_grass(5)
        ans = hungriest_hippo([h1, h2, h3])
        self.assertEqual(h1.colour, "green")
        self.assertEqual(ans, h3)
if __name__ == '__main__':
 unittest.main(exit=True)
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
