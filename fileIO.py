

class FileIO:
    def __init__(self, path, file_type=".txt"):
        self.path = path
        self.file_type = file_type
    
    def read_as_vector(self):
        vec = []
        with open(self.path) as inp:
            for line in inp:
                line = self.remove_new_line_caracters(line)
                vec.append(line)
        return vec
    
    def remove_new_line_caracters(self, str):
        return str.replace('\n', '')
