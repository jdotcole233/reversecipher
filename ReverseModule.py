class Encrypt:

    def __init__(self, text):
        self.text = text
    
    def encryption(self):
        reverse = ""
        length = len(self.text) - 1

        while length >= 0:
            reverse = reverse + self.text[length]
            length = length - 1
        
        return reverse



def userinput() -> str:
    try:
        user_input = input("Enter a text to be encrypted:\n> ")
    except ValueError:
        print('Invalid input')
    except KeyboardInterrupt:
        print("Keyboard interruption. Halting program..\n")

    return user_input
