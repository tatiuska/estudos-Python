from wordle import Wordle


def main():
    print("Hello, Wordle!")
    wordle = Wordle("APPLE")

    while True:
        word = input("Type your guess: ")
        if word == wordle.secret:
            print("You have guessed the word!")
            break
        print("Your guess is incorrect.")


if __name__ == "__main__":
    main()
