#import os

word = str(input("Player 1 choose a 4 letters word: "))
#os.system("cls")
print(chr(27) + "[2J") 

def horca():
  print("______   ")
  print("|     |  ")
  print("|        ")
  print("|        ")
  print("|        ")
  print("|______  ")
  print("         ")

def horca2():
    print("______   ")
    print("|     |  ")
    print("|     0  ")
    print("|        ")
    print("|        ")
    print("|______  ")
    print("         ")

letra1 = word[0]
letra2 = word[1]
letra3 = word[2]
letra4 = word[3]


horca()

letra_1 = ("_")
letra_2 = ("_")
letra_3 = ("_")
letra_4 = ("_")


while(True):
      # print(chr(27) + "[2J") 
      # os.system("cls")
      
      # horca()

      print(letra_1, letra_2, letra_3, letra_4)
      if letra_1 == letra1 and letra_2 == letra2 and letra_3 == letra3 and letra_4 == letra4:
       break
      else:  
        guess = str(input("Player 2 choose a letter: "))
        
        if guess == letra1:
          letra_1 = letra1
        if guess == letra2:
          letra_2 = letra2
        if guess == letra3:
          letra_3 = letra3
        if guess == letra4:
          letra_4 = letra4
        else:
          horca2()
        











