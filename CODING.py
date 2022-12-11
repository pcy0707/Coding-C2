 
Splash = """
   _____     _                 _      _____                      
  (_____)   | |               (_)    (_____)                     
     _  ____| | _   ____  ____ _        _ _   _ ____  ____   ___ 
    | |/ _  | || \ / _  |/ ___) |      | | | | |    \|  _ \ /___)
 ___| ( ( | | |_) | ( | | |   | |   ___| | |_| | | | | | | |___ |
(____/ \_||_|____/ \_||_|_|   |_|  (____/ \____|_|_|_| ||_/(___/ 
                                                     |_|         
"""
print(Splash)

Board = """

       0
       | 
       |
      _|_________________
     |      []
     |      []
     |      []
     /      []
  __/______/__\____
/                 `\~^~^~^~^~^~^~^~^~^

"""
#Defines Board so it can be called on later

BoardJump = """

                            ,
                            |
                            |
      ____________________  |
     |      []              0
     |      []             .|,
     |      []
     /      []              
  __/______/__\____        
/                `\~^~^~^~^~^~^~^~^~^

"""

GameOver = """

__   _______ _   _   _    _ _____ _   _                 
\ \ / /  _  | | | | | |  | |_   _| \ | |                
 \ V /| | | | | | | | |  | | | | |  \| |                
  \ / | | | | | | | | |/\| | | | | . ` |                
  | | \ \_/ / |_| | \  /\  /_| |_| |\  |                
  \_/  \___/ \___/   \/  \/ \___/\_| \_/                
                                                        
                                                        
 _____   ___  ___  ___ _____   _____  _   _ ___________ 
|  __ \ / _ \ |  \/  ||  ___| |  _  || | | |  ___| ___ \ 
| |  \// /_\ \| .  . || |__   | | | || | | | |__ | |_/ /
| | __ |  _  || |\/| ||  __|  | | | || | | |  __||    / 
| |_\ \| | | || |  | || |___  \ \_/ /\ \_/ / |___| |\ \ 
 \____/\_| |_/\_|  |_/\____/   \___/  \___/\____/\_| \_|

 """


def instructions():
    print("The game will give you questions, type the number next to the answers to choose the answer. Your goal is to jump of the diving board! If you succesfully jump of the board you win!")

    response = int(input("Please Type 1 to start the game\n"))

    if response == 1:
        openingStory()
        question1()

def openingStory():
    print("You and your dad arrive at the pool. You have a fun swimming lesson and now you have some free time.")

def question1():
#defines the first question

    print("What do you want to do?")

    print("")
    print("1. Look at people jumping off the diving board")
    print("2. Get some icecream")
    print("3. Go home")
    print("")

    response = int(input("Please Type 1, 2, or 3 to select one of the options\n"))
    #This allows the user to type a response

    if response == 1:
    #Gives the correct answer according to the response
        print("")
        print("You look at the people jumping off the board, it looks very high")
        print("")
        path1()
        #Calls the next question here
   
  
    elif response == 2:
        print("")
        print("You go get some ice cream")
        print("Wow that was some nice ice cream!")
        print("")
        path2()
    
  
    elif response == 3:
        print("")
        print("You leave the pool")
        print("You go home and rest")
        pathHome()
   
    
    else:
    #Allows the player to go back to the question if they provid an invalid answer
        print("")
        print("This is not a valid choice, please try again")
        print("")
        question1()


def path1():

    print("")
    print ("What do you want to do now?")

    print("")
    print("1. Try to jump off the board yourself")
    print("2. Go up closer and take a closer look")
    print("3. Leave")
    print("")


    response2 = int(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response2 == 1:
        print("")
        print("You are now right next to the board")
        print("")
        path1s1()
   
  
    elif response2 == 2:
        print("")
        print("You are now right next to the board, it looks so high!")
        print("")
        print("Another kid leaps off the board, up up up they go and down down down they come.")
        print("A big splash and they dissappear into the water.")
        print("")
        path1s2()
  
    elif response2 == 3:
        print("")
        print("You leave the pool and go home.")
        print("")
        pathHome()
   
    
        print("")
        print("This is not a valid choice, please try again")
        print("")
        path1()

    else:
        print("")
        print("This is not a valid choice, please try again")
        print("")
        path1()

def path1s1():

    print("")
    print("do you want to climb up?")

    print("")
    print("1. Yes")
    print("2. Stay there and watch a bit longer")
    print("3. Leave")
    print("")
 
  
    response = int(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response == 1:
        print("")
        print("You climb on the board, it looks so high")
        print("You stare down and it looks like you are above the clouds")
        pathBoard()
  
    elif response == 2:
        print("")
        print("You watch a bit longer")
        print("More people jump, SPLASH")
        print("you are now right next to the board")
        print("")
        path1s1()

    elif response == 3:
        print("")
        print("You leave the pool")
        print("You go home and rest")
        pathHome()
   
    
    else:
        print("")
        print("This is not a valid choice, please try again")
        print("")
        path1s1()

def path1s2():

    print("")
    print("More kids jump off the diving board")
    print("Do you want to climb up?")

    print("")
    print("1. Yes")
    print("2. Stay there and watch a bit longer")
    print("3. Leave")
    print("")

    response = int(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response == 1:
        print("")
        print("You climb on the board, it looks so high")
        print("You stare down and it looks like you are above the clouds")
        pathBoard()
  
    elif response == 2:
        print("")
        print("You watch a bit longer")
        print("More people jump, SPLASH")
        print("you are now right next to the board")
        print("")
        path1s2()

    elif response == 3:
        print("")
        print("You leave the pool")
        print("You go home and rest")
        pathHome()
   
    
    else:
        print("")
        print("This is not a valid choice, please try again")
        print("")
        path1s2()




def path2():

    print("")
    print("What do you want to do now")

    print("")
    print("1. Go to the pool")
    print("2. Go home")
    print("3. Eat some more food")
    print("")


    response = int(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response == 1:
        print("")
        print("You are now back at the pool")
        print("")
        path2s1()

    elif response == 2:
        print("")
        print("You are now at home")
        print("")
        pathHome()

    elif response == 3:
        print("")
        print("You eat many good food such as pizza and even more ice cream. Now you are really full")
        print("")
        path2s3() 

    else:
        print("")
        print("This is not a valid choice, please try again")
        print("")
        path2()


def path2s1():

    print("")
    print("What do you want to do?")

    print("")
    print("1. Start swimming again")
    print("2. Look at people jump off the diving board")
    print("3. Go home")


    response = int(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response == 1:
        print("")
        print("You swim some more, it was very fun!")
        print("")
        question1()

    elif response == 2:
        print("")
        print("You look at the people jumping off the board, it looks very high")
        print("")
        path1()

    elif response == 3:
        print("")
        print("You leave the pool")
        print("You go home and rest")
        pathHome()

    else:
        print("")
        print("This is not a valid choice, please try again")
        print("")
        path2s1()



def path2s3():

    print("")
    print("What do you want to do now?")

    print("1. Go to the pool")
    print("2. Go home")
    print("")

    response = int(input("Please Type 1 or 2 to select one of the options\n"))

    if response == 1:
        print("")
        print("You are now back at the pool")
        print("")
        pathPoolFull()

    elif response == 2:
        print("")
        print("You are now at home")
        print("")
        pathHome()

    else:
        print("")
        print("This is not a valid choice, please try again")
        print("")
        path2()

def pathPoolFull():

    print("")
    print("You are back at the pool. You tried to swim but you are too full to swim!")
    pathHome()

def pathHome():

    print("")
    print("You take some rest at home")

    print("Its the next day!")
    print("")
    openingStory()
    question1()

def pathBoard():

    print("")
    print(Board)
    print("On the board")
    print("It looks so high")
    print("Do you want to jump?")

    print("")
    print("1. Jump")
    print("2. Leave and try again next time")
    print("")


    response = int(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response == 1:
        print("")
        print("You are at the edge of the board")
        print("It looks so high")
        print("")
        pathBoardJump()

    elif response == 2:
        print("")
        print("You get off the diving board")
        print("")
        question1()

    else:
        print("")
        print("This is not a valid choice, please try again")
        print("")
        pathBoard()

def pathBoardJump():

    print("")
    print("you start to feel nervous, it looks sooo high")
    print("")

    print("")
    print("1. Take a few deep breaths and calm down")
    print("2. Continue moving forward")
    print("3. Get off the diving board and try to clam down")
    print("")

    response = int(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response == 1:
        pathBoardSuccess()

    elif response == 2:
        print("")
        print("You get too nervous and go home. Try again tomorrow")
        print("")
        pathHome()

    elif response == 3:
        print("")
        print("you climb down.")


    else:
        print("")
        print("This is not a valid choice, please try again")
        print("")
        pathBoardJump()


def pathBoardSuccess():

    print("")
    print("You are now calm and are now at the edge of the board. Do you jump into the pool?")
    print("")

    print("")
    print("1. Yes")
    print("2. No")
    print("")

    response = int(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response == 1:
        pathJump()

    elif response == 2:
        pathAsk()

    else:
        print("This is not a valid choice, please try again")
        print("")
        pathBoardSuccess()


def pathAsk():

    print("You climb down")
    print("You can try again tomorrow!")
    pathHome()


def pathJump():

    print("")
    print(BoardJump)

    print("")
    print("You take the leap of faith, you start falling. Before you know it, you hear a SPLASH, You did it.")
    print(GameOver)





validChoice = False
# global start

while (validChoice == False):
    #global validChoice
    #global start
    
    print("Welcome to Jabari Jumps!!!")
    start = int(input("Please type 1 to play, type 2 to view the instructions\n"))
    if start == 1:
        print("We will now start the game!")
        print("")
        validChoice = True
        openingStory() # here we call the first question directly
        question1()
    elif start == 2:
        print("I will now show you all the Commands and Instructions")
        print("")
        validChoice = True
        instructions()
    else:
        # this will take us back to the beginning of the loop to see this menu again
        print("This is not a valid choice, please try again")
        print("")
  
