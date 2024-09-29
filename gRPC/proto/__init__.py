import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

# デバック用
if __name__ == "__main__":
    print(Path(__file__))
    print(Path(__file__).parent)
    print(sys.path)