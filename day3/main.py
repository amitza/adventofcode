from utils.utils import read_input_lines


def gear_ratios(mat: list[str]) -> list[int]:
    valid_signs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
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
                elif i > 0 and k < m - 1 and mat[i - 1][k] not in valid_signs:
                    parts.append(int(mat[i][j:k]))
                elif i < n - 1 and j > 0 and mat[i + 1][j - 1] not in valid_signs:
                    parts.append(int(mat[i][j:k]))
                elif i < n - 1 and k < m - 1 and mat[i + 1][k] not in valid_signs:
                    parts.append(int(mat[i][j:k]))
                elif j > 0 and mat[i][j-1] not in valid_signs:
                    parts.append(int(mat[i][j:k]))
                elif k < m - 1 and mat[i][k] not in valid_signs:
                    parts.append(int(mat[i][j:k]))
                else:
                    if i > 0 and not all(c in valid_signs for c in mat[i - 1][j:k]):
                        parts.append(int(mat[i][j:k]))
                    elif i < n - 1 and not all(c in valid_signs for c in mat[i + 1][j:k]):
                        parts.append(int(mat[i][j:k]))
                j = k
            else:
                j += 1
    return parts


if __name__ == '__main__':
    lines = [line for line in read_input_lines(file_name='input.txt')]
    print(f'total gear: {sum(gear_ratios(lines))}')
