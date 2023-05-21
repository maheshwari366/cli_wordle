import random

def generate_wordle_word():
    with open('words.txt', 'r') as f:
        words = f.read().split('\n')
    return random.choice(words)

def generate_wordle_puzzle():
    target_word = generate_wordle_word()
    
    print("Welcome to Wordle Puzzle!")
    print("Guess the word with 5 letters.")
    print("You have 6 attempts.")
    
    attempts = 0
    while attempts < 6:
        guess = input("Enter your guess: ").lower()
        
        if len(guess) != 5:
            print("Invalid guess! The word has 5 letters.")
            continue
        
        if guess == target_word:
            print("Congratulations! You guessed the word correctly!")
            break
        
        feedback = ""
        for i in range(5):
            if guess[i] == target_word[i]:
                feedback += guess[i]
            elif guess[i] in target_word:
                feedback += "*"
            else:
                feedback += "-"
        
        print("Feedback:", feedback)
        attempts += 1
    
    if attempts >= 6:
        print("You ran out of attempts! The word was:", target_word)

generate_wordle_puzzle()