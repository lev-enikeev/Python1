import random

guessesTaken = 0

print ("Привет как тебя зовут?")

Name = input()

number = (random.randint(0,20))
print ('Что ж,' + Name + ' я загадываю число от 0 до 20.')

for guessesTaken in range(6):
    print("попробуй угадать")
    guess = input()
    guess = int(guess)

    if guess < number :
        print("твоё число слишком маленькое.")
          
    if guess > number:
        print("твоё число слишком большое.")

    if guess == number:
        break

if guess == number:
     guessesTaken = str(guessesTaken + 1)
     print ('ты справился за ' + guessesTaken + " попытки.")

if guess != number:
     number = str(number)
     print("увы я загадал число " + number + '.')
