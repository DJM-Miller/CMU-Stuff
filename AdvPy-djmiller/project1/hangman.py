# Main Author: Darrin Miller
# Project Start Date: 10/9/2022
# Description: Creating a game for my advanced python class using pygame


import pygame
from sys import exit
from random import randint, choice
from time import sleep

pygame.init()

#Holds player information
class Player:
    count = 0

    def __init__(self,name,wins,games):
        self.name = name
        self.wins = int(wins)
        self.games = int(games)
        Player.count += 1
#read in player data from file and fills player_list
def read_player_data(player_list):
    input = []
    count = 0
    with open(playerFile, 'r') as fin:
        for line in fin:
            for word in line.split():
                input.append(word)
            player_list.append(Player(input[0],input[1],input[2]))
           
            input.clear()
#writes updated data to file
def write_player_data(player_list):
    with open(playerFile, 'w') as fout:
        for player in player_list:
            fout.write(f"{player.name} {player.wins} {player.games}\n")
#displays menu
def menu_screen():
    mystring = "Welcome " + curr_player.name
    welcome_surf = hangman_font.render(mystring, False,'Black')
    welcome_rect = welcome_surf.get_rect(center = (500,75))
    mystring2 = "Press Space to Start Game"
    start_surf = hangman_font.render(mystring2,False,'White')
    start_rect = start_surf.get_rect(center = (500,450))
    esc_surf = hangman_font2.render("Enter esc to Exit", False, 'Black')
    esc_rect = esc_surf.get_rect(center = (250,200))
    login_surf = hangman_font2.render("Enter 1 to Login", False, 'Black')
    login_rect = login_surf.get_rect(center = (250,350))
    create_surf = hangman_font2.render("Enter 2 to Create Player", False, 'Black')
    create_rect = create_surf.get_rect(center = (750,200))
    stat_surf = hangman_font2.render("Enter 3 to View Stats", False, 'Black')
    stat_rect = stat_surf.get_rect(center = (750,350))

    display_hangpost(0)
    screen.blit(welcome_surf,welcome_rect)
    screen.blit(start_surf,start_rect)
    screen.blit(esc_surf,esc_rect)
    screen.blit(login_surf,login_rect)
    screen.blit(create_surf,create_rect)
    screen.blit(stat_surf,stat_rect)
#displays win or lose scree
def win_lose_screen(mystring, won):
    target_surf = hangman_font.render(mystring, False,'Black')
    target_rect = target_surf.get_rect(center = (500,75))
    mystring2 = "The target word was " + target_word 
    guess_surf = hangman_font.render(mystring2,False,'White')
    guess_rect = guess_surf.get_rect(center = (500,440))
    return_surf = hangman_font.render('Returning To Menu.',False,'White')
    return_rect = return_surf.get_rect(center = (500,475))


    screen.blit(background_surf,(0,0))
    if won:
        display_hangpost(0)
    else:
        display_hangpost(6)
    screen.blit(target_surf,target_rect)
    screen.blit(guess_surf,guess_rect)
    screen.blit(return_surf,return_rect)
    pygame.display.update()
    sleep(3)
#Displays back ground and hangpost based on inded
def display_hangpost(index):
    hang_suf = hangposts[index]
    hang_rect = hang_suf.get_rect(topleft = (300,100))
    screen.blit(background_surf,(0,0))
    screen.blit(hang_suf,hang_rect)  
#selects random word from file for game
def pick_target_word(wordfilename):
    with open(wordfilename,'r') as fin:
        lines = fin.read().splitlines()
    return choice(lines)
#Shows correct letters and place of missing letters      
def display_correct(myset):
    mystring = ''
    for i in target_word:
        if i in myset:
            mystring += i + ' '
        else:
            mystring += '_ '
    target_surf = hangman_font.render(mystring, False,'Black')
    target_rect = target_surf.get_rect(center = (500,75))
    screen.blit(target_surf,target_rect)
#displays current incorrect guess
def display_guesses():
    guess_surf = hangman_font.render(set_to_str(guess_set),False,'White')
    guess_rect = guess_surf.get_rect(center = (500,450))
    screen.blit(guess_surf,guess_rect)
#converts set to string
def set_to_str(myset):
    mystring = ''
    for i in myset:
        mystring += i + ' '
    return mystring
#determins if win has occured
def win_state():
    for i in target_word:
        if i not in correct_set:
            return False
    return True   
#displays a screen
def enter_player_screen(Input_name):
    prompt = 'Enter Your Player Name: ' + Input_name
    prompt_surf = hangman_font.render(prompt, False, 'Black')
    prompt_rect = prompt_surf.get_rect(bottomleft = (150,95))

    display_hangpost(0)
    screen.blit(prompt_surf,prompt_rect)
#displays a screen
def player_found_screen(Input_name):
    prompt = f'Welcome Back {Input_name}'
    prompt_surf = hangman_font.render(prompt, False, 'Black')
    prompt_rect = prompt_surf.get_rect(bottomleft = (150,95))

    display_hangpost(0)
    screen.blit(prompt_surf,prompt_rect)
    pygame.display.update()
    sleep(2)
#displays a screen
def player_nfound_screen(Input_name):
    prompt = f'Player {Input_name} Not Found Set to Default Player'
    prompt_surf = hangman_font.render(prompt, False, 'Black')
    prompt_rect = prompt_surf.get_rect(bottomleft = (150,95))

    display_hangpost(0)
    screen.blit(prompt_surf,prompt_rect)
    pygame.display.update()
    sleep(3)
#displays a screen
def player_new_screen(Input_name):
    prompt = f'Welcome to the game {Input_name}!'
    prompt_surf = hangman_font.render(prompt, False, 'Black')
    prompt_rect = prompt_surf.get_rect(bottomleft = (150,95))

    display_hangpost(0)
    screen.blit(prompt_surf,prompt_rect)
    pygame.display.update()
    sleep(2)
#displays a screen
def stat_screen():
    title = f"{curr_player.name}'s Stat Overview"
    title_surf = hangman_font.render(title,False,'Black')
    title_rect = title_surf.get_rect(center =(500,75))
    win_surf = hangman_font.render(f"Wins: {curr_player.wins}",False,'Black')
    win_rect = win_surf.get_rect(center = (350,200))
    game_surf = hangman_font.render(f"Games: {curr_player.games}",False,'Black')
    game_rect = game_surf.get_rect(center = (650,200))
    if curr_player.games > 0:
        percentage = float(curr_player.wins / curr_player.games)
    else:
        percentage = 0.00
    myperc = "Win Percentage: {0:.2g}".format(percentage)
    perc_surf = hangman_font.render(myperc,False,'Black')
    perc_rect = perc_surf.get_rect(center = (500,325))
    mystring2 = "Press Space to Return to Menu"
    return_surf = hangman_font.render(mystring2,False,'White')
    return_rect = return_surf.get_rect(center = (500,450))

    display_hangpost(0)
    screen.blit(title_surf,title_rect)
    screen.blit(win_surf,win_rect)
    screen.blit(game_surf,game_rect)
    screen.blit(perc_surf,perc_rect)
    screen.blit(return_surf,return_rect)

##########------Initializations-------#####################
#Screen & framerate
screen_width_height = (1000,500)
screen = pygame.display.set_mode(screen_width_height)
pygame.display.set_caption("DJ's Hangman Game")
game_clock = pygame.time.Clock()

#Background
#image taken from "https://www.freepik.com/free-vector/wild-west-desert-landscape-cartoon-seamless-scene-game-cactus-nature-interface-vector-illustration_10602892.htm#page=4&query=wild%20west&position=3&from_view=search&track=sph" Image by macrovector</a> on Freepik
background_surf = pygame.image.load('graphics/WildWest1.jpg').convert()
background_surf = pygame.transform.scale(background_surf,(1000,500))

#Hangpost and Character
#images for hangpost and hangman->0 is no hanging 6 is completely hung
hangpost0 = pygame.image.load('graphics/hangposts/hangpost0.png').convert_alpha()
hangpost1 = pygame.image.load('graphics/hangposts/hangpost1.png').convert_alpha()
hangpost2 = pygame.image.load('graphics/hangposts/hangpost2.png').convert_alpha()
hangpost3 = pygame.image.load('graphics/hangposts/hangpost3.png').convert_alpha()
hangpost4 = pygame.image.load('graphics/hangposts/hangpost4.png').convert_alpha()
hangpost5 = pygame.image.load('graphics/hangposts/hangpost5.png').convert_alpha()
hangpost6 = pygame.image.load('graphics/hangposts/hangpost6.png').convert_alpha()
hangposts = [hangpost0,hangpost1,hangpost2,hangpost3,hangpost4,hangpost5,hangpost6]

#Text
hangman_font = pygame.font.Font(None,50)
hangman_font2 = pygame.font.Font(None,30)

##########------Importand Variables-------#####################
hangman_inmenu = False
hangman_ingame = False
hangman_login = True
hangman_create = False
hangman_stats = False

chances_remaining = 6
guess_set = set()
correct_set = set()
wordFile = 'hangmanWords.txt'
playerFile = 'playerData.txt'
target_word = ""
player_name = ""
Player_list = []
read_player_data(Player_list)
curr_player = Player_list[0] #Default Player if no one logs in


#-------------------------------------------------------------------#
##########------Main Loop of Game-------#############################
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            write_player_data(Player_list)
            pygame.quit()
            exit()
        #Running Menu
        if hangman_inmenu:
            if event.type == pygame.KEYDOWN:
                #Quit Game
                if event.key == pygame.K_ESCAPE: 
                    write_player_data(Player_list)
                    pygame.quit()
                    exit()
                #Start New Game
                if event.key == pygame.K_SPACE:
                    hangman_ingame = True
                    hangman_inmenu = False
                    target_word = pick_target_word(wordFile)
                    #print(target_word) #uncomment to print target word in console for testing  
                    correct_set.clear()
                    guess_set.clear()
                    chances_remaining = 6
                #View Player Stats
                if event.key == pygame.K_1:
                    hangman_inmenu = False
                    hangman_login = True
                #Login or Create New Player
                if event.key == pygame.K_2: 
                    hangman_inmenu = False
                    hangman_create = True
                #View Player Stats
                if event.key == pygame.K_3: 
                    hangman_inmenu = False
                    hangman_stats = True
                    
        #Running Game
        if hangman_ingame:
            if event.type == pygame.KEYDOWN and event.unicode.isalpha():
                #print(event.unicode)
                if event.unicode.lower() in target_word:
                    correct_set.add(event.unicode.lower())
                if (event.unicode.lower() not in target_word) and (event.unicode.lower() not in guess_set):
                    guess_set.add(event.unicode.lower())
                    chances_remaining-=1 
        #Running Login
        if hangman_login:
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    player_name += event.unicode.upper()
                if event.key == pygame.K_BACKSPACE:
                    player_name = ""
                if event.key == pygame.K_RETURN:
                    found = False
                    for player in Player_list:
                        if player_name == player.name:
                            curr_player = player
                            found = True
                            player_found_screen(curr_player.name)
                    if not found:
                        curr_player = Player_list[0]
                        player_nfound_screen(player_name)
                    #Enter new name into player file
                    hangman_login = False
                    hangman_inmenu = True
                    player_name = ""
        #Running Create New Player
        if hangman_create:
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    player_name += event.unicode.upper()
                if event.key == pygame.K_BACKSPACE:
                    player_name = ""
                if event.key == pygame.K_RETURN:
                    found = False
                    for player in Player_list:
                        if player_name == player.name:
                            curr_player = player
                            found = True
                            player_found_screen(curr_player.name)
                    if not found:
                        if len(player_name) > 0:
                            Player_list.append(Player(player_name,0,0))
                            curr_player = Player_list[-1]
                            player_new_screen(curr_player.name)
                    hangman_create = False
                    hangman_inmenu = True
                    player_name = ""
        #Running Stats 
        if hangman_stats:
            stat_screen()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                hangman_inmenu = True
                hangman_stats = False



                     
    if hangman_ingame:
            screen.blit(background_surf,(0,0))
            display_hangpost(6-chances_remaining)
            display_correct(correct_set)
            display_guesses()

            if win_state():
                hangman_ingame = False
                hangman_inmenu = True
                curr_player.wins+=1
                curr_player.games+=1
                win_lose_screen("Congrats! You Won!!!",True)
            if chances_remaining < 1:
                hangman_ingame = False
                hangman_inmenu = True
                curr_player.games+=1
                win_lose_screen("Sorry, You Lost",False)

    elif hangman_inmenu:
        menu_screen()

    elif hangman_login:
         enter_player_screen(player_name)
    
    elif hangman_create:
        enter_player_screen(player_name)
    

        
    #updatescreen
    pygame.display.update()
    game_clock.tick(60)
