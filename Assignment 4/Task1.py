try:
    with open("sample.txt") as f:
        for i, line in enumerate(f, 1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

