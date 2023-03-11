
"""
@author: Augusto Fonseca and Rodrigo Dornelles
"""

# CaesarCipher

# contains collection of string constants
import string

# Create a class
class CaesarCipher:
    
    def __init__(self, rotate):
        self._characteres = list(string.ascii_uppercase)
        self._rotate = rotate
        print(f"Creating a new Ceaser Cipher with rotate value {rotate}")
    
    def encrypt(self, input):
        
        # make sure the input is uppercase
        input = input.upper()
        
        # transform the string in list
        input = list(input)
    
        # create an empty output
        output = []
        # loop through the list to change according with the rotation
        for letter in input:
            
            # if is not a letter keep as it is
            if letter not in self._characteres:
                output.append(letter)
            else:
                # identify the index of this letter
                index = self._characteres.index(letter)
                
                # identify the correspondent letter
                secret_letter = (index + self._rotate) % 26
                
                # append the new letter
                output.append(self._characteres[secret_letter])
        
        return "".join(output)
    
    def decrypt(self, input):
        
         # make sure the input is uppercase
        input = input.upper()
        
        # transform the string in list
        input = list(input)
    
        # create an empty output
        output = []
        # loop through the list to change according with the rotation
        for letter in input:
            
            # if is not a letter keep as it is
            if letter not in self._characteres:
                output.append(letter)
            else:
                # identify the index of this letter
                index = self._characteres.index(letter)
                
                # identify the correspondent letter
                secret_letter = (index - self._rotate) % 26
                
                # append the new letter
                output.append(self._characteres[secret_letter])
        
        return "".join(output)


