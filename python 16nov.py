#Rock, paper, scissors game

player1 = input("Player1 - rock, paper, scissors : ")
player2 = input("Player2 - rock, paper, scissors : ")
if player1 == player2:
    print("Draw!!!!!!!")
elif(player1== "rock" and player2== "scissors"):
    print("Player1 wins")
elif(player1== "scissors" and player2== "paper"):
    print("Player1 wins")
elif(player1== "paper" and player2== "rock"):
    print("Player1 wins")
elif(player2== "rock" and player1== "scissors"):
    print("Player2 wins")
elif(player2== "scissors" and player1== "paper"):
    print("Player2 wins")
elif(player2== "paper" and player1== "rock"):
    print("Player2 wins")

#guess the number game

min=1
max=100
reply=""
print("Guess a number between 1 to 100.")

while reply != "yes":
    logic = (min+max)//2
    print("My guess is ",logic,"?""(Enter yes/greater/lesser)")
    reply = input()
    if reply == "greater":
        min = logic
    elif reply == "lesser":
        max = logic
    elif reply == "yes":
        print("I guessed it")
    else:
        print("Invalid")

