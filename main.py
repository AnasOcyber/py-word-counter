from pathlib import Path

file_path = input("Paste the path to the text file: ")
path = Path(file_path)

text = path.read_text().lower()

count = 1

result = {}

for letter in text:
    if letter not in result:
        result[letter] = count
    else:
        result[letter] = result.get(letter) + 1

for item in result:
    print(item, result[item])
