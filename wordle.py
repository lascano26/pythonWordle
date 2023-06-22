"""Structured Wordle."""

def contains_char(char_search: str, char_guess: str) -> bool:
    """Checking whether or not a char is in a str."""
    assert len(char_guess) == 1
    i: int = 0
    char_exists: bool = False
    while i < len(char_search):        
        while not char_exists and i < len(char_search):
            if char_search[i] == char_guess: 
                char_exists = True 
            i = i + 1
        if char_exists:
            return True
        else: 
            return False
    return False
# Here I am checking whether or not an inputted character is in a string. I do 
# this by checking each index of the string and seeing if the character is there. 


def emojified(guess: str, secret: str) -> str:
    """Checking the indices for which box to print."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_str: str = ""
    c: int = 0
    chr_exists: bool = False
    while not chr_exists and c < len(secret):
        if secret[c] == guess[c]:
            emoji_str = emoji_str + GREEN_BOX
        else:
            if contains_char(secret, guess[c]) is True:
                emoji_str = emoji_str + YELLOW_BOX
            else: 
                emoji_str = emoji_str + WHITE_BOX
        c = c + 1
    return emoji_str

# Here I am checking the indices to be able to see whether a yellow, white, or green
# box should be printed. I do this by checking the indices that are the same and 
# also check for characters at other indices.


def input_guess(expected_length: int) -> str:
    """Checking if a guess is the expected length."""
    guess: str = input(f"Enter a {str(expected_length)} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {str(expected_length)} chars! Try again: ")
    return guess
# Here I am checking if an inputted guess is the right length and prompting
# another input if it is not the correct length. 


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1 
    secret: str = "codes"
    player_guess: str = ""
    while turns <= 6 and secret != player_guess:
        print(f"=== Turn {turns}/6 ===")
        player_guess = input_guess(len(secret))
        print(emojified(player_guess, secret))
        if (emojified(player_guess, secret)) == "\U0001F7E9" * len(secret):
            print(str(f"You won in {str(turns)}/6 turns!"))
            print("")
        else: 
            turns += 1 
    if turns > 6:
        print("X/6 - Sorry, try again tomorrow!")    
        print("")
# Here I am bringing together all of my defined functions and using them to create
# the final version of the game. This includes printing the turn count, prompting
# a guess, printing the emoji string, and printing whether or not the player has won.
 

if __name__ == "__main__":
    main() 