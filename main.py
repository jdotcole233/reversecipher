
from  ReverseModule import Encrypt, userinput


def run():
    start = True
    while start:
        try:
            choice = int(input("Choose:\n1.Encrpypt using reverse cipher\n2.Quit:\n> "))
            if choice == 1:
                user_input = userinput()

                if not user_input:
                    raise ValueError

                rvse = Encrypt(user_input)
                cipher = rvse.encryption()
                print("Cipher text is: '{}' \n".format(cipher))

            elif choice == 2:
                print("Ending program. GoodBye\n")
                start = False
            else:
                print("Invalid input, choose 1 or 2 :)\n")
                
        except ValueError:
            print("Value error")
        except KeyboardInterrupt:
            print("Keyboard interruption. Halting program..\n")
            start = False


if __name__ == "__main__":
    run()