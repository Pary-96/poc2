import json
import sys


def check_json(file_path):
    try:
        with open(file_path) as f:
            json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error in file {file_path}: {e}")
        return False
    return True


if __name__ == "__main__":
    # if len(sys.argv) < 2:
    #     print("Usage: python validate_json.py <file_path>")
    #     sys.exit(1)
    file_path = sys.argv[1]
    if check_json(file_path):
        print(f"File {file_path} is a valid JSON file.")
        sys.exit(0)
    else:
        print(f"File {file_path} is not a valid JSON file.")
        sys.exit(1)
