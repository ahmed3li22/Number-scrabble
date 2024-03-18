#File: CS112_A1_T2_2_20230525
#Purpose: Number scrabble game. each player takes 3 number in turns. the player who take
#          3 numbers with sum = 15 wins the game
#Author: Ahmed Ali Ahmed Somida
#ID: 20230525
def Number_scrabble ():
    #selecting the data types for the numbers that can be chosen
    available_numbers=[1,2,3,4,5,6,7,8,9]
    #introducinng 2 list for each player's selected numbers
    player1_numbers=[]
    player2_numbers=[]
    counter=0
    #welcome message and available numbers and current game status
    print("welcome to the game")
    print(f"Available numbers are:{available_numbers}")
    print(f"player 1 numbers are {player1_numbers}")
    print(f"player 2 numbers are {player2_numbers}")
    #determining which player will take the turn
    while True:
        if counter % 2 == 0:
            current_player = "Player 1"
            player_numbers = player1_numbers
        else:
            current_player = "Player 2"
            player_numbers = player2_numbers
        #make sure that the user inter an available intger not anything else
        try:
            choose_number = int(
                input(f"{current_player}, please choose an available number from {available_numbers}: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if choose_number not in available_numbers:
            print("This number is not available. Please select one from available numbers.")
            continue
        # Remove the number from available numbers
        available_numbers.remove(choose_number)

        # Adding the number to the list of the player
        player_numbers.append(choose_number)

        # Check if the player won (when 3 numbers of his list equal 15)
        if counter >= 4:
            for i in range(len(player_numbers)):
                for j in range(i + 1, len(player_numbers)):
                    for k in range(j + 1, len(player_numbers)):
                        if player_numbers[i] + player_numbers[j] + player_numbers[k] == 15:
                            print(f"{current_player} wins!")
                            return

        # Check if there are no available numbers and showing the result
        if len(available_numbers) == 0:
            print("Draw")
            print(f"player 1 numbers are: {player1_numbers}")
            print(f"player 2 numbers are: {player2_numbers}")
            return

        # Incrementing the counter for the next round of selection
        counter += 1

        # Print available numbers for the player to choose
        print(f"Available numbers are: {available_numbers}")
        print(f"player 1 numbers are: {player1_numbers}")
        print(f"player 2 numbers are: {player2_numbers}")

#starting the program
Number_scrabble()