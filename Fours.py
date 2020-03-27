def who_is_winner(pieces_position_list):
    board = dict()
    for i in range(7):
        board.update({'ABCDEF'[j] + str(i): 0 for j in range(6)})

    
    return board


print(who_is_winner([
    "C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
    "D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red",
    "B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"
]))
