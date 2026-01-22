import random

# Hangman stages
HANGMAN_STAGES = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]

# Word list
WORDS = [
    "python", "programming", "computer", "science", "developer",
    "algorithm", "variable", "function", "keyboard", "monitor",
    "internet", "database", "software", "hardware", "network",
    "security", "encryption", "password", "authentication", "firewall"
]

def display_game_state(word, guessed_letters, attempts):
    """Display current game state"""
    # Show the word with guessed letters revealed
    display_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    print(f"\nWord: {display_word}")
    
    # Show hangman diagram
    print(HANGMAN_STAGES[attempts])
    
    # Show guessed letters
    if guessed_letters:
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    
    # Show remaining attempts
    print(f"Remaining attempts: {len(HANGMAN_STAGES) - attempts - 1}")

def get_user_guess(guessed_letters):
    """Get and validate user input"""
    while True:
        guess = input("Guess a letter: ").lower().strip()
        
        if len(guess) != 1:
            print("Please enter exactly one letter!")
            continue
        
        if not guess.isalpha():
            print("Please enter a letter (a-z)!")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'! Try a different letter.")
            continue
        
        return guess

def play_game():
    """Main game loop"""
    word = random.choice(WORDS)
    guessed_letters = set()
    attempts = 0
    max_attempts = len(HANGMAN_STAGES) - 1
    
    print("=" * 40)
    print("Welcome to Hangman!")
    print("=" * 40)
    print(f"The word has {len(word)} letters.")
    
    while attempts < max_attempts:
        display_game_state(word, guessed_letters, attempts)
        
        guess = get_user_guess(guessed_letters)
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            
            # Check if player has won
            if all(letter in guessed_letters for letter in word):
                print("\n" + "=" * 40)
                print(f"🎉 Congratulations! You won! The word was '{word}'!")
                print("=" * 40)
                return True
        else:
            attempts += 1
            print(f"Wrong guess! '{guess}' is not in the word.")
            
            # Check if player has lost
            if attempts == max_attempts:
                print("\n" + "=" * 40)
                print(f"💀 Game Over! You lost! The word was '{word}'!")
                print("=" * 40)
                return False

def main():
    """Main program loop"""
    play_again = "y"
    wins = 0
    losses = 0
    
    while play_again.lower() == "y":
        won = play_game()
        
        if won:
            wins += 1
        else:
            losses += 1
        
        print(f"\nScore - Wins: {wins}, Losses: {losses}")
        play_again = input("\nPlay again? (y/n): ").strip()
    
    print("\nThanks for playing! Goodbye!")

if __name__ == "__main__":
    main()