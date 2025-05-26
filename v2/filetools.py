class FileTools:
    def __init__(self):
        pass
    def find(string):
        try:
            with open("io/input.txt", "rt") as file:
                for line in file:
                    if string in line:
                        return line.strip()
            return None
        except FileNotFoundError:
            return None
    def get_line(line_number):
        try:
            with open("io/input.txt", 'r') as file:
                for i, line in enumerate(file):
                    if i + 1 == line_number:
                        return line.strip()
                return None
        except FileNotFoundError:
            return None