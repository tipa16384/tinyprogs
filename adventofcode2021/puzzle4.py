import re

puzzle_data_file = 'puzzle4.dat'


def get_balls(fp):
    "given a file pointer, return the first line as an array of comma-separated integers"
    return [int(x) for x in fp.readline().split(',')]


def get_matrix(fp):
    """
    given a file pointer, skip the first line and read the next five lines as a
    5x5 matrix of integers separated by spaces
    """
    while fp.readline() != '':
        matrix = []
        for i in range(5):
            matrix.append([int(x)
                           for x in re.split(u'\s+', fp.readline().strip())])
        yield matrix


def sanity_check():
    "open the puzzle data file and print the return from get_balls() and get_matrix()"
    with open(puzzle_data_file, 'r') as fp:
        print(get_balls(fp))
        for matrix in get_matrix(fp):
            print(matrix)


def mark_ball_in_board(ball, matrix):
    "mark the ball in the board"
    for row in matrix:
        if ball in row:
            row[row.index(ball)] = -1


def mark_ball_in_boards(ball, matrices):
    "mark the ball in all the boards"
    for matrix in matrices:
        mark_ball_in_board(ball, matrix)


def winning_board(matrix):
    "return True if any row or column is -1"
    for row in matrix:
        if sum(row) == -5:
            return True
    for i in range(5):
        if sum([row[i] for row in matrix]) == -5:
            return True
    return False


def get_winning_boards(matrices):
    "return a list of winning boards"
    winning_boards = []
    for matrix in matrices:
        if winning_board(matrix):
            winning_boards.append(matrix)
    return winning_boards


def play_bingo(part2=False):
    "read the puzzle data file and get the balls and the matrix"
    with open(puzzle_data_file, 'r') as fp:
        balls = get_balls(fp)
        matrices = list(get_matrix(fp))
        for ball in balls:
            mark_ball_in_boards(ball, matrices)
            winning_boards = get_winning_boards(matrices)
            if winning_boards:
                if not part2 or len(matrices) == 1:
                    assert len(winning_boards) == 1
                    return ball, winning_boards[0]
                else:
                    for board in winning_boards:
                        matrices.remove(board)

    raise Exception('no winning board found')


def score_board(ball, board):
    "return product of the ball and the sum of all the numbers in the board that are not -1"
    return ball * sum([sum([x for x in row if x != -1]) for row in board])


if __name__ == '__main__':
    # sanity_check()
    ball, board = play_bingo(False)
    print(score_board(ball, board))
    ball, board = play_bingo(True)
    print(score_board(ball, board))
