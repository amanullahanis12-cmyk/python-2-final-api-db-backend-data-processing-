"""
* Name         : Functions
* Author       : Amanullah Anis
* Created      : 5/5/2025
* Course       : CIS189
* IDE          : Visual Studio
* Description  : Has simple methods to save space on the main file
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""
#Module imported
import datetime
#Class used for simple methods
class Methods:
    #Used to count spaces in a string
    def limit_validating(self, word):
        """
 Use reST style.

 :param parameter_1: A string to see if there spaces to count words.
 :returns: The amount of spaces to see how many words are there
 """
        #Variable for keeping track of spaces
        count = 0
        #Iterates through string
        for letter in word:
            #If there any spaces count gets 1 added to it
            if letter == ' ':
                count = count + 1
        #Returns number of spaces and used to keep track of word count
        return count
    #Used to validate if author has any charachters it should not have
    def number(self, input):
        """
 Use reST style.

 :param parameter_1: A string to see if there any numbers in it.
 :raises keyError: raises a ValueError if there any unnessarry charachters in it
 """
        #A set of charachters that are not valid inputs for authors name
        characters = set("1234567890!@#$%^&*()?|+=<>.-")
        #iterates through authors name
        for char in input:
            #iterates through every charchter in the set
            for num in characters:
                #if there are there will be an error raised
                if char == num:
                    raise ValueError
    #Used to get the current date
    def get_date(self):
        """
 Use reST style.

 :returns: The current day's date in year-month-day format
 """
        #Uses DateTime module to get date and then returns it
        today = datetime.date.today()
        return today

