import random


def play():
    print("Choose:\n 'r' for rock \n 's' for scissors \n 'p' for paper ")
    player1 = input("Your pick: ").lower()
    player2 = random.choice(['r', 'p', 's'])
    print(f'The computer picked: {player2}')

    if player1 == player2:
        print("It is a draw!")
        exit()

    def is_win():
        if (player1 == 'p' and player2 == 'r') or (player1 == 's' and player2 == 'p') or (
                player1 == 'r' and player2 == 's'):
            return True

    if is_win() is True:
        print("Humans won")
    else:
        print("Computer won")


play()


