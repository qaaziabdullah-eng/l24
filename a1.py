import random
import time
number=random.randint(1,100)
def intro():
    print("may i ask you for your name?")
    global Name
    name = input()
    print(name + ", we are going to play a game. i am thinking of a number between 1 and 100")
    if(number%2==0):
        x='evenn'
    else:
        x='odd'
        print("\nthis is an {} number".format(x))
        time.sleep(0.5)
        print("go ahead. guess!")

def pick():
    guesstaken = 0
    while guesstaken <6:
      time.sleep(.25)
      enter=input("enter guesses: ")    
      try:
          guess = int(enter)
          if guess<=100 and guess>=1:
              guessestaken=guessestaken+1
              if guessestaken<6:
                  if guess<number:
                    print("the guess of the number that you have entered is to low")
                  if guess != number:
                    print("the guess of the number that you have entered is to high")
                  if guess !=number:
                    time.sleep(.5)
                    print("try again!")
                  if guess == number:
                    break
                  
              if guess>100 or guess<1:
                 print("silly goose! that number isn't in the range")
                 time.sleep(.25)
                 print("please enter a number between 1 and 100")

      except:
        print("i don't think "+enter+"is a number.sorry")

    if guess == number:
     guessestaken = str(guessestaken)   
     print("you guessed my number")
    if guess !=number:
      print("nope.wrong guess")

playing="yes"
while playing=="yes":
   intro()
   pick()
   print("do you want to play again?")
   playagain=input()
