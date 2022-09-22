#Math Text adeventure game

import random

def Monster_health(a):

    #Using randomly assigned integers in a given range to get a different monster health each time
    M_health = random.randint(20, a) 

    #Changing it to a float to be able to subtract from player health
    M_health = float(M_health)

    return M_health

def Monster_attack(b):

    M_attack = random.randint(1, b)
    M_attack = float(M_attack)

    return M_attack

def Player_strength(c):

    strength = 0
    
    #Using a for loop to be able to increase strength 
    for i in range(c):

        strength += 10

        #Iterate through the loop
        i += 1

    return strength

def Player_attack(f, c):

    P_attack = random.randint(1, f) + random.randint(0, Player_strength(c)) 

    P_attack = float(P_attack) 

    return P_attack     

def Math_problem():
    a = random.randint(1,1000)
    b = random.randint(1,1000)
    solved = bool()

    #random.choice() chooses randomly from a list
    c = random.choice(["+", "-", "/", "*"])

    if c == "*":

        print(a, c, b)

        #Changing answer to a float from a string
        answer = float(input(""))

        if answer == (a * b):
            
            solved = True

        else:

            solved = False
    
    
    if c == "+":

        print(a, c, b)

        #Using an input to assign a value from the user
        answer = float(input(""))

        if answer == (a + b):
            
            solved = True

        else:

            solved = False

    if c == "/":

        #answer till the last decimal place
        print(a, c, b)
        answer = float(input(""))

        if answer == (a / b):
            
            solved = True

        else:

            solved = False

    if c == "-":

        print(a, c, b)
        answer = float(input(""))

        if answer == (a - b):
            
            solved = True

        else:

            solved = False

    print(solved)

    #Assigning a boolean value in order for the player attack to work
    return solved

def Battle(a, f, c, b, g, h):

    #Assigning a variable to another called function
    Mon_h = Monster_health(a)
    P_h = h
    P_a = Player_attack(f, c)
    print("Player Health = " , P_h)
    print("Player Strength = " , Player_strength(c))
    print("Monster Health = ", Mon_h )
    print("")

    while Mon_h > 0:

        if Math_problem() == True:
            
            print("")
            print("Player attack!! 🗡️")
            Mon_h -= P_a
                
        print("Monster Attack!!")
        M_a = Monster_attack(b)
        P_h -= M_a

        if M_a > g:

            #If randomly selected integer is above a certain value then it prints
            print("Critical attack!")

        print("")
        print("Player Health = " , P_h)
        print("Player Strength = " , Player_strength(c))
        print("Monster Health = ", Mon_h )

        if P_h <= 0:

            print("You eat some food and regain some health")
            P_h = 30
            print("Player Health = " , P_h)
    

if __name__ == "__main__":

    x = True

    #Making a list
    storage = ["🍖🍎"]

    #Using a while loop to execute the story
    while x == True:

        #Story starts now
        print("Welcome to the land of Mun where monsters have raveged the place.")

        #\n is used to go to next line in the terminal
        print("Only you can defeat the monsters with the power of math!\n")

        print("You come across a dungeon and see two different paths.")
        path = input("Do you take the left or right path\n")

        #Makes the string all uppercase
        path = path.upper()
        
        #Using if statements to do different paths
        if path == "L" or path == "LEFT":

            print("You follow the dark left path until you come across a hurt person in a dead end.")
            print("Jolie: Help!")
            print("The Evil Monster has kidnapped my brother!")
            Answer = input("Can you help him?\n")
            Answer = Answer.upper()

            if Answer == "Y" or Answer == "YES":
                print("Jolie; Thank you for helping me 😊")
                print("you go back and take the right path and walk for a long time until...")

                #Using funky text to make it look like a monster
                print("🐉: G͛͌͠r̿͛͠r͊͘͠e͒̐͛ḧ́͒͘h̽̕e̓̿̚h̀̒͘j͐̚͝d̓͠͝n̔̕̚ń͆͝r͋̾r͐͑͒!!\n")

                #Calling the battle function
                Battle(40, 10, 1, 10, 5, 100)

                print("")
                print("Congrats you have defeated the monster\n")
                print("You eat food to replenish your health")
                print("You continue on until you find a tresure chest")
                print("In the tresure chest there is a potion\n")

                Answer = input("Do you drink the potion now or later\n")
                Answer = Answer.upper()

                if Answer == "NOW" or Answer == "N":
                    
                    print("")
                    print("You drink this potion and replenish you health and gain strength.\n")

                    print("Player Health = 100")
                    print("Player Strength = 20\n")
                    s = 2
                    p = True

                elif Answer == "LATER" or Answer == "L":
                    print("You store the potion for later\n")

                    #Adds the string to the end of the list
                    storage.append("✨🏺✨")
                    print(storage)
                    s = 1
                    p = False

                print("You explore for a while until you come across a large monster...")
                print("👹: A̴͖͔̙̚̚r̴͕͖̼̔̐͝t̵̡̞͉̾̿e̴̝͚̙̐̽̕h̸̼͎̟́͌͠h̴̘̪̒̈́̓e̵͕̟̞͆́͋h̸͚̘͕͒͒̈́j̵͖͕̙̐͝d̴̘͔͚̔̈́̓n̴͓̼̔̿͌n̸̡͍͔͆̓͝d̵̟̝̓́͜͠!!\n")

                #Changing the parameters to make the monster harder to battle
                Battle(100, 10, s, 20, 5, 100)

                print("")
                print("Congrats you have defeated the monster\n")
                print("You eat food to replenish your health\n")

                if p == True:
                    print("You come across a mysterious flower 🌸")
                    print("You decide to eat the flower 🌸 and drink the potion ✨🏺✨ as you are mentally tired\n")

                    
                    print("You feel recharged and have gained new stats\n")
                    print("Player Health = 300")
                    print("Player Strength =  30\n")

                else:
                    print("You come across a mysterious flower 🌸")
                    print("You decide to eat the flower 🌸 as you are mentally tired\n")

                    
                    print("You feel recharged and have gained new stats\n")
                    print("Player Health = 300")
                    print("Player Strength =  30\n")  

                print("???: o̺͔ʅ̘͚̘ʅ̦͖͕ǝ̺̺͙ɥ̡͙͕\n")
                print("You turn around and see the ghost with a child around Jolies age.")
                print("Child: Help me!!!")
                print("¡̵͓̙̈́̐͜͝¡̵̡̠̫͒̐́¡̴͚̝̫͑̿͑ʇ̵͓͇͆͋̀s̸̠̪̦̔͊͘ɹ̸͍͑͜͝ᴉ̵͉̠͎̾́̀ⅎ̵̫̪̻̓͛̕ ǝ̸͓͕̠͌̀͝ɯ̵͕͚͖͋̔͝ ʇ̸͍̙͆͛̿ɐ̸̠̝͉̽͋͝ǝ̵̢̟͖͛̽̒ⅎ̵͙͓͓͛̚ǝ̴̻̟͚̐̽͛ṕ̵̡̝͆͆͜ o̴̝͔̘͋͛͘ʇ̸͍͚̦̿̿ ǝ̸͉̝̪͒̒͊ʌ̵̢̪̝́̓̈́ɐ̵͓͕̠͑͒͌ɥ̴͕͉̈́̔̕ ʅ̸̫̠̙̾͝͠ʅ̴̺͐͋͑͜ᴉ̴̡͚̞̿̿̕ʍ̸̞̦̾̓͆ n̸͕͎̙̓͑͐o̴̢͚̓̐̒ʎ̵̙͎̀͋͐ p̵͖̪̟̀̀͘ʅ̵̼̺͛͛͜ᴉ̵̢͓͙͊͒͆ɥ̵͕͚̐͛̕ɔ̸͓͓̝̐͑̕ ǝ̵̞͙̫̿̀̈́ɥ̵̦͖̫̈́͒̀ʇ̴̡͕̪̿͘͘ ʇ̸͕̦͔͑̐͌u̵̡̘̼͌͌̽ɐ̸͙͍͕̓̚̚ʍ̵̼̻̝͐̒̈́ n̴̡͎̈́͒͘͜o̵͔͓̙̿͐́ʎ̴͖̪͚̽́͋ ⅎ̴͔̺͌̚̕ Ḯ̵̢̪̼̓͘\n")

                Battle(500, 30, 3, 30, 18, 300)

                print("👻: o̵̠̟̝͊͘͝o̵̝̟̺͌̀͝o̵͓̠͓̔͊o̵͇̻͍̾͑o̵̻͉͖͑͊͝o̴̡̢͎̔̽̈́o̴͚͉̾͋͘o̸̢͕͖͊̈́̚o̸̢̺͖̽̓͘ö̸͚͚̠́͐̚ò̴̢̫̈́̽͜o̴̢͇͙͑̔͘o̸͍͙̒̽̔͜ò̵̢͖͙̓̓ò̸̡͓̠̚o̵̟̦̻͛̔͠o̵̡͎͎͌͑̔o̴̢̼̝͊̕̚o̴̫̠̙͑͐̓o̵̺̝͔̿̓͠Ǹ̵̙̘̫͝\n")
                print("Congrats you have defeated the ghost\n")

                r = True

                #To exit out of the while loop
                x = False

            elif Answer == "NO" or Answer == "N":

                print("Jolie: Please you have to help him!! 🙏")
                print("He's my only family left 😭😭😭\n")

                print("While you are trying to calm down Jolie a monster sneaks up to you.\n")

                Battle(40, 10, 1, 10, 5, 100)

                print("")
                print("Congrats you have defeated the monster\n")
                print("You eat food to replenish your health\n")

                print("After dealing with Jolie and the monster, you decide to leave this kingdom")

                r = False
                x = False

        if path == "R" or path == "RIGHT":

            print("🐉: G͛͌͠r̿͛͠r͊͘͠e͒̐͛ḧ́͒͘h̽̕e̓̿̚h̀̒͘j͐̚͝d̓͠͝n̔̕̚ń͆͝r͋̾r͐͑͒!!\n")

            Battle(40, 10, 1, 10, 5, 100)

            print("")
            print("Congrats you have defeated the monster\n")
            print("You eat food to replenish your health")
            print("You continue on until you find a tresure chest")
            print("In the tresure chest there is a potion\n")

            Answer = input("Do you drink the potion now or later\n")
            Answer = Answer.upper()

            if Answer == "NOW" or Answer == "N":
                
                print("")
                print("You drink this potion and replenish you health and gain strength.\n")

                print("Player Health = 100")
                print("Player Strength = 20\n")
                s = 2

            elif Answer == "LATER" or Answer == "L":

                print("You store the potion for later\n")
                storage.append("✨🏺✨")
                print(storage)
                s = 1

            print("You explore for a while until you come across a large monster...")
            print("👹: A̴͖͔̙̚̚r̴͕͖̼̔̐͝t̵̡̞͉̾̿e̴̝͚̙̐̽̕h̸̼͎̟́͌͠h̴̘̪̒̈́̓e̵͕̟̞͆́͋h̸͚̘͕͒͒̈́j̵͖͕̙̐͝d̴̘͔͚̔̈́̓n̴͓̼̔̿͌n̸̡͍͔͆̓͝d̵̟̝̓́͜͠!!\n")

            Battle(100, 10, s, 20, 5, 100)

            print("")
            print("Congrats you have defeated the monster\n")
            print("You eat food to replenish your health\n")

            print("You come across a mysterious flower 🌸")
            print("You decide to eat the flower 🌸 and drink the potion ✨🏺✨ as you are mentally tired\n")

            
            print("You feel recharged and have gained new stats\n")
            print("Player Health = 300")
            print("Player Strength =  30\n")
            s = 3

            print("???: o̺͔ʅ̘͚̘ʅ̦͖͕ǝ̺̺͙ɥ̡͙͕\n")
            print("You turn around and see the ghost with a child around Jolies age.")
            print("Child: Help me!!!")
            print("¡̵͓̙̈́̐͜͝¡̵̡̠̫͒̐́¡̴͚̝̫͑̿͑ʇ̵͓͇͆͋̀s̸̠̪̦̔͊͘ɹ̸͍͑͜͝ᴉ̵͉̠͎̾́̀ⅎ̵̫̪̻̓͛̕ ǝ̸͓͕̠͌̀͝ɯ̵͕͚͖͋̔͝ ʇ̸͍̙͆͛̿ɐ̸̠̝͉̽͋͝ǝ̵̢̟͖͛̽̒ⅎ̵͙͓͓͛̚ǝ̴̻̟͚̐̽͛ṕ̵̡̝͆͆͜ o̴̝͔̘͋͛͘ʇ̸͍͚̦̿̿ ǝ̸͉̝̪͒̒͊ʌ̵̢̪̝́̓̈́ɐ̵͓͕̠͑͒͌ɥ̴͕͉̈́̔̕ ʅ̸̫̠̙̾͝͠ʅ̴̺͐͋͑͜ᴉ̴̡͚̞̿̿̕ʍ̸̞̦̾̓͆ n̸͕͎̙̓͑͐o̴̢͚̓̐̒ʎ̵̙͎̀͋͐ p̵͖̪̟̀̀͘ʅ̵̼̺͛͛͜ᴉ̵̢͓͙͊͒͆ɥ̵͕͚̐͛̕ɔ̸͓͓̝̐͑̕ ǝ̵̞͙̫̿̀̈́ɥ̵̦͖̫̈́͒̀ʇ̴̡͕̪̿͘͘ ʇ̸͕̦͔͑̐͌u̵̡̘̼͌͌̽ɐ̸͙͍͕̓̚̚ʍ̵̼̻̝͐̒̈́ n̴̡͎̈́͒͘͜o̵͔͓̙̿͐́ʎ̴͖̪͚̽́͋ ⅎ̴͔̺͌̚̕IḮ̵̪̓͘\n")

            Battle(500, 30, s, 30, 18, 300)

            print("👻: o̵̠̟̝͊͘͝o̵̝̟̺͌̀͝o̵͓̠͓̔͊o̵͇̻͍̾͑o̵̻͉͖͑͊͝o̴̡̢͎̔̽̈́o̴͚͉̾͋͘o̸̢͕͖͊̈́̚o̸̢̺͖̽̓͘ö̸͚͚̠́͐̚ò̴̢̫̈́̽͜o̴̢͇͙͑̔͘o̸͍͙̒̽̔͜ò̵̢͖͙̓̓ò̸̡͓̠̚o̵̟̦̻͛̔͠o̵̡͎͎͌͑̔o̴̢̼̝͊̕̚o̴̫̠̙͑͐̓o̵̺̝͔̿̓͠Ǹ̵̙̘̫͝\n")
            print("Congrats you have defeated the ghost\n")

            r = True
            x = False

    #Exiting the while loop to end the story
    if r == True:

        print("Childe: Thanks for saving me back there\n")

        print("Everyone reaches back in town and you are celebrated as a hero\n")

        print("The End")

    elif r == False:

        print("You leave as a disgraced hero wandering the continent\n")

        print("The End")
