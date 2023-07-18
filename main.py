def create_board():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board


def display_board(board):
    print('---------')
    for row in board:
        print('|', end='')
        for cell in row:
            print(cell, end='|')
        print('\n---------')


def check_winner(board):
    # Проверка горизонтальных и вертикальных линий
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    # Ничья
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return 'Ничья'

    # Игра продолжается
    return None


# Функция для выполнения хода игрока
def make_move(board, row, col, player):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False


# Основная функция игры
def play_game():
    board = create_board()
    current_player = 'X'

    while True:
        display_board(board)

        # Ход игрока
        print('Ход игрока', current_player)
        row = int(input('Введите номер строки (0, 1 или 2): '))
        col = int(input('Введите номер столбца (0, 1 или 2): '))

        if make_move(board, row, col, current_player):
            winner = check_winner(board)
            if winner:
                display_board(board)
                print('Победитель:', winner)
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print('Некорректный ход. Попробуйте ещё раз.')


# Запуск игры
play_game()