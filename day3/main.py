from utils.utils import read_input_lines


def gear_ratios(mat: list[str]) -> list[int]:
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
                print(f'{i}: {j} -> {k} [{mat[i][j:k]}]')
                if i > 0 and j > 0 and mat[i - 1][j - 1] != '.':
                    parts.append(int(mat[i][j:k]))
                    break
                elif i > 0 and j < m - 1 and mat[i - 1][j + 1] != '.':
                    parts.append(int(mat[i][j:k]))
                    break
                elif i < n - 1 and j > 0 and mat[i + 1][j - 1] != '.':
                    parts.append(int(mat[i][j:k]))
                    break
                elif i < n - 1 and j < m - 1 and mat[i + 1][j + 1] != '.':
                    parts.append(int(mat[i][j:k]))
                    break
                for sub_i in range(j, k):
                    if i > 0 and mat[i - 1][sub_i] != '.':
                        parts.append(int(mat[i][j:k]))
                        break
                    if i < n - 1 and mat[i + 1][sub_i] != '.':
                        parts.append(int(mat[i][j:k]))
                        break
                j = k
            else:
                j += 1
    return parts


if __name__ == '__main__':
    total = 0
    lines = [line for line in read_input_lines()]
    for t in gear_ratios(lines):
        total += t
    print(f'total gear: {total}')
