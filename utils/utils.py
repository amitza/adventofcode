from typing import List, Any


def read_input_lines(file_name: str = None) -> list[str]:
    if file_name is None:
        file_name = 'input.txt'
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            yield line


def read_input_matrix(file_name: str = None) -> List[List[Any]]:
    if file_name is None:
        file_name = 'input.txt'
    mat = [[]]
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            mat.append([])
            line = line.strip()
            mat[i] = list(line)
    return mat
