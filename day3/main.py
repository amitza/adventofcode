from utils.utils import read_input_lines


def is_part_already_starred(all_stars: dict[int, dict[int, int]], i: int, j: int, part: int) -> bool:
    if i not in all_stars.keys():
        all_stars[i] = {j: part}
        return False
    else:
        if j not in all_stars[i]:
            all_stars[i].append(j)
            return False
        else:
            return True


def gear_ratios(mat: list[str]) -> list[int]:
    valid_signs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    all_stars: dict[int, dict[int, int]] = {}
    parts = []
    n = len(mat)
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
                        is_part_already_starred(all_stars=all_stars, i=i-1, j=j-1)
                elif i > 0 and k < m - 1 and mat[i - 1][k] not in valid_signs:
                    parts.append(int(mat[i][j:k]))
                    if mat[i - 1][k] == '*':
                        is_part_already_starred(all_stars=all_stars, i=i-1, j=k)
                elif i < n - 1 and j > 0 and mat[i + 1][j - 1] not in valid_signs:
                    parts.append(int(mat[i][j:k]))
                    if mat[i + 1][j - 1] == '*':
                        is_part_already_starred(all_stars=all_stars, i=i+1, j=j-1)
                elif i < n - 1 and k < m - 1 and mat[i + 1][k] not in valid_signs:
                    parts.append(int(mat[i][j:k]))
                    if mat[i + 1][k] == '*':
                        is_part_already_starred(all_stars=all_stars, i=i+1, j=k)
                elif j > 0 and mat[i][j - 1] not in valid_signs:
                    parts.append(int(mat[i][j:k]))
                    if mat[i][j - 1] == '*':
                        is_part_already_starred(all_stars=all_stars, i=i, j=j-1)
                elif k < m - 1 and mat[i][k] not in valid_signs:
                    parts.append(int(mat[i][j:k]))
                    if mat[i][k] == '*':
                        is_part_already_starred(all_stars=all_stars, i=i, j=k)
                else:
                    if i > 0:
                        for c_i, c in enumerate(mat[i - 1][j:k]):
                            if c not in valid_signs:
                                parts.append(int(mat[i][j:k]))
                                if c == '*':
                                    is_part_already_starred(all_stars=all_stars, i=i - 1, j=j + c_i)
                                break
                    elif i < n - 1:
                        for c_i, c in enumerate(mat[i + 1][j:k]):
                            if c not in valid_signs:
                                parts.append(int(mat[i][j:k]))
                                if c == '*':
                                    is_part_already_starred(all_stars=all_stars, i=i + 1, j=c_i)
                                break
                j = k
            else:
                j += 1
    return parts


if __name__ == '__main__':
    lines = [line for line in read_input_lines(file_name='input2.txt')]
    print(f'total gear: {sum(gear_ratios(lines))}')
