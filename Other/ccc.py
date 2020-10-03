import random
import time


def displeyIntro():
    print('''вы находитесь в землях, заселёных драконами.Перед собой вы видете две пещеры в первой - дружелюбный дракон, во второй - жадный и голодный дракон''')
    cave = ""
    while cave != '1' and cave != '2':
        print("в какую пещеру вы войдёте (нажмите 1 или 2)")
        print()

    return cave

def checkCave(chosenCave):
    print("вы приближаетесь к пещере...")
    time.sleep(2)
    print("её тем ота заставляет вас дрожать от страха")
    time.sleep(2)
    print("Дракон выпрыгивает на вас раскрывает пасть и...")
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print("делица с вами сокровищами")
    else:

        print("моментально вас съедает")
