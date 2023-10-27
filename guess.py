import random

def main():

    number = random.randint(1, 10)

    play = int(input("please guess my number between 1-10: "))

    while play != number:
        if play >= 1 and play <= 10:
            print("HAHA, you are wrong.")
            difference = abs(number - play)
            print("you are ",difference, "away from my number.")
            play = int(input("please guess another number: "))

        elif play <= 1 and play >= 10:
            print("That's not between 1 to 10.")
            play = int(input("please guess another number: "))

    print("Yes! you got the number right!")




main()



