# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str)->bool:

    min_size = 0
    max_size = 3
    if min_size <= x < max_size and min_size <= y < max_size:
        slot = game_board[y][x] 
        if slot == "":
            game_board[y][x] = piece
            return True 
    return False 

            
