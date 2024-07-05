from utils.utils import read_input_lines


def add_part_in_gear_map(gears: dict[int, dict[int, list[int]]], i: int, j: int, part_i: int, part: int) -> None:
    if i not in gears.keys():
        gears[i] = {j: [part]}
    else:
        if j not in gears[i].keys():
            gears[i][j] = [part]
        else:
            gears[i][j].append(part)


def gear_ratios(mat: list[str]) -> (list[int], int):
    valid_signs = set('0123456789.')
    parts = []
    n = len(mat)
    gears: dict[int, dict[int, list[int]]] = {}
    for i, line in enumerate(mat):
        j = 0
        m = len(line)
        while j < m:
            if line[j].isdigit():
                k = j + 1
                while k < m and mat[i][k].isdigit():
                    k += 1
                print(f'{i + 1}: {j} -> {k} [{mat[i][j:k]}]')
                if i > 0 and j > 0 and mat[i - 1][j - 1] not in valid_signs:
                    parts.append(int(mat[i][j:k]))
                    if mat[i - 1][j - 1] == '*':
                        add_part_in_gear_map(gears=gears, i=i - 1, j=j - 1, part_i=len(parts) - 1, part=)
                elif i > 0 and k < m - 1 and mat[i - 1][k] not in valid_signs:
                    parts.append(int(mat[i][j:k]))
                    if mat[i - 1][k] == '*':
                        add_part_in_gear_map(gears=gears, i=i - 1, j=k, part_i=len(parts) - 1)
                elif i < n - 1 and j > 0 and mat[i + 1][j - 1] not in valid_signs:
                    parts.append(int(mat[i][j:k]))
                    if mat[i + 1][j - 1] == '*':
                        add_part_in_gear_map(gears=gears, i=i + 1, j=j - 1, part_i=len(parts) - 1)
                elif i < n - 1 and k < m - 1 and mat[i + 1][k] not in valid_signs:
                    parts.append(int(mat[i][j:k]))
                    if mat[i + 1][k] == '*':
                        add_part_in_gear_map(gears=gears, i=i + 1, j=k, part_i=len(parts) - 1)
                elif j > 0 and mat[i][j - 1] not in valid_signs:
                    parts.append(int(mat[i][j:k]))
                    if mat[i][j - 1] == '*':
                        add_part_in_gear_map(gears=gears, i=i, j=j - 1, part_i=len(parts) - 1)
                elif k < m - 1 and mat[i][k] not in valid_signs:
                    parts.append(int(mat[i][j:k]))
                    if mat[i][k] == '*':
                        add_part_in_gear_map(gears=gears, i=i, j=k, part_i=len(parts) - 1)
                else:
                    if i > 0:
                        for c_i, c in enumerate(mat[i - 1][j:k]):
                            if c not in valid_signs:
                                parts.append(int(mat[i][j:k]))
                                if c == '*':
                                    add_part_in_gear_map(gears=gears, i=i - 1, j=j + c_i, part_i=len(parts) - 1)
                                break
                    elif i < n - 1:
                        for c_i, c in enumerate(mat[i + 1][j:k]):
                            if c not in valid_signs:
                                parts.append(int(mat[i][j:k]))
                                if c == '*':
                                    add_part_in_gear_map(gears=gears, i=i + 1, j=c_i, part_i=len(parts) - 1)
                                break
                j = k
            else:
                j += 1

    gear_ratio_total = 0
    for gear_x, gear_dict in gears.items():
        for gear_y, parts_i in gear_dict.items():
            if len(parts_i) == 2:
                print(
                    f'found gear from parts: {parts[parts_i[0]]} * {parts[parts_i[1]]} = {(parts[parts_i[0]] * parts[parts_i[1]])}')
                gear_ratio_total += (parts[parts_i[0]] * parts[parts_i[1]])

    return parts, gear_ratio_total


if __name__ == '__main__':
    lines = [line for line in read_input_lines(file_name='input.txt')]
    parts, gear_ratio_total = gear_ratios(lines)
    print(f'total parts: {sum(parts)}')
    print(f'total gear ratio: {gear_ratio_total}')
