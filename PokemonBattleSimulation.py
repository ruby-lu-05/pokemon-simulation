###############################################################################################
#                            RUBY LU - POKEMON BATTLE SIMULATION                              #                
###############################################################################################
                                        # 10/16/2020

# the player and computer each get 1 water type, 1 fire type, and 1 electric type
# dictionary containing the player's pokemon choices and their respective HPs:
p_poks = {"WAILORD":90, "NINETAILS":80, "JOLTEON":110}
# pokemon dictionaries will always be in the order: fire, water, electric
# dictionary containing the computer's pokemon choices and their respective HPs:
c_poks = {"KINGLER":80, "FLAREON":90, "RAICHU":110}
# as the game goes on, pokemon will gradually be deleted from both dictionaries

# copies of the above dictionaries (for reference later in the program)
# difference: unlike the main dictionaries, these items will NOT be changed or deleted
p_poks2 = {"WAILORD":90, "NINETAILS":80, "JOLTEON":110}
c_poks2 = {"KINGLER":80, "FLAREON":90, "RAICHU":110}

# lists containing the pokemon of each type
water = [list(p_poks2)[0], list(c_poks2)[0]]
fire = [list(p_poks2)[1], list(c_poks2)[1]]
elec = [list(p_poks2)[2], list(c_poks2)[2]]

round_counter = 0  # to keep track of rounds

# welcoming the player
print("Welcome to this Pokemon battle simulation!\n"
      "Your opponent is the computer.\n"
      "You may enter 'stop' when choosing an action if you wish the exit the game.\n"
      "\nChoose your Pokemon!")
# giving players a list of pokemon to choose from
for i in p_poks:
    print("- " + i)
# creating input to allow player choice
p_pok = input("Enter Pokemon name: ").upper()
while p_pok not in p_poks:  # continuous user input until answer is valid
    p_pok = input("Invalid Pokemon name. Please try again: ").upper()
# assigning hp based on pokemon choice
p_hp = p_poks[p_pok]

# random pokemon will be chosen by the computer
import random
c_pok = random.choice(list(c_poks.keys()))
c_hp = c_poks[c_pok]

# loop to allow continuous game
while True:
    print("____________________________________________________________")
    round_counter += 1
    # loser is determined by whoever loses all their pokemon first
    if len(p_poks) == 0 and len(c_poks) == 0:
        print("\nYou and your opponent both have no more Pokemon left. It's a tie!")
        break  # game would be over, so loop is exited
    if len(p_poks) == 0 and len(c_poks) != 0:
        print("\nNo more available Pokemon left. You lose.\n"
              "Better luck next time!")
        break
    if len(c_poks) == 0 and len(p_poks) != 0:
        print("\nOpponent has no more Pokemon so you win. Congratulations!")
        break
    
    print("\n                          ROUND " + str(round_counter) + ":\n")

    # random choice with 1/8 chance of True being selected:
    true_false = [True, False, False, False, False, False, False, False]
    import random
    # applying random choice to switching, missing, and critical hits
    c_switch = random.choice(true_false)
    p_miss = random.choice(true_false)
    c_miss = random.choice(true_false)
    p_crit_hit = random.choice(true_false)
    c_crit_hit = random.choice(true_false)

    # SECTION 1: COMPUTER'S CHOICES
    # the computer will choose a new pokemon if their existing pokemon is dead
    if c_pok not in c_poks and len(c_poks) != 0:
        c_pok = random.choice(list(c_poks.keys()))
        c_hp = c_poks[c_pok]
    print("Your opponent sent out " + c_pok + ".")
    print("\n" + c_pok + "\n"
          "HP:[" + int(c_hp/10)*"=" + int((c_poks2[c_pok]-c_hp)/10)*"-" + "]")
    # new random pokemon is selected if the computer ends up switching
    if c_switch == True:
        c_pok = random.choice(list(c_poks.keys()))
        c_hp = c_poks[c_pok]
        c_damage = 0
    # if the computer does not switch, they will choose a move
    else:
        # checking if the chosen pokemon is the water pokemon
        if c_pok == list(c_poks2)[0]:
            c_moves = {"WATER GUN":40, "CRABHAMMER":20, "BUBBLE BEAM":30, "RAZOR SHELL":30}
        # same thing applies for the other pokemon
        if c_pok == list(c_poks2)[1]:
            c_moves = {"LAVA PLUME":30, "FLARE BLITZ":30, "EMBER":10, "FIRE FANG":20}
        if c_pok == list(c_poks2)[2]:
            c_moves = {"THUNDER":30, "ELECTRO BALL":30, "ELECTRIFY":20, "THUNDER WAVE":20}
        # computer choosing a random move (damage is assigned using the dictionary)
        c_move = random.choice(list(c_moves.keys()))
        c_damage = c_moves[c_move]

    # SECTION 2: PLAYER'S CHOICES
    # creating a player switch variable that may be subject to change
    p_switch = False
    # if the player's previous pokemon died, they will get to choose a new one
    if p_pok not in p_poks and len(p_poks) != 0:
        print("\nChoose your Pokemon!")
        # giving players the list of pokemon to choose from
        for i in p_poks:
            print("- " + i)
        # creating input to allow player choice
        p_pok = input("Enter Pokemon name: ").upper()
        while p_pok not in p_poks:  # continuous user input until answer is valid
            p_pok = input("Invalid Pokemon name. Please try again: ").upper()

    # the player will continue with the pokemon from last round if it's not dead
    else:
        # confirming player choice and displaying health bar
        print("\nYou have chosen " + p_pok + ".")
        print("\n" + p_pok + "\n"
              "HP:[" + int(p_hp/10)*"=" + int((p_poks2[p_pok]-p_hp)/10)*"-" + "]"
              + str(int(p_hp)) + "/" + str(p_poks2[p_pok]))
    options = ["SWITCH POKEMON", "FIGHT", "STOP GAME"]
    # player will not have the option to switch if they only have one pokemon
    if len(p_poks) == 1:
        del options[0]
    # asking player what they want to do (by displaying options) and creating input
    print("\nWhat would " + p_pok + " like to do?")
    for i in options:
        print("- " + i)
    confirm = input("Answer: ").upper()
    while confirm not in options:  # continuous user input until answer is valid
        confirm = input("Invalid answer. Please try again: ").upper()
    # allowing player to choose a new pokemon if they want
    if confirm == "SWITCH POKEMON":
        print("\nChoose your new Pokemon!")
        for i in p_poks:
            print("- " + i)
        p_pok = input("Enter Pokemon name: ").upper()
        while p_pok not in p_poks:  # continuous user input until answer is valid
            p_pok = input("Invalid Pokemon name. Please try again: ").upper()
        # updating player pokemon hp and damage 
        p_hp = p_poks[p_pok]
        p_switch = True
        p_damage = 0

    # if they choose to fight, they will be prompted to choose a move
    elif confirm == "FIGHT":
        print("\nPick a move!")
        # checking if the chosen pokemon is the water pokemon
        if p_pok == list(p_poks2)[0]:
            # creating a unique list of moves based on the pokemon type
            p_moves = {"SOAK":30, "MIST":20, "DIVE":10, "WATER GUN":30}
        # same thing applies to all pokemon
        if p_pok == list(p_poks2)[1]:
            p_moves = {"INFERNO":40, "FIRE BLAST":20, "FIRE SPIN":30, "FLAMETHROWER":30}
        if p_pok == list(p_poks2)[2]:
            p_moves = {"THUNDER SHOCK":30, "THUNDER WAVE":40, "CHARGE BEAM":10, "SPARK":20}
        # letting user input answer
        for i in p_moves:
            print("- " + i)
        p_move = input("Enter move: ").upper()
        while p_move not in p_moves:  # continuous user input until answer is valid
            p_move = input("Invalid move. Please try again: ").upper()
        # assigning damage based on player choice
        p_damage = p_moves[p_move]
            
    # the only other choice would be to stop the game
    else:
        print("Game has stopped.")
        break  # breaking the loop if the player wants to exit

    # SECTION 3: APPLYING ELEMENTAL MULTIPLIERS
    # player or computer damage will be doubled if the conditions are satisfied
    if (p_pok in water and c_pok in fire) or (p_pok in elec and c_pok in water):
        p_damage = p_damage*2
    if (c_pok in water and p_pok in fire) or (c_pok in elec and p_pok in water):
        c_damage = c_damage*2
    # player or computer damage will be divided by 2 if the conditions are satisfied
    if p_pok in fire and c_pok in water:
        p_damage = p_damage/2
    if c_pok in fire and p_pok in water:
        c_damage = c_damage/2
    # if the two pokemon are the same type, both damage values will also be divided by 2
    if (c_pok in water and p_pok in water) or (c_pok in fire and p_pok in fire)\
       or (c_pok in elec and p_pok in elec):
        p_damage = p_damage/2
        c_damage = c_damage/2

    # SECTION 4: BATTLE
    print("\n------------------------------------------------------------"
          "\n                     TIME TO BATTLE!"
          "\n------------------------------------------------------------\n")
    # dialogue depending on whether the computer is switching or fighting
    if c_switch == True:
        print("Your opponent has switched their Pokemon to " + c_pok + ".")
    # applying possible critical hit or miss
    elif c_miss == True:
        c_damage = 0
        print(c_pok + " tried to attack with " + c_move + " but missed.")
    else:
        print(c_pok + " has attacked with " + c_move + ".")
        if c_crit_hit == True:
            c_damage == c_damage*2
            print("Critical hit!")
        # dialogue depending on the amount of damage done
        if c_damage >= 60:
            print("Ouch!")
        if c_damage <= 10:
            print("Not so effective...")

    # outputting the player's actions
    print()
    if p_switch == True:
        print("You have switched your Pokemon to " + p_pok + ".")
    # applying possible critical hits or misses
    elif p_miss == True:
        p_damage = 0
        print(p_pok + " tried to attack with " + p_move + " but missed. Yikes!")
    else:
        print(p_pok + " has attacked with " + p_move + ".")
        if p_crit_hit == True:
            p_damage = p_damage*2
            print("Critical hit!")
        # dialogue depending on the amount of damage done
        if p_damage == 40 and p_crit_hit == False:
            print("Great choice!")
        if p_damage <= 10:
            print("Not so effective...")

    # updating player and computer health
    p_hp -= c_damage
    c_hp -= p_damage

    # updating hp values in the main dictionary
    p_poks[p_pok] = p_hp
    c_poks[c_pok] = c_hp

    # outputting the new pokemon health bars
    print("\n" + p_pok + " (You)")
    if p_hp <= 0:  # making sure the hp doesn't go into the negatives
        print("HP:[" + int((p_poks2[p_pok])/10)*"-" + "]")
        print(p_pok + " has fainted! You may no longer choose this Pokemon.")
        # the player's pokemon will be deleted from the main dictionary when dead
        del p_poks[p_pok]
    else:  # displaying hp as a fraction of the original hp
        print("HP:[" + int(p_hp/10)*"=" + int((p_poks2[p_pok]-p_hp)/10)*"-" + "]"
              + str(int(p_hp)) + "/" + str(p_poks2[p_pok]))
    # warning user when their pokemon's health is low or their pokemon is dead
    if 0 < p_hp <= 10:
        print("Warning! " + p_pok + " is in critical condition.")

    print("\n" + c_pok + " (Opponent)")
    if c_hp <= 0:
        print("HP:[" + int((c_poks2[c_pok])/10)*"-" + "]")
        # informing user if one of their opponent's pokemon is dead
        print(c_pok + " (your opponent) has fainted!")
        # the computer's pokemon will also be deleted from the main dictionary when dead
        del c_poks[c_pok]
    else:
        print("HP:[" + int(c_hp/10)*"=" + int((c_poks2[c_pok]-c_hp)/10)*"-" + "]")
    print()
