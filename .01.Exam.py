from random import randint
name=(input("Hello! What is your name?"))
print("Well,",name,",I'm thinking of a number between 1 and 20")
x = randint(1,20)

print('You have 5 guesses!')
guesses = 0

for guesses in range(5):
    n=int(input("Take a guess:"))
    if n<x and guesses<4: 
       print("Your guess is too low")
       guesses +=1
    elif n>x and guesses <4: 
        print("Your guess is too high")
        guesses +=1
    elif n==x and guesses<=4 :
        print('Good job,' ,name, ', you guessed my number in',guesses,'tries!')
        guesses +=1
    else:
        print("Nope! The number I was thinking of is" ,x,".")
        break
   




       



