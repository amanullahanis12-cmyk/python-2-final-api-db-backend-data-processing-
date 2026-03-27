"""
* Name         : Unit Tester
* Author       : Amanullah Anis
* Created      : 5/5/2025
* Course       : CIS189
* IDE          : Visual Studio
* Description  : Tests each function in Functions to see if they work
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""
#testing the Functions file and imports necessary modules for testing
from Functions import Methods
import datetime
import unittest
#Class made for testing methods.
class TestFinal(unittest.TestCase):
    #Makes sure limit_validating returns 0 for no spaces
    def test_limit_validation(self):
        testing = Methods()
        self.assertEqual(testing.limit_validating("hi"), 0)
    #Makes sure limit_validating returns 1 for one spaces
    def test_limit_validation2(self):
        testing = Methods()
        self.assertEqual(testing.limit_validating("hi there"), 1)
    #Makes sure value is raised if bat charachter is in it
    def test_number(self):
        with self.assertRaises(ValueError):
            testing = Methods()
            testing.number("1")
    #Makes sure value is raised if bat charachter is in it
    def test_number2(self):
        with self.assertRaises(ValueError):
            testing = Methods()
            testing.number("Hi there ?")
    #Makse sure current date is being returned
    def test_date(self):
        testdate = datetime.date.today()
        testing = Methods()
        self.assertEqual(testing.get_date(), testdate)
            
#Testing occurs
if __name__ == '__main__':
    unittest.main()