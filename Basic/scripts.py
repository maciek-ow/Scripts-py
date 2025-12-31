import random

def main():
    x = random.randint(0,100)
    print("Hello dear user, i want for you to guess my number")
    guess = int(input())
    while guess != x:
        if guess > x:
            print("your number is to big, try guessing lower")
            guess = int(input())
        else:
            print("you guess to low try higher")
            guess = int(input())
    print ("you guessed right!", x,"=",guess)
if __name__ == "__main__":
    main()