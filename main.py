from HigherLower import *

def main():
    game = HigherLower()
    guess = random.randint(0, 100)
    while game.try_guess(guess) != 0:
        guess = random.randint(0, 100)
        print(guess)



if __name__ == "__main__":
    main()