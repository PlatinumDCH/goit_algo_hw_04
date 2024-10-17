from pathlib import Path
from colorama import Fore, init
import sys


class DirectoryExplorer:
    def __init__(self, path: Path):
        self.path = path

    def color_file_name(self, file: Path) -> str:
        """change color name file"""
        if file.is_dir():
            return Fore.BLUE
        elif file.suffix == ".py":
            return Fore.YELLOW
        elif file.suffix == ".ipynb":
            return Fore.MAGENTA
        elif file.suffix in [".txt", ".md"]:
            return Fore.GREEN
        else:
            return Fore.RED

    def explore(self, indent: str = ""):
        if self.path.is_dir():
            print(f"{indent}{Fore.BLUE}{self.path.name}")

            for item in self.path.iterdir():
                DirectoryExplorer(item).explore(indent + "    ")
        else:
            color = self.color_file_name(self.path)
            print(f"{indent}{color}{self.path.name}")


if __name__ == "__main__":

    init(autoreset=True)

    if len(sys.argv) != 2:
        print("Not found path argument.")
        sys.exit(1)

    path = Path(sys.argv[1])

    if path.is_dir() and path.exists():
        explorer = DirectoryExplorer(path)
        explorer.explore()
    else:
        print("path not found or path not directory.")
