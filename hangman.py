# Write your code here
import random

print('H A N G M A N')
menu = ''
while menu != 'play' or menu != 'exit':
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == 'exit':
        lives = 0
        break
    elif menu == 'play':
        break
list_words = ['python', 'java', 'kotlin', 'javascript']
game_word = list(random.choice(list_words))
hint = ['-' for a in game_word]
game_word_check = frozenset(game_word)
instances_index = []
letter_counter = {}
used_letters = set()
temporary_word = game_word.copy()
temporary_num = 0
lives = 8

for char in set(game_word):
    letter_counter[char]=game_word.count(char)  # we count letters in game_word
while lives > 0:  # player has 8 tries to guess word
    print('')
    print(''.join(hint))
    letter = input('Input a letter: ')
    if len(letter) != 1:
        print('You should input a single letter')
    elif letter.islower() != True:
        print('Please enter a lowercase English letter')
    elif letter in used_letters:
        print("You've already guessed this letter")
    elif letter not in game_word_check:
        print("That letter doesn't appear in the word")
        used_letters.add(letter)
        lives -= 1
    elif letter in game_word_check:
        if letter_counter[letter] > 1:
            for a in range(letter_counter[letter]):  # we get a list of letter[indexes] to use it
                instances_index.append(temporary_word.index(letter) + temporary_num)
                temporary_word.remove(letter)
                hint[instances_index[temporary_num]] = letter
                temporary_num += 1
        else:
            temporary_index = game_word.index(letter)  # we just replace '-' in hint with a correct letter
            hint[temporary_index] = letter
        temporary_word = game_word.copy()
        temporary_num = 0
        used_letters.add(letter)
    if '-' not in hint:  # if there's no covered letters - game finished
        break
if lives >= 1 and '-' not in hint:
    print('You guessed the word!\nYou survived!')
else:
    print('You lost!')
