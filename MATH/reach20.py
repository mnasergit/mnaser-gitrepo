import random

def reach20_game(number, max_number, max_add):
    remaining_number = max_number - number
    LIST = []
    while remaining_number <= 20:
        # Player's turn
        player_add = int(input("Player's turn: "))
        while player_add > max_add or player_add > remaining_number or player_add <= 0:
            print("Invalid input! You can only add between 1 and", min(max_add, remaining_number))
            player_add = int(input("Player's turn: "))
        number += player_add
        remaining_number -= player_add
        if number == 20:
            for i in range (1, player_add+1):
                LIST.append(f"{len(LIST)+1}P")
            print (LIST)
            print("Player wins!")
            break
        for i in range (1, player_add+1):
            LIST.append(f"{len(LIST)+1}P")
        
        # Computer's turn
        if remaining_number == 2:
            computer_add == remaining_number
            print("Computer's turn:", computer_add)
            number += computer_add
            for i in range (1, computer_add+1):
                LIST.append(f"{len(LIST)+1}C")
            
            print (LIST)
            print("Computer wins!")
            print("")
            break
        elif remaining_number == 1:
            computer_add == remaining_number
            print("Computer's turn:", computer_add)
            number += computer_add
            for i in range (1, computer_add+1):
                LIST.append(f"{len(LIST)+1}C")
            print (LIST)
            print("Computer wins!")
            print("")
            break
        else:
            computer_add = random.randint(1, 2)
            print("Computer's turn:", computer_add)
            number += computer_add
            remaining_number -= computer_add
            for i in range (1, computer_add+1):
                LIST.append(f"{len(LIST)+1}C")
            print (LIST)
            print("")

# Example usage:
start_number = 0  # Initial number of objects
max_number = 20
max_add = 2  # Maximum number of objects a player can add in one turn

reach20_game(start_number, max_number, max_add)