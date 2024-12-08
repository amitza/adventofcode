from utils.utils import read_input_lines


def cube_conundrum_part_1(s: str, red: int, blue: int, green: int) -> int:
    game_id, game = s.split(': ')
    rounds = game.split('; ')
    for r in rounds:
        cubes = r.split(', ')
        for c in cubes:
            amount, color = c.split(' ')
            if color == 'red':
                if int(amount) > red:
                    return 0
            elif color == 'blue':
                if int(amount) > blue:
                    return 0
            elif color == 'green':
                if int(amount) > green:
                    return 0

    return int(game_id.split(' ')[-1])


def cube_conundrum_part_2(s: str) -> int:
    max_colors = {'red': 0, 'blue': 0, 'green': 0}
    game_id, game = s.split(': ')
    rounds = game.split('; ')
    for r in rounds:
        cubes = r.split(', ')
        for c in cubes:
            amount, color = c.split(' ')
            if int(amount) > max_colors[color]:
                max_colors[color] = int(amount)
    return max_colors['red'] * max_colors['blue'] * max_colors['green']


if __name__ == '__main__':
    total = 0
    total_pow = 0
    for line in read_input_lines():
        total += cube_conundrum_part_1(s=line, red=12, green=13, blue=14)
        total_pow += cube_conundrum_part_2(s=line)
    print(f'total games id: {total}')
    print(f'total power of games: {total_pow}')
