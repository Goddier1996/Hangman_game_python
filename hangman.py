import random # הפעלת שיטה רנדומלית
import datetime # הפעלת זמן

# מילים שקיימים ברשימה
wordList = {1:'ferrari',2:'ford',3:'bugatti',4:'maserati'
             ,5:'bentley',6:'maclaren',7:'lamborghini',8:'BMW',
             9:'mercedes',10:'pagani'}


######################################################################################################

def menu():# תפריט ראשי
     
    print("*********************************Home Menu**************************************\n")
    
    print("A: Start a Game")
    print("B: more Info about Game")
    print("C: Show all word's we have in Dictionary")
    print("D: Show all info Players")
    print("E: exit")

    choice = input("Please enter your choice: ")

    print(" ")
    
    if choice == "A" or choice == "a":
        word = getWord(wordList)
        play(word)
        

    elif choice == "B" or choice == "b":
        Info()
        print("*******************************************************************************\n")
        menu()

        
    elif choice == "C" or choice == "c":
        print("All word's in Dictionary:\n")
        ShowAllDictionary(wordList)
        print("*******************************************************************************\n")
        menu()

            
    elif choice == "D" or choice == "d":     
       InfoPlayers()
       print("*******************************************************************************\n")
       menu()

       
    elif choice == "E" or choice == "e":
        exit()

        
    else:
        print("You must only select either A - E")
        print("Please try again")
        menu()


        
######################################################################################################

def menuInGame():# תפריט משחק

    print(" ")
    print("*********************************Game Menu**************************************\n")


    print("A: Play playAgin this game")
    print("B: Back to menu")

    choice = input("Please enter your choice: ")


    if choice == "A" or choice == "a":
        playAgin()
        
    elif choice == "B" or choice == "b":
        menu()
     
    else:
        print("You must only select enter A - B")
        print("Please try again")
        menuInGame()


        
######################################################################################################
        
def getWord(wordList):# לקיחת מילים מרשימה ולהגריל אותם בשיטה רנטומלית
    
    word = random.choice(wordList) # הגרלת מילה מתוך הרשימה
    
    return word.upper() # upper הופך את המילה לאותיות גדולות



######################################################################################################

def play(word):#משחק

    print("Hello bro what your name ?")# פרטי משתמש
    name = input()
    
    timeStartGame = datetime.datetime.now()# הצגת זמן תחילת זמן
    print("\n")
    print("Let's play "+ name + "\n")

    word_completion = "_" * len(word)  
    guessed = False
    guessed_letters = []
    tries = 6  # מספר ניסיונות,ניקוד
    
    
    print(displayHangman(tries))
    print(word_completion)
    print("\n")
    
    while guessed == False and tries > 0:

        print(" ")
        
        # שואל עם משתמש צריך עזרה
        NeedHelp = input("""Do you need help(yes/no)?""")

        if NeedHelp == "yes" or NeedHelp == "YES":
            
              # אופציות של עזרה
          print("Help in Game:")
          print("A: to ask Admin")
          print("B: Call a friend")
          print("C: See word what you need Now")
          print("D: See what length word was")
          
          choice = input("Please enter your choice: ")    


          if choice == "A" or choice == "a":# עזרה א        
            HelpInGame()


          if choice == "B" or choice == "b":# עזרה ב
            HelpInGameFrind()


          if choice == "C" or choice == "c":# עזרה ג
            print("The word you need now for Win this Game:")
            print(word)
            

          if choice == "D" or choice == "d":# עזרה ד
            print("The length word was : " + str(len(word)))
            
            


        elif NeedHelp == "no" or NeedHelp == "NO":
            print("")


        elif NeedHelp != "no" or NeedHelp != "NO" or NeedHelp != "yes" or NeedHelp != "YES":
            print("You don't print NO or Yes!!!")
             
        
        print(" ")
        guess = input("guess a letter or word: ").upper()# קליטת אות
        
        
        if len(guess) == 1 and guess.isalpha():# אם אורך הקליטה 1 וגם זה אות תעשה את הבדיקות

                        
            if guess in guessed_letters:# אם הוקלד כבר אותה אות
                print("you already tried", guess, "!")
                
                
            elif guess not in word:# אם האות לא קיימת ברשימה
                print(guess, "isn't in the word :(")
                tries -= 1# ניקוד מתוך 6
                
                
            else:# שמירת אות במערך אם היא נכונה
                print("Nice one,", guess, "is in the word!")
                guessed_letters.append(guess)# append = הוספת אות למערך
                word_as_list = list(word_completion)
                indices = [saveLetter for saveLetter, letter in enumerate(word) if letter == guess]# שמירה בספריה לפי אות 1 שמירה במערך
                # עובר בלולאה של המילה ובודק אם הקליטה של המשתמש כלומר האות קיימת במילה
                
                
                for index in indices:
                    word_as_list[index] = guess
                    
                word_completion = "".join(word_as_list)# join = לעשות רווח בין האותיות

                
                if "_" not in word_completion:# אם אין מקום פנוית תהפוך את המשתנה לנכון ותסגור את הלולאה
                    guessed = True

              
        else:# אם תיהיה שגיאה והאות לא מתאימה תדפיס הודעה ואת הציור המתאים לפי הניקוד
            print("invalid input")
            
            
        print(displayHangman(tries))# הצגת איש תלוי לפי מערך 
        print(word_completion)# הצגת מילה
        print("\n")
        

         
    if guessed == True:# אם הכל נכון תדפיס ותחזור לתפריט
        print("Good Job " + name + " you Win this game!\nYou have attempts left :")
        print(tries)
        
        print("time when you start this game")# הצגת זמנים התחלת מזמן וסיום משחק
        print(timeStartGame.strftime("%X"))# הצגת זמן של תחילת זמן
        print("finish time")
        timeEndGame = datetime.datetime.now()# הצגת סיום של משחק
        print(timeEndGame.strftime("%X"))

        
        
                      # הכנסת מידע של שחקן לתוך קובץ חדש
        fileGame = open(r"C:\Users\artiom\Desktop\Gamefile.txt", "a")
        
        fileGame.write("Info Player:\n\n" )
        fileGame.write("name Player : " + name + "\nYou have attempts left : ")# שם
        fileGame.write(str(tries) + "\n")# מספר ניחושים
        fileGame.write("The word was this game : " + word + "\n" )#הצגת מילה
        fileGame.write("The length word was this game : " + str(len(word)) + "\n" )#הצגת אורך מילה
        fileGame.write("Start The game : " + timeStartGame.strftime("%X") + "\n")# התחלת משחק
        fileGame.write("End The game : " + timeEndGame.strftime("%X") + "\n")# סיום משחק
        fileGame.write("------------------------------\n")

        
        fileGame.close()

        menuInGame()

        
    else:# אם לא נכון תדפיס את ההודעה כי עבר מספר הניסיונות
        print("I'm sorry " + name +" , but you ran out of tries. The word was " + word + ". Maybe next time!")
        menuInGame()


        
######################################################################################################
        
def displayHangman(tries):# ציור של איש תלוי
    
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,# 0
                
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,# 1
                
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,# 2
                
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,# 3
                
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,# 4
                
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,# 5
                
                   """
                   -------- 
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """# 6
    ]
    return stages[tries]



######################################################################################################

def exit():# יציאה

 exit = False

 while exit == False: 
     
     choice = input("you wont Exit ? (yes/no)")

     if choice == "yes" or choice == "YES":
        print("bye Bro")
        exit = True
        break
        
     if choice == "no" or choice == "NO":
        menu()

     else:
         print("Erorr you didn't enter yes or no , try again !!")
         

        
######################################################################################################
        
def playAgin():# לשחק שוב
    
        word = getWord(wordList)
        play(word)


        
######################################################################################################
        
def Info():# מידע על המשחק
    
     print("info about How Play This Game :")
     print("in this game you have to guess the correct word,\nin each round of the game the word that has to be guessed changes. ")


     
######################################################################################################
     
def HelpInGame():# עזרה לבקש מ admin
    
    print("The hint we can give, a word guess of luxury vehicles that exist in the world.")


    
######################################################################################################

def HelpInGameFrind():# עזרה להתקשר לחבר
    
    print("Calling a friend = 052-8365428")
    print("Hi bro Maybe This Sports car")


    
######################################################################################################

def ShowAllDictionary(wordList):# הדפסת את כל במילים מהרשימה

    for x, y in wordList.items():
      print(x, y)


      
######################################################################################################

def InfoPlayers():# להציג מה שיש בתוך הקובץ כלומר מידע של השחקנים

    try:
        
     fileGame = open(r"C:\Users\artiom\Desktop\Gamefile.txt", "r")
     print(fileGame.read())
     
    except FileNotFoundError:
        
     print('There is nothing in the file , please start playing')


     
######################################################################################################

def main():
    
    print("                        Welcome to Hangman Game :\n") 
    menu()


if __name__ == "__main__":
    main()
