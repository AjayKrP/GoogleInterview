def connect_four():
    row = 6
    col = 7
    board = [[0 for _ in range(col)] for _ in range(row)]
    row_index = [0 for _ in range(col)]
    curr = 0
    while True:
        user = 1 if curr % 2 == 0 else 2
        y = int(input(f'user {user} column choice? '))
        x = row_index[y]
        if x < 0 or x >= row or y < 0 or y >= col or board[x][y] != 0:
            print('bad move!')
            continue
        board[x][y] = user
        row_index[y] += 1
        if check_winning_position(board, x, y, row, col, user):
            print(f'user {user} has won the game!')
            return
        curr += 1
        if curr == row * col:
            print(f'game tie!')
            return


def check_winning_position(board, x, y, row, col, current_choice):
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [1, 1], [1, -1], [1, 1]]
    print(board)
    for i in range(len(directions)):
        consecutive_items = 1
        cx = directions[i][0] + x
        cy = directions[i][1] + y
        while cx >= 0 or cx < row or cy >= 0 or cy < col:
            if board[cx][cy] == current_choice:
                consecutive_items += 1
            else:
                break
            if consecutive_items == 4:
                return True
            cx += directions[i][0]
            cy += directions[i][1]
    return False


connect_four()
