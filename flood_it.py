import sys
from collections import deque


# Read the number of test cases
t = int(sys.stdin.readline())

# Read the board
for test_case in range(t):
    # x = Map dimensions (length)
    n = int(sys.stdin.readline())

    # Set amount of tiles in grid excluding the starting tile
    t, total = 0, n**2 - 1

    # Read Board
    board = [[int(x) for x in list(sys.stdin.readline().strip())] for _ in range(n)]

    visited = [[False for _ in range(len(row))] for row in board]

    def flood_fill(board, x, y, target, count_moves=None):
        n = len(board)
        visited = [[False] * n for _ in range(n)]
        move_counts = {}

        def dfs(x, y, count):
            if x < 0 or x >= n or y < 0 or y >= n or visited[x][y] or board[x][y] != target:
                return count
            visited[x][y] = True
            count += 1
            count = dfs(x - 1, y, count)
            count = dfs(x + 1, y, count)
            count = dfs(x, y - 1, count)
            count = dfs(x, y + 1, count)
            return count

        total_moves = dfs(x, y, 0)
        if count_moves:
            move_counts[target] = total_moves

        board[y][x] = target
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n:
                continue
            if board[new_y][new_x] == target:
                continue
            if count_moves:
                move_counts[board[new_y][new_x]] = dfs(new_x, new_y, 0)
            else:
                dfs(new_x, new_y, 0)
        return total_moves, move_counts

    def find_most_connected_number(board):
        count = {}
        for row in board:
            for value in row:
                if value not in count:
                    count[value] = 0
        for row in range(n):
            for col in range(n):
                visited = [[False for _ in range(len(row))] for row in board]
                count[board[row][col]] += dfs(board, visited, (row, col), board[row][col])
        return max(count, key=count.get)

    def dfs(board, visited, pos, target):
        x, y = pos
        if x < 0 or x >= n or y < 0 or y >= n or visited[x][y]:
            # Position is out of bounds or already visited
            return 0
        visited[x][y] = True
        if board[x][y] != target:
            # Position does not have the target value
            return 0
        count = 1
        count += dfs(board, visited, (x - 1, y), target)  # Left
        count += dfs(board, visited, (x + 1, y), target)  # Right
        count += dfs(board, visited, (x, y - 1), target)  # Up
        count += dfs(board, visited, (x, y + 1), target)  # Down
        return count

    while t < total:
        print(t, " t", total)
        print(find_most_connected_number(board))  # Output: 1
        most_color = find_most_connected_number(board)
        for row in range(n):
            for col in range(n):
                tot_moves, count_moves = flood_fill(board, row, col, most_color, count_moves=True)
                t += tot_moves





