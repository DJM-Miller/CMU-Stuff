#Made by Darrin Miller
#Date: 10/9/2022
#Description: Basic console game of hangman intended to be converted to pygame version


from ctypes import sizeof
from random import randint, choice

###########---------Methods----------#######################
def word_choice(wordfilename):
    with open(wordfilename,'r') as fin:
        lines = fin.read().splitlines()
    return choice(lines)

def output(target, correct_set, chances):
    print()
    for i in range(len(target)):
        if i in correct_set:
            print(target[i],' ',end='')
        else:
            print('_',' ',end='')
    print(f"Remaining tries:{chances}")
    print()

###########---------Variables----------#######################
wordFile = 'hangmanWords.txt'
target_word = word_choice(wordFile)
chances = 6
game_active = True
correct_set = set()
###########---------MAIN GAME LOOP----------#######################
while(game_active):
    output(target_word,correct_set,chances)
    print('Enter a character to guess the word:',end='')
    guess = input()
    if(len(guess)!=1):
        print('Invalid Input')
    correct_guess = False
    for i in range(len(target_word)):
        if(guess.lower() == target_word[i]):
            correct_set.add(i)
            correct_guess = True
    if not correct_guess:
        chances -= 1

    
    #End States
    if len(correct_set) == len(target_word):
        print('Congrats You Win!!! We wont hang You.\n')
        print(f'Winning word was {target_word}.\n')
        game_active = False
    if(chances < 1):
        print('LOSER, Hang Them!')
        print(f'Winning word was {target_word}.\n')
        game_active = False
       

#Code to remove words less than 5 and greater than 10 letters from file
#Original word list copied from https://www.mit.edu/~ecprice/wordlist.10000
#Nolonger needed unless new word list created
# with open(wordFile, 'r') as fin:
#     lines = fin.read().splitlines()
# with open(wordFile, 'w') as fout:
#     for i in lines :
#         if(len(i)>=5 and len(i)<=10):
#             fout.write(i)
#             fout.write('\n')