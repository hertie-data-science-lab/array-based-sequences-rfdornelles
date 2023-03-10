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
        
        print(f"Received the input:\n{input}")
        # make sure the input is uppercase
        input = input.upper()
        
        print(f"Received the input:\n{input}")
        
        # transform the string in list
        input = list(input)
        
        print(f"Received the input:\n{input}")
        # create an empty output
        output = []
        # loop through the list to change according with the rotation
        for letter in input:
            
            # if is not a letter keep as it is
            if letter not in self._characteres:
                output.append(letter)
                print(f"Output {letter}, {output}")
            else:
                # identify the index of this letter
                index = self._characteres.index(letter)
                
                # identify the correspondent letter
                secret_letter = (index + self._rotate) % 26
                
                # append the new letter
                output.append(self._characteres[secret_letter])
        
        return "".join(output)
# init

# method encrypt

# method decrypt

####

# convenient technique for performing string transformations is to create an equivalent list of characters, edit the
# list, and then reassemble a (new) string based on the list. 

# sending the string as a parameter to the constructor of the list class

# we can use a list of characters to build a string by invoking the join
# method on an empty string

# we can write the Caesar cipher with a rotation of r as a simple
# formula

# Replace each letter i with the letter (i + r) % 26

# #####

# a = "Teste"

# a = a.upper()

# a = list(a)

# a

# a = "".join(a)

# a

# # characters

# characters = list(string.ascii_uppercase)

# # ### encrypt

# input = "Teste".upper()
# input

# r = 10

# for i in input:
#     t = (characters.index(i) + r) % 26
    
#     print(i, t, characters[t])
    

# characters.index("I")