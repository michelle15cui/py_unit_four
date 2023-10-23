import random

def main():

    number = random.randint(1, 10)
    print("Please guess a number between 1-10!")

    play = int(input("please guess my number: "))

    if play >= 1 and play <= 10:
            print("sorry, you are wrong.")
            print("you are ", number-play, "away from my number")
            play = int(input("please guess another number: "))
    elif play <= 1 and play >= 10:
            print("That's not between 1 to 10.")
            play = int(input("please guess another number: "))
    elif play == number:
            print("Yes! you got the number right!")

main()
