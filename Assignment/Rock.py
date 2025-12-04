#collect ans input frm the userin the terminal and call it player1_input
#check if both inputs are the same and display TIE if they are
#check if the first input is scissors amd the second input is paper then display player1 wins
#otherwise if vice versa display





#A function is any keyword that requires a paranthesis beside it

message = "ENter a Rock, or papare or scissors: "

player1 = input(message).lower()
player2 = input(message).lower()

#player1 = player1.lower()
#player2 = player2.lower()

if player1 == player2:
    print("TIE")

elif player1 == 'scissors' and player2 == 'paper':
    print("player1 Wins")

elif player2 == 'scissors' and player1 == 'paper':
    print("player2 Wins")

elif player1 == 'rock' and player2 == 'scissor':
    print("player1 Wins")

elif player2 == 'rock' and player1 == 'scissor':
    print("player2 Wins")

elif player1 == 'rock' and player2 == 'paper':
    print("player2 Wins")

elif player2 == 'rock' and player1 == 'paper':
    print("player1 Wins")

else: print("Invalid Input")
