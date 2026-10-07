import random

# 100 words with hints
words = {
    "python": "A popular programming language",
    "computer": "An electronic machine used to process data",
    "programming": "The process of writing computer instructions",
    "developer": "A person who creates software",
    "keyboard": "A device used for typing",

    "internet": "A worldwide network connecting computers",
    "website": "A collection of pages available on the internet",
    "software": "Programs that run on a computer",
    "hardware": "Physical parts of a computer",
    "database": "A system used to store organized information",

    "algorithm": "A step-by-step method for solving a problem",
    "variable": "A named storage location in programming",
    "function": "A reusable block of code",
    "computer": "An electronic device that processes information",
    "monitor": "A screen used to display information",

    "mouse": "A pointing device used with a computer",
    "printer": "A device that produces documents on paper",
    "scanner": "A device that converts documents into digital form",
    "laptop": "A portable personal computer",
    "smartphone": "A mobile phone with advanced computing features",

    "android": "A mobile operating system developed by Google",
    "windows": "A popular computer operating system",
    "linux": "An open-source operating system",
    "browser": "Software used to access websites",
    "server": "A computer that provides services to other computers",

    "network": "A group of connected computers",
    "cybersecurity": "The practice of protecting systems from digital attacks",
    "password": "A secret code used to access an account",
    "encryption": "Converting information into a protected form",
    "firewall": "A security system that controls network traffic",

    "cloud": "Internet-based computing and storage",
    "python": "A programming language known for simple syntax",
    "java": "A widely used object-oriented programming language",
    "javascript": "A programming language commonly used for web pages",
    "database": "An organized collection of data",

    "machine": "A device that performs a task",
    "learning": "The process of gaining knowledge or skills",
    "artificial": "Something made by humans rather than naturally",
    "intelligence": "The ability to learn and solve problems",
    "robot": "A machine capable of performing tasks automatically",

    "science": "The systematic study of the natural world",
    "technology": "The application of scientific knowledge",
    "education": "The process of gaining knowledge",
    "student": "A person who studies",
    "teacher": "A person who helps others learn",

    "college": "An institution for higher education",
    "classroom": "A room where students learn",
    "library": "A place containing books and other resources",
    "notebook": "A book used for writing notes",
    "pencil": "An instrument used for writing or drawing",

    "book": "A written or printed work",
    "author": "A person who writes a book",
    "movie": "A motion picture",
    "music": "Organized sound used for expression",
    "picture": "A visual representation of something",

    "camera": "A device used to capture photographs",
    "television": "A device used to watch programs",
    "radio": "A device that receives broadcast signals",
    "headphones": "A device worn over the ears to hear sound",
    "speaker": "A device that produces sound",

    "telephone": "A device used to communicate with others",
    "message": "Information sent from one person to another",
    "email": "Electronic mail sent over the internet",
    "social": "Related to interaction with other people",
    "friend": "A person you know and like",

    "family": "A group of related people",
    "mother": "A female parent",
    "father": "A male parent",
    "brother": "A male sibling",
    "sister": "A female sibling",

    "flower": "The colorful reproductive part of a plant",
    "garden": "A place where plants are grown",
    "forest": "A large area covered with trees",
    "mountain": "A large natural elevation of the earth",
    "river": "A natural flowing stream of water",

    "ocean": "A very large body of salt water",
    "island": "Land surrounded by water",
    "rainbow": "A colorful arc seen after rain",
    "thunder": "The sound produced by lightning",
    "sunshine": "Light from the sun",

    "animal": "A living organism that is not a plant",
    "elephant": "The largest land animal",
    "tiger": "A large striped wild cat",
    "lion": "A large wild cat known as the king of the jungle",
    "rabbit": "A small animal with long ears",

    "butterfly": "An insect with colorful wings",
    "dolphin": "An intelligent marine mammal",
    "penguin": "A flightless bird that lives mainly in cold regions",
    "giraffe": "An animal with a very long neck",
    "monkey": "An intelligent animal that climbs trees",

    "apple": "A common red or green fruit",
    "banana": "A long yellow fruit",
    "orange": "A round citrus fruit",
    "mango": "A sweet tropical fruit",
    "watermelon": "A large fruit with green skin and juicy flesh",

    "pizza": "A popular dish with a flat bread base and toppings",
    "burger": "A sandwich containing a patty",
    "sandwich": "Food made with bread and filling",
    "chocolate": "A sweet food made from cocoa",
    "icecream": "A frozen sweet dessert",

    "football": "A popular sport played with a ball",
    "cricket": "A bat-and-ball sport popular in India",
    "tennis": "A sport played with a racket and ball",
    "basketball": "A sport where players throw a ball into a hoop",
    "volleyball": "A sport played by hitting a ball over a net"
}


# Hangman drawings
HANGMAN_PICS = [
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


def display_word(word, guessed_letters):
    displayed_word = ""

    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "

    return displayed_word


def play_game():

    # Select a random word
    word = random.choice(list(words.keys()))

    # Get hint
    hint = words[word]

    # Store guessed letters
    guessed_letters = []

    # Maximum incorrect guesses
    max_attempts = 6
    incorrect_guesses = 0

    print("\n" + "=" * 45)
    print("             WELCOME TO HANGMAN")
    print("=" * 45)

    print("\n💡 Hint:", hint)

    while incorrect_guesses < max_attempts:

        print(HANGMAN_PICS[incorrect_guesses])

        print("Word:", display_word(word, guessed_letters))

        print(
            "Guessed letters:",
            ", ".join(guessed_letters)
            if guessed_letters
            else "None"
        )

        print(
            "Incorrect guesses:",
            incorrect_guesses,
            "/",
            max_attempts
        )

        # Check if player won
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 CONGRATULATIONS!")
            print("You guessed the word:", word)
            return

        # Get input
        guess = input("\nEnter a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1:
            print("❌ Please enter only ONE letter.")
            continue

        if not guess.isalpha():
            print("❌ Please enter a valid alphabet letter.")
            continue

        # Check repeated letter
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        # Store guess
        guessed_letters.append(guess)

        # Check guess
        if guess in word:
            print("✅ Correct guess!")

        else:
            incorrect_guesses += 1
            print("❌ Wrong guess!")

    # Game over
    print(HANGMAN_PICS[incorrect_guesses])

    print("\n💀 GAME OVER!")
    print("The correct word was:", word)


def main():

    while True:

        play_game()

        while True:

            play_again = input(
                "\nDo you want to play again? (y/n): "
            ).lower().strip()

            if play_again == "y":
                break

            elif play_again == "n":
                print("\nThanks for playing Hangman! 👋")
                return

            else:
                print("Please enter 'y' or 'n'.")


# Start the game
if __name__ == "__main__":
    main()