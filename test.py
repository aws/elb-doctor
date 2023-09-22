import os

def insecure_code(user_input):
    # Insecure use of os.system() which can lead to command injection
    os.system(user_input)

if __name__ == "__main__":
    command = input("Please enter a command to execute: ")
    insecure_code(command)
