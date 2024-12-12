def count_xmas(grid):
    def search_word(word, x, y, dx, dy):
        for i in range(len(word)):
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == word[i]):
                return False
            x += dx
            y += dy
        return True

    word = "XMAS"
    directions = [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1), (-1, 1)]
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for dx, dy in directions:
                if search_word(word, i, j, dx, dy):
                    count += 1

    return count

# Example usage
grid = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX"
]
# with open('/Users/francis.joseph/dev/adventofcode/day4_1.txt') as f:
#     grid = [line.strip() for line in f.readlines()]
#     print(count_xmas(grid))  # Output: 18

def count_x_mas(grid):
    def search_x_mas(x, y):
        patterns = [
            [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)],  # Normal X-MAS
            [(2, 2), (2, 0), (1, 1), (0, 0), (0, 2)],  # Rotated 180 degrees
            [(0, 0), (2, 0), (1, 1), (2, 2), (0, 2)],  # Rotated 90 degrees clockwise
            [(0, 2), (2, 2), (1, 1), (0, 0), (2, 0)]   # Rotated 90 degrees counterclockwise
        ]
        for pattern in patterns:
            if all(0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] == 'M' for dx, dy in pattern[:2]) and \
                all(0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] == 'A' for dx, dy in pattern[2:3]) and \
                all(0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] == 'S' for dx, dy in pattern[3:]):
                return True
        return False

    count = 0
    for i in range(len(grid) - 2):
        for j in range(len(grid[0]) - 2):
            if search_x_mas(i, j):
                count += 1

    return count

# Example usage
with open('/Users/francis.joseph/dev/adventofcode/2024/day4.txt') as f:
    grid = [line.strip() for line in f.readlines()]
    print(count_x_mas(grid))  # Output: 9