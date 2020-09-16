# fileIO

## Usage

```from fileIO import FileIO

def main():
    print("Iniciando...")
    file = FileIO("./test.txt")
    vec = file.read_as_vector()
    print(vec)

if __name__ == '__main__':
    main()```