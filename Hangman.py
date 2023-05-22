import math
import random

HANGMAN_ASCII_ART = """Welcome to the game Hangman

    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
"""
MAX_TRIES = 6

num_rand = random.randint(5, 10)
    
HANGMAN_PHOTOS = { 
'picture_1': "x-------x",
'picture_2': """
    x-------x
    |
    |
    |
    |
    |""",
'picture_3': """
    x-------x
    |       |
    |       0
    |
    |
    |""",
'picture_4': """
    x-------x
    |       |
    |       0
    |       |
    |
    |""",
'picture_5': """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""",
'picture_6': """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""",
'picture_7': """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """
}

def print_hangman(num_of_tries):
    if int(num_of_tries) == 0:
        print(HANGMAN_PHOTOS['picture_1'])
        
    elif int(num_of_tries) == 1:
        print(HANGMAN_PHOTOS['picture_2'])
        
    elif int(num_of_tries) == 2:
        print(HANGMAN_PHOTOS['picture_3'])
        
    elif int(num_of_tries) == 3:
        print(HANGMAN_PHOTOS['picture_4'])
        
    elif int(num_of_tries) == 4:
        print(HANGMAN_PHOTOS['picture_5'])
        
    elif int(num_of_tries) == 5:
        print(HANGMAN_PHOTOS['picture_6'])
        
    elif int(num_of_tries) == 6:
        print(HANGMAN_PHOTOS['picture_7'])         

def is_valid_input(letter_guessed):
    """
    The function asks for a single character.
    After that you check if the character is single or if it is made of symbols.
    Prints the error or the character that was converted to lowercase.
    :param letter_guessed: The character sent for testing
    :return True: In case the character is correct or False in the case of an error
    :rtype bool
    """
    
    if not letter_guessed.isalpha():
        if len(letter_guessed) > 1:
            print("E3")
        else:
            print("E2")
        return False 
               
    elif len(letter_guessed) > 1:
        print("E1")
        return False 
           
    else:
        letter_guessed = letter_guessed.lower()
        return True
    

def check_valid_input(letter_guessed, old_letters_guessed):
    
    if is_valid_input(letter_guessed) == False:
        return False
    
    else:
        return True
    
    
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    
    if check_valid_input(letter_guessed, old_letters_guessed):
        if letter_guessed not in old_letters_guessed:
            old_letters_guessed.append(letter_guessed.lower())
            return True
        
        else:
            print('The signal is already selected')
            return False
                
    else:
        print('X')
        print(' -> '.join(old_letters_guessed))
        return False
    
    
def show_hidden_word(secret_word, old_letters_guessed):
    new_str = ""
    for i in secret_word:
        if i in old_letters_guessed:
            new_str = (new_str + i)
        else:
            new_str = (new_str + '_') 
    print(new_str)
    
def check_win(secret_word, old_letters_guessed):
    for i in secret_word:
        if i not in old_letters_guessed:
            return False
    return True

def choose_word(file_path, index):
    """
    This function returns a word from a file,
    The function receives a path to the file and an index.
    The function accepts the words into a list and returns the word in the requested position.
    :param file_path: path to the file index: selected location
    :type file_path: string, index: int
    :return the selected word
    :rtype string
    """
    open_file = open(file_path, 'r')
    
    line = open_file.readline()
    
    temp_list = line.split(' ')
 
    open_file.close()
    
    if index > len(temp_list):
        index = (index - 1) % len(temp_list)
        
    print(temp_list[index])
    
    return temp_list[index]

def main():
    secret_word = ""
    old_letters_guessed = []
    num_of_tries = 0
    
    path_file = input('Enter a path to the file: ')
    index = input('and a number to select the word from the file: ')
    secret_word = choose_word(path_file, int(index))
    
    print_hangman(num_of_tries)
    
    show_hidden_word(secret_word, old_letters_guessed)
    
    while(num_of_tries < MAX_TRIES):
        letter_guessed = input('Enter the letter of your choice: ')
        
        while(try_update_letter_guessed(letter_guessed, old_letters_guessed)) == False:
            letter_guessed = input('Enter the letter of your choice: ')
        
        if letter_guessed not in secret_word:
            print(':(')
            num_of_tries += 1
            print_hangman(num_of_tries)
        
        if check_win(secret_word, old_letters_guessed) == True:
            print('WIN')
            show_hidden_word(secret_word, old_letters_guessed)            
            break
        
        if num_of_tries == 6:
            print('LOSE')
        
        show_hidden_word(secret_word, old_letters_guessed)
        
        
        
        
    
    
    
    exit()
  
    
if __name__ == "__main__":
    main()   
    