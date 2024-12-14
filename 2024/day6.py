def parse_map(map_str):
    return [list(line) for line in map_str.strip().split('\n')]

def print_map(map_grid):
    for line in map_grid:
        print(''.join(line))

def move_guard(map_grid, start_pos, start_dir):
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    visited = set()
    x, y = start_pos
    direction = start_dir

    while 0 <= x < len(map_grid) and 0 <= y < len(map_grid[0]):
        visited.add((x, y))
        map_grid[x][y] = 'X'

        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy

        if 0 <= nx < len(map_grid) and 0 <= ny < len(map_grid[0]) and map_grid[nx][ny] != '#':
            x, y = nx, ny
        else:
            direction = turn_right[direction]
        if nx < 0 or nx >= len(map_grid) or ny < 0 or ny >= len(map_grid[0]):
            break
        

    return visited

def find_start_position(map_grid):
    directions = ['^', '>', 'v', '<']
    for i, row in enumerate(map_grid):
        for direction in directions:
            if direction in row:
                start_pos = (i, row.index(direction))
                map_grid[i][row.index(direction)] = '.'
                return start_pos, direction
    return None, None



def find_loop_positions(map_grid, start_pos, start_dir):
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    loop_positions = set()

    for i in range(len(map_grid)):
        progress = (i + 1) / len(map_grid) * 100
        print(f'Progress: [{("=" * int(progress // 2)).ljust(50)}] {progress:.2f}%', end='\r')
        for j in range(len(map_grid[0])):
            if (i, j) == start_pos or map_grid[i][j] == '#':
                continue

            temp_grid = [row[:] for row in map_grid]
            temp_grid[i][j] = '#'
            visited = set()
            x, y = start_pos
            direction = start_dir

            while 0 <= x < len(temp_grid) and 0 <= y < len(temp_grid[0]):
                if (x, y, direction) in visited:
                    loop_positions.add((i, j))
                    break
                visited.add((x, y, direction))
                temp_grid[x][y] = 'X'

                dx, dy = directions[direction]
                nx, ny = x + dx, y + dy

                if 0 <= nx < len(temp_grid) and 0 <= ny < len(temp_grid[0]) and temp_grid[nx][ny] != '#':
                    x, y = nx, ny
                else:
                    direction = turn_right[direction]
                if nx < 0 or nx >= len(temp_grid) or ny < 0 or ny >= len(temp_grid[0]):
                    break

    return loop_positions

    
def main():
    with open('/Users/francis.joseph/dev/adventofcode/2024/day6.txt', 'r') as file:
        map_str = file.read()
#         map_str = """
# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...
# """
        map_grid = parse_map(map_str)
        start_pos, start_dir = find_start_position(map_grid)

        # visited_positions = move_guard(map_grid, start_pos, start_dir)
        loop_positions = find_loop_positions(map_grid, start_pos, start_dir)
        print(f"Possible positions for new obstruction: {len(loop_positions)}")
    
    print_map(map_grid)
    # print(f"Distinct positions visited: {len(visited_positions)}")
    print(f"Num of loop positions: {len(loop_positions)}")


if __name__ == "__main__":
    main()

