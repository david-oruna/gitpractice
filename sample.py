# Let's code tetris

# Let's make a <3 printer



banlist = ["Goat", "Cow", "Horse", "Cat", "Dog", "Bird", "Pig"]

def fun():
    while True:
        try:
            take = input("Enter your name: ")
            if take.isalpha():
                
                if take.lower() == "donkey":
                    print("XD")
                elif take.lower() == "human":
                    print("Hey are u an alien? 👽")
                else:
                    print("That's a cool name")
                    for i in take:
                        print("<3")
                print('Finishing .. . . ')                  
                break
            else:
                print("Only letters!")
                continue   
        except ValueError as e:
            print(f"Value error {e}")

        
            
fun()