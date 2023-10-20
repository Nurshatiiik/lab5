import random
def guess_the_number():
    secret_number = random.randint(1, 20)
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    num_guesses = 0
    while True:
        try:
            guess = int(input("Take a guess: "))
            num_guesses += 1
            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
                break
        except ValueError:
            print("Please enter a valid number between 1 and 20.")

            
if __name__ == "__main__":
    guess_the_number()
