class Block:
    def __init__(self) -> None:
        self.type: int
        self.attr: dict
        self.data: list

def read(filename: str) -> str:
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def parse(text: str) -> None:
    pass

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='PAF parser')
    parser.add_argument('filename', type=str, help='the input file')
    args = parser.parse_args()
    parse(read(args.filename))
