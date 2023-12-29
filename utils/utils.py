def read_input_lines(file_name: str = None) -> list[str]:
    if file_name is None:
        file_name = 'input.txt'
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            yield line
