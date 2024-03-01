from string import ascii_letters, ascii_uppercase, digits
from random import randint, sample


class Passwords:
    def __init__(self) -> None:
        self.letters = ascii_letters
        self.lettersU = ascii_uppercase
        self.digits = digits
        self.spcl = "!$"
        self.minLength = 12

    def criteria(self, length:int) -> dict:
        """Validate minimum password length and provide password criteria for
        letter casing, special characters, and numbers based on the given
        length.
        
        Returns a dictionary with the password requirements."""

        criteria = {}
        if length >= self.minLength:
            """Generate x numbers, special characters, and upper
            cased letters based on length."""
            criteria['digits'] = int(length / 5)
            criteria['spcl'] = int(length / 6)
            criteria['upper'] = int(length / 6)
            criteria['remainder'] = length - (criteria['digits'] +
                                        criteria['spcl'] + criteria['upper'])
            return criteria
        else:
            exit('Password length does not meet the minimum critera of'
                 f' {self.minLength} characters.')


    def generate(self, length:int) -> str:
        """Generate a random password of x length"""

        def runX(charType, times:int) -> str:
            """Generate specific character type n number of times"""
            passAdd = ""
            for x in range(times):
                passAdd += charType[randint(0, len(charType)-1)]
            return passAdd
                        

        password = ""
        passCriteria = self.criteria(length)

        if passCriteria:
            password += runX(self.lettersU, passCriteria['upper'])
            password += runX(self.digits, passCriteria['digits'])
            password += runX(self.spcl, passCriteria['spcl'])
            password += runX(self.letters, passCriteria['remainder'])
            pwlen = len(password)
            return password[0] + ''.join(sample(password[1:pwlen], pwlen-1))
        else:
            return

        
if __name__ == '__main__':
    Passwords = Passwords()
