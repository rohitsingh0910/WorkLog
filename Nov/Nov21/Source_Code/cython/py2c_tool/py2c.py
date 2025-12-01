# py2c.py
import sys
import os
from converter import convert_file_py

def main():
    if len(sys.argv) != 2:
        print("Usage: python py2c.py <python_file>")
        sys.exit(1)
    input_path = sys.argv[1]
    if not os.path.exists(input_path):
        print("Input file not found:", input_path)
        sys.exit(1)
    output_path = input_path.replace(".py", ".c")
    convert_file_py(input_path.encode('utf-8'), output_path.encode('utf-8'))
    print("Generated:", output_path)

if __name__ == "__main__":
    main()
