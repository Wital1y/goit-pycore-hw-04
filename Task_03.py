import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def print_directory_structure(directory, prefix=""):
    try:
        dir_path = Path(directory)

        if not dir_path.exists() or not dir_path.is_dir():
            print(Fore.RED + "Error: Path does not exist or is not a directory")
            return

        for path in sorted(dir_path.iterdir()):
            if path.is_dir():
                print(prefix + Fore.BLUE + f"📂 {path.name}/")
                print_directory_structure(path, prefix + "    ")
            else:
                print(prefix + Fore.GREEN + f"📜 {path.name}")

    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(Fore.RED + "Usage: python3 Task_03.py <directory-path>")
    else:
        directory = sys.argv[1]
        print_directory_structure(directory)
