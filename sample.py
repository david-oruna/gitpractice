# Let's do some oop dummy program
from time import sleep
import sys 

# This is a list of banned names
# Not yet finished

banlist = ["Goat", "Cow", "Horse", "Cat", "Dog", "Bird", "Pig", "Fish"]

def printer(version):
    while True:
        try:
            take = input("Enter your name: ")
            
            if take.lower() in banlist:
                print("Not animals allowed")
                
                continue
            else:
                if take.isalpha():
                    
                    if take.lower() == "donkey":
                        print("XD")
                    elif take.lower() == "human":
                        print("Hey are u an alien? 👽")
                    else:
                        print("That's a cool name")
                        for i in take:
                            print("<3")
                    end = 'Finishing process .... '
                    for x in end:
                        sys.stdout.write(x)
                        sys.stdout.flush()
                        sleep(0.2)                  
                    break
                else:
                    print("Only letters!")
                    continue   
        except ValueError as e:
            print(f"Value error {e}")

        
            
# Now just call it
<<<<<<< HEAD
printer("Dog")

# Now then create another compliment
#def compliment():
=======
printer()
>>>>>>> 6c6425c38042633b6acfd326ba2e7f3a466eb1e7
