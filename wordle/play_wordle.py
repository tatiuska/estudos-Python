from wordle import Wordle

def main():
    print("Hello, Wordle!")
    wordle = Wordle("APPLE")

    while wordle.can_attempt:
        word = input("Type your guess: ")

        if len(word) != wordle.WORD_LENGTH:
            print(f"Word must be {wordle.WORD_LENGTH} characters long!")
            continue
            
        wordle.attempt(word)
        result = wordle.guess(word)
        print(*result, sep="\n")

    if wordle.is_solved:
        print("You've solved the puzzle!")
    else:
        print("You failed to solve the puzzle.")


if __name__ == "__main__":
    main()
