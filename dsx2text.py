from libdsx.model import Document
from pathlib import Path
import libdsx
import sys

class InvalidDocument(RuntimeError):
    pass

def read(name: Path) -> str:
    try:
        libdsx.validate_file(name)
    except libdsx.DSXError as error:
        raise InvalidDocument()
    else:
        document: Document = libdsx.load(name)
        return libdsx.render(document)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Too few arguments!")
        sys.exit(1)

    pathinput: Path = Path(sys.argv[1])
    if not pathinput.exists():
        print("Path doesn't exist!")
        sys.exit(1)

    try:
        buffer: str = read(pathinput)
    except InvalidDocument:
        print("Invalid document!")
        sys.exit(1)

    print(buffer, end="")