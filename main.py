from HigherLower import *

def main():
    game = HigherLower()
    guess = int(input())#random.randint(1, 100)
    while game.try_guess(guess) != 0:
        guess = int(input())  # random.randint(1, 100)
        print(guess)


if __name__ == "__main__":
    main()