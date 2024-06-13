print("------------Welcome to the game zone:---------------")
print("Do you want to play single player or multi-player games: ")
print("Choose your option - ")
print("1.single player")
print("2.multiplayer")
p = int(input("Enter the  number"))
if p == 1:
    print("1.TIK-TAC-TOE")
    print("2.ROCK-PAPER-SCISSOR")
    print("3.KAUN BANEGA CROREPATI")
    print("4.HANGMAN GAME")
    a = int(input("Enter the number"))
    if a == 1:
        import numpy as np
      # game of tic-tac-toe
        def printGrid():
        for i in l:
            print(i)

        def initials():
            player1 = input("Enter your side X/O player -1").upper()
            if player1 == 'X': player2 = 'O'
        else             : player2 = 'X'
        print("Hence player-2 got", player2)
        return player1, player2
    
        def posToRowCol(pos):
            row = d[pos][0]
            col = d[pos][1]
            return row, col
    
        def chanceP1():
            while True:
                w = int(input("Choose the position for player1: "))
                row, column = posToRowCol(w)
                if l[row][column] not in 'OX':
                    l[row][column] = p1
                    printGrid()
                    return
                else: 
                    print('Position already taken.')
                            chanceP1()
        def chanceP2():
            #l = [1,2,3,4,5,6,7,8,9]
            while True:
                v = np.random.randint(1,9)
                #v = int(input("Choose the position for player2: "))
                row, column = posToRowCol(v)
                if l[row][column] not in 'OX':
                    l[row][column] = p2
                    printGrid()
                    return
                else:
                    print('Position already taken')
                    chanceP2()
        def getPlayer(ini):
            if ini == 'X':
                if p1 == 'X': return 'Player1'
                else        : return 'Player2'
            else:
                if p1 == 'O': return 'Player1'
                else        : return 'Player2'
            def winHor():
                if   l[0][0] == 'X' and l[0][1] == 'X' and l[0][2]  == 'X': return 'X'
                elif l[1][0] == 'X' and l[1][1] == 'X' and l[1][2]  == 'X': return 'X'
                elif l[2][1] == 'X' and l[2][0] == 'X' and l[2][2]  == 'X': return 'X'
                elif l[0][1] == 'O' and l[0][0] == 'O' and l[0][2]  == 'O': return 'O'
                elif l[1][1] == 'O' and l[1][0] == 'O' and l[1][2]  == 'O': return 'O'
                elif l[2][1] == 'O' and l[2][0] == 'O' and l[2][2]  == 'O': return 'O'
                else                                                      : return -1
            
            def winVer():   
                if   l[0][1] == 'X' and l[1][1] == 'X' and l[2][1]  == 'X': return 'X'
                elif l[2][0] == 'X' and l[0][0] == 'X' and l[1][0]  == 'X': return 'X'
                elif l[0][2] == 'X' and l[1][2] == 'X' and l[2][2]  == 'X': return 'X'
                elif l[0][1] == 'O' and l[1][1] == 'O' and l[2][1]  == 'O': return 'O'
                elif l[2][0] == 'O' and l[0][0] == 'O' and l[1][0]  == 'O': return 'O'
                elif l[0][2] == 'O' and l[1][2] == 'O' and l[2][2]  == 'O': return 'O'
                else                                                      : return -1
            
            def winDiag():    
                if   l[0][0] == 'X' and l[1][1] == 'X' and l[2][2]  == 'X': return 'X'
                elif l[2][0] == 'X' and l[1][1] == 'X' and l[0][2]  == 'X': return 'X'
                elif l[0][0] == 'O' and l[1][1] == 'O' and l[2][2]  == 'O': return 'O'
                elif l[2][0] == 'O' and l[1][1] == 'O' and l[0][2]  == 'O': return 'O'
                else                                                      : return -1
            
            def winCheck():
                h = winHor()
                if h == -1:
                    v = winVer()
                    if v == -1:
                        di = winDiag()
                        if di == -1: 
                            return 0
                        else: 
                            print(getPlayer(di), 'wins')
                            return 1
                    else: 
                        print(getPlayer(v), 'wins')
                        return 1
                else: 
                    print(getPlayer(h), 'wins')
                    return 1
                l = [['1','2','3'],
                 ['4','5','6'],
                 ['7','8','9']]
            d = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
            print()
            print("-----------WELCOME TO THE GAME OF TIC-TAC-TOE-----------")
            printGrid()
            p1, p2 = initials()
            count = 0
            
            while True:
                chanceP1()
                count += 1
                if winCheck(): break
                if count == 9:
                    print('Tie')
                    break
                    
                chanceP2()
                count += 1
                if winCheck(): break
                if count == 9:
                    print('Tie')
                    break

    elif a ==2 :
      import numpy as np
        #rockpaperscissor
    def initials():
        print("How many players want to play :")
        print("1. singleplayer")
        print("2. multiplayer")
        p = int(input("Enter the number"))
        if p == 1:
            l = ['R','S','P']
            player1 =  np.random.choice(l)
            #player1 = input("Choose you option player-1 \n 1. R for rock \n 2. S for scissor \n 3. P for paper\n").upper()
            player2 = input("Choose you option player-2 \n 1. R for rock \n 2. S for scissor \n 3. P for paper\n").upper()
            return player1,player2
        elif p ==2:     
            player1 = input("Choose you option player-1 \n 1. R for rock \n 2. S for scissor \n 3. P for paper\n").upper()
            player2 = input("Choose you option player-2 \n 1. R for rock \n 2. S for scissor \n 3. P for paper\n").upper()
        else:
            print("Enter the valid number")
    def win(a,b):
          counta = 0 
          countb = 0
          if a ==  b  : print('TIE')    
          elif a =='R' and b == 'S' : 
              print('PLAYER-1 WINS') 
              counta += 1 
          elif a == 'S' and b == 'P' : 
              print('PLAYER-1 WINS') 
              counta += 1      
          elif a == 'P' and b == 'R' : 
              print('PLAYER-1 WINS') 
              counta += 1 
          elif a == 'R' and b == 'P' : 
              print('PLAYER-2 WINS') 
              countb += 1       
          elif a == 'S' and b == 'R' : 
              print('PLAYER -2 WINS') 
              countb += 1 
          elif a == 'P' and b == 'S' : 
              print('PLAYER - 2 WINS') 
              countb += 1
          else:
              print("Enter the valid option")
          return counta,countb  
             
        def total(c,d):      
              if c>d  : print("Player-1 WINS MORE MATCHES")
              elif d>c: print("Player-2 WINS MORE MACTHES")
              else    : print("ITS A TIE")
          
for i in range(0,5):  
     a,b = initials()
     c,d = win(a,b)
total(c,d)

    elif a ==3:
       questions = ["What is the capital of Finland?",
             "What is the name of Bridget Jones' baby in the third Bridget Jones film?",
             "Which five colours make up the Olympic rings?",
             "In which decade was Madonna born?",
             "What is the most sold flavour of Walker's crisps?",
             "Grand Central Terminal, Park Avenue, New York is the world's",
            "Entomology is the science that studies",
            "Eritrea, which became the 182nd member of the UN in 1993, is in the continent of",
            "Garampani sanctuary is located at",
             "For which of the following disciplines is Nobel Prize awarded?",         
            "Hitler party which came into power in 1933 is known as?",
             "FFC stands for ?"            
            ]
options = [['Oulu','Helsinki','Kuopio','Jeonsu'],
           ["William","Armstrong","Stuart","Jinski"],
           ["Black, green, blue, white and red","Blue, green, orange, yellow and safforn","Black, green, blue, yellow and red","Black, grey, blue, yellow and pink"],
           ["The 1940s (1949)","The 1960s (1965)","The 1970s (1978)","The 1950s (1958)"],
           ["Cheese and Onion" ,"Cheese and pasta","tomato and Onion","Cheese and garlic"],
            ["largest railway station","highest railway station","longest railway station","None of the above"],         
          ["Behavior of human beings","Insects","The origin and history of technical and scientific terms","The formation of rocks"],
           ["Asia","Africa","Europe","Australia"],
           ["Junagarh, Gujarat", "Diphu, Assam", "Kohima, Nagaland", "Gangtok, Sikkim"],
           ["Physics and Chemistry","Physiology or Medicine","Literature Peace and Economics","All of the above"],
            ["Labour Party","Nazi Party","Ku-Klux-Klan","Democratic Party"],
           ["Foreign Finance Corporation","Film Finance Corporation","Federation of Football Council","None of the above"]
          ]
correct = ['Helsinki','William','Black, green, blue, yellow and red','The 1950s (1958)','Cheese and Onion','largest railway station','Insects',
            'Africa','Diphu, Assam','Physiology or Medicine','Nazi Party','Film Finance Corporation']

prize = ['0','1000','2000','5000','10000','20000','1000000','200000','500000','1000000','5000000','10000000']

import numpy as np
import pyrebase as pb   
import pyrebase

config = {
  "apiKey": "apiKey",
  "authDomain": "assignment-efe1b-default-rtdb.firebaseapp.com",
  "databaseURL": "https://assignment-efe1b-default-rtdb.firebaseio.com/",
  "storageBucket": "assignment-efe1b-default-rtdb.appspot.com"
}
total =0
firebase = pyrebase.initialize_app(config)
db = firebase.database()
import pyttsx3 
converter = pyttsx3.init()  
converter.setProperty('rate', 125) 
converter.setProperty('volume', 1.0) 
# converter.setProperty('language',hindi) 
converter.say("WELCOME TO THE GAME !!! OF WHO WILL BECOME THE MILLIONAIRE ") 
converter.say("I'M YOUR HOST! THE AI") 



converter.runAndWait() 

voices = converter.getProperty('voices') 
  
for voice in voices: 
    # to get the info. about various voices in our PC  
    print("Voice:") 
    print("ID: %s" %voice.id) 
    print("Name: %s" %voice.name) 
    print("Age: %s" %voice.age) 
    print("Gender:female %s" %voice.gender) 
    print("Languages Known: %s" %voice.languages)
print("-----------SWAGAT HAI AAPKA KAUN BANEGA CROREPATI ME ----------")
flag = 1;
variable = 0;
p1 = (input("MANYAWAR KA NAAM:"))
print("----------CHALIYIEN SHURU KARTEY HAIN---------")
for i in range(0,len(questions)):
    ques = np.random.choice(questions,12,replace = False).tolist()
    print()
    print("Yeh Sawaal ",prize[i],"ruppes ke liye hai")
    print("Question",i+1)
    print(i+1,ques[i])
    ques=questions[i]
    qos=questions.index(ques)
    print("Options:")
    for j in range(0,4):
            print('\t',j+1,options[questions][j])
    right = int(input("Enter the correct options number :\n"))
    if options[qos][right-1] == correct[qos]:
            print("Hence your option is correct\n")
    elif i<=4:
        print("Incorrect")
        print("AAP AAJ GHR LEKE JAA RHE HAI SHUNYA RASHI")
        total =0
        break
    elif i>=4 and i<=8:
        print("MANYAWAR YEH UTTAR GALAT HAI:")
        print("AAP AAJ GHR LEKE JAA RHE HAI:",prize[4],"RUPPES")
        total = prize[4]
        break
    elif i>=8:
        print("MANYAWAR YEH UTTAR GALAT HAI:")
        print("AAP AAJ GHR LEKE JAA RHE HAI:",prize[8],"RUPPES")
        total = prize[4]
        break
    if i == 4 or i == 8:
        print("AAPNE YEH PADAV PAAR KR LIYA HAI AUR AB AAP GHR LEKE HI JAYENGEY KUCH MULYA KI RASHI:");
        print(prize[i])
        total = prize[4]
    if i<len(questions)-1:
        ask = input("Do You Want to Proceed :Y/N").upper()
        if ask == 'Y':
            flag = 1
        else:
            flag = 0;
            print("Hence you won cash prize if ",prize[i])
            total = prize[i]
            break  
            
    if(i==len(questions)):
        print("-------------MANYAWAR AAP JEET GYE HAI POOREY EK CRORE RUPPPES -----")
        print("-------------AAP GHR LEKE JAA RHE HAI----- ")
        print(total)
    data = {p1:total}
    db.child("Player_Name").update(data)
elif a == 4:
        l = ["india","china","brazil","kenya","pakistan","bangladesh","hongkong","iran","iraq","isreal"]
import numpy as np
print("----------WELCOME TO THE HANGMAN GAME --------")
print("-----------YOU WILL HVAE TO GUESS THE COUNTRY NAME -----------")
print("-----RULES-----")
print("YOU WILL GET TOTAL OF 5 CHANCES TO GUESS THE LETTER")
print("YOU WILL ")
word = np.random.choice(l,replace = 'True')
word
list1 = []
for i in range(len(word)):
    list1.append('_')
print(list1)
count = 0;
p = len(word)
print("word consist of ",len(word),"letters")
print("GUESS THE LETTER OR GUESS THE WORD")
for i in range(5):
    print("1 for letter \n 2 for word")
    number = int(input("Enter your choice"))
    if number == 1:
        # for i in range(0,5):
            max =5
            l1 = input("Enter the  letter of your guess").lower()
            if l1 in word: 
                count += 1 
                print("You guess the letter right")
                for i in range(len(word)):
                    if word[i] == l1:
                        list1[i] = l1
                # list1[word.index(l1) ] = l1
                print(list1)
            else            : 
                    count = 0
                    print("you guess the worng letter")
            max-=1
            print("You left with chances",max)
    if number == 2:
        l1 = input("Enter the  word of your guess").lower()
        if l1 == word: 
            print("You guess the word right")
            break
        else         : count = 0
    if count == len(word):
        print("You guess the word right")

    else:
        print("Enter the valid number  1 ,2 or 3")
elif p == 2:
    print("1.TIK-TAC-TOE")
    print("2.ROCK-PAPER-SCISSOR")
    a = int(input("Enter the number"))
    if a == 1:
        # game of tic-tac-toe
def printGrid():
    for i in l:
        print(i)

def initials():
    player1 = input("Enter your side X/O player -1").upper()
    if player1 == 'X': player2 = 'O'
    else             : player2 = 'X'
    print("Hence player-2 got", player2)
    return player1, player2

def posToRowCol(pos):
    row = d[pos][0]
    col = d[pos][1]
    return row, col
    
def chanceP1():
    while True:
        w = int(input("Choose the position for player1: "))
        row, column = posToRowCol(w)
        if l[row][column] not in 'OX':
            l[row][column] = p1
            printGrid()
            return
        else: 
            print('Position already taken.')
            chanceP1()
def chanceP2():
    v = int(input("Choose the position for player2: "))
    row, column = posToRowCol(v)
    if l[row][column] not in 'OX':
        l[row][column] = p2
        printGrid()
        return
    else:
        print('Position already taken')
        chanceP2()
def getPlayer(ini):
    if ini == 'X':
        if p1 == 'X': return 'Player1'
        else        : return 'Player2'
    else:
        if p1 == 'O': return 'Player1'
        else        : return 'Player2'
def winHor():
    if   l[0][0] == 'X' and l[0][1] == 'X' and l[0][2]  == 'X': return 'X'
    elif l[1][0] == 'X' and l[1][1] == 'X' and l[1][2]  == 'X': return 'X'
    elif l[2][1] == 'X' and l[2][0] == 'X' and l[2][2]  == 'X': return 'X'
    elif l[0][1] == 'O' and l[0][0] == 'O' and l[0][2]  == 'O': return 'O'
    elif l[1][1] == 'O' and l[1][0] == 'O' and l[1][2]  == 'O': return 'O'
    elif l[2][1] == 'O' and l[2][0] == 'O' and l[2][2]  == 'O': return 'O'
    else                                                      : return -1

def winVer():   
    if   l[0][1] == 'X' and l[1][1] == 'X' and l[2][1]  == 'X': return 'X'
    elif l[2][0] == 'X' and l[0][0] == 'X' and l[1][0]  == 'X': return 'X'
    elif l[0][2] == 'X' and l[1][2] == 'X' and l[2][2]  == 'X': return 'X'
    elif l[0][1] == 'O' and l[1][1] == 'O' and l[2][1]  == 'O': return 'O'
    elif l[2][0] == 'O' and l[0][0] == 'O' and l[1][0]  == 'O': return 'O'
    elif l[0][2] == 'O' and l[1][2] == 'O' and l[2][2]  == 'O': return 'O'
    else                                                      : return -1

def winDiag():    
    if   l[0][0] == 'X' and l[1][1] == 'X' and l[2][2]  == 'X': return 'X'
    elif l[2][0] == 'X' and l[1][1] == 'X' and l[0][2]  == 'X': return 'X'
    elif l[0][0] == 'O' and l[1][1] == 'O' and l[2][2]  == 'O': return 'O'
    elif l[2][0] == 'O' and l[1][1] == 'O' and l[0][2]  == 'O': return 'O'
    else                                                      : return -1

def winCheck():
    h = winHor()
    if h == -1:
        v = winVer()
        if v == -1:
            di = winDiag()
            if di == -1: 
                return 0
            else: 
                print(getPlayer(di), 'wins')
                return 1
        else: 
            print(getPlayer(v), 'wins')
            return 1
    else: 
        print(getPlayer(h), 'wins')
        return 1
        
l = [['1','2','3'],
     ['4','5','6'],
     ['7','8','9']]
d = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
print()
print("-----------WELCOME TO THE GAME OF TIC-TAC-TOE-----------")
printGrid()
p1, p2 = initials()
count = 0

while True:
    chanceP1()
    count += 1
    if winCheck(): break
    if count == 9:
        print('Tie')
        break
        
    chanceP2()
    count += 1
    if winCheck(): break
    if count == 9:
        print('Tie')
        break
    elif a ==2 :
        print("-------------WELCOME TO THE GAME OF ROCK PAPER SCISSOR------------")
counta = 0
countb = 0
for i in  range(0,3):
    a = input("Choose you option player-1 \n 1. R for rock \n 2. S for scissor \n 3. P for paper\n").upper()
    b = input("Choose you option player-2 \n 1. R for rock \n 2. S for scissor \n 3. P for paper\n").upper()
    if a == 'R' and b == 'R' : 
              print('TIE')
    elif a =='R' and b == 'S' : 
              print('PLAYER-1 WINS') 
              counta += 1 
    elif a == 'R' and b == 'P' : 
              print('PLAYER-2 WINS') 
              countb += 1 
    elif a == 'S' and b == 'R' : 
              print('PLAYER -2 WINS') 
              countb += 1 
    elif a == 'S' and b == 'P' : 
              print('player -1 wins') 
              counta += 1 
    elif a == 'S' and b == 'S' : 
              print('TIE')
    elif a == 'P' and b == 'R' : 
              print('PLAYER-1 WINS') 
              counta += 1 
    elif a == 'P' and b == 'P' : 
              print('TIE')
    elif a == 'P' and b == 'S' : 
              print('PLAYER - 2 WINS') 
              countb += 1 
    else:
        print("Enter a valid option")
if counta > countb:
    print("player 1 wins the series")
elif countb>counta:
    print("player 2 wins the series")
else:
    print("Its a tie")
    else:
        print("Enter the valid number ")
else :
    print("Enter the valid number")
