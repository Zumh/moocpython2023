# Write your solution here
def who_won(game_board: list[list[int]])->int:
    player_1 = 0
    player_2 = 0
    for board in game_board:
        for player in board:
            if  player == 1:
                player_1 += 1
            elif player == 2:
                player_2 += 1
    value = 1
    if player_1 == player_2:
        value = 0
    elif player_1 < player_2:
        value = 2
    
    return value