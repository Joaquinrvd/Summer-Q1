def RPS():
    print("welcome to Rock, Paper, Scissors!")
    player1 = input("Player 1, Please enter your name: ")
    player2 = input("Player 2, Please enter your name: ")
   
    p1_choice = input(f"{player1}, chose between Rock, Paper, & Scissors ").lower()

    while not IsValidMove(p1_choice):
        print("is not valid move try again")
        p1_choice = input(f"{player1}, chose between Rock, Paper, & Scissors ").lower()
    
    p2_choice = input(f"{player2}, chose between Rock, Paper, & Scissors ").lower()
   
    while not IsValidMove(p2_choice):
        print("is not valid move try again")
        p2_choice = input(f"{player2}, chose between Rock, Paper, & Scissors ").lower()



    if p1_choice == "rock" and p2_choice == "scissors":
        print(f"Rock beats Scissors, {player1} wins! ")
    elif p1_choice == "paper" and p2_choice == "rock":
        print(f"paper beats rock, {player1} wins! ")
    elif p1_choice == "scissors" and p2_choice == "paper":
        print(f"scissors beats paper, {player1} wins! ")
    elif p1_choice == "rock" and p2_choice == "rock":
        print(f"rock and rock are the same! No one wins! ")
    elif p1_choice == "paper" and p2_choice == "paper":
        print(f"paper and paper are the same! No one wins! ")
    elif p1_choice == "scissors" and p2_choice == "scissors":
        print(f"scissors and scissors are the same! No one wins! ")
    elif p2_choice == "paper" and p1_choice == "rock":
        print(f"paper beats rock, {player2} wins! ")
    elif p2_choice == "rock" and p1_choice == "scissors":
        print(f"rock beats scissors, {player2} wins! ")
    elif p2_choice == "scissors" and p1_choice == "paper":
        print(f"scissors beats paper, {player2} wins! ")

def IsValidMove(playerMove):
    validMoves = ["rock", "paper", "scissors"]

    if playerMove in validMoves:
        return True
    else:
        return False

RPS()
