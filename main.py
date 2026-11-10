print("You are in a room with both Mewtwo and Mew - you have to last 60 seconds without letting everything break loose - just the aura of both superior beings makes you tremble in fear - be careful of your every move.")
game_running = True

while game_running:
    print("Press 1 to stay and ask how their day is going, press 2 to desperately try to escape, Press 3 to talk about civil matters like a distinguished young gentleman. ")
    choice1 = input("You are stuck with the door locked completely \n")

    if choice1 == "1":
        print("You stay in the room and ask how their day is going")
        print("Mewtwo is disappointed in your idea of a conversation, but Mew loves it. Good ending")
    elif choice1 == "2":
        print("You bang on the door as hard as humanely possible, but to no avail.")
        print("Cooked - Mewtwo finds that exceptionally disrespectful, and Mew thinks you do not want to play - they both zap you to the Andromeda galaxy where you try to start a new life - terrible ending.")
    elif choice1 == "3":
        print("you make bread with JJ")
        print("You also WIN!!!")
    elif choice1 == "4":
        print("You find a Mewtwo's mega stone")
        print("After finding the mega stone, do you show Mewtwo or keep it to sell on the black market for moolah.")
        choice2 = input("Press 5 to show Mewtwo, or Press 6 to hide the mega stone in your pocket.\n")

        if choice2 == "5":
            print("You give back the Mega stone")
            print("Wait!! We have been searching for that! Mewtwo and Mew get shocked and as a sincere thank you they become your Pokemon")
            print("WON SECRET ENDING")
        elif choice2 == "100":
            print("You keep the mega stone")
            print("Then Mewtwo feels its presence")
            print("You slowly turn to face Mewtwo.... JUST TO GET VAPORIZED IN A MILISECOND")
            print("BAD SECRET ENDING")