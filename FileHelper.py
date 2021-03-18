class FileHelper:
    def __init__(self):
        pass

    @staticmethod
    def read_from_file(file_path: str):
        with open(file_path, 'r') as file:
            return file.read()

    @staticmethod
    def write_to_file(file_path: str, data: str, operator: str = 'w'):
        with open(file_path, operator) as file:
            file.write(data)
