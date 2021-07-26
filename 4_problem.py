"""
GCD of two numbers using for loop
Example 1 :
Input 60,48
Output=12

"""

import unittest
def GCD_Loop( a, b):
    """
    def computeGCD(x, y):

    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i

    return gcd

a = 60
b= 48

# prints 12
print ("The gcd of 60 and 48 is : ",end="")
print (computeGCD(60,48))
    """
    pass
# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestGCD_Loop(unittest.TestCase):

    def test_01(self):
        input_nums = [60,48]
        output_num = 12

        self.assertEqual(GCD_Loop(input_nums[0],input_nums[1]), output_num)

    def test_02(self):
        input_nums = [54,24]
        output_num = 6

        self.assertEqual(GCD_Loop(input_nums[0],input_nums[1]), output_num)



if __name__ == '__main__':
    unittest.main(verbosity=2)
