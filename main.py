from pathlib import Path


def count_words(text):
    count = 1
    for letter in text:
        if letter not in result:
            result[letter] = count
        else:
            result[letter] = result.get(letter) + 1
    return result


def print_result(result):
    for item in result:
        print(f"'{item[0]}' appeard {item[1]} times.")


file_path = input("File path: ")
path = Path(file_path)

if path.exists():
    text = path.read_text().lower()
    result = {}

    if input("Would you like to exclude any stop word (y/n)? ").lower() == 'y':
        new_text = ""
        words_to_exclude = input(
            "What words do you want to exclude (seperate them by a space)? ")
        words = words_to_exclude.split(' ')
        words_to_exclude = text.split(' ')
        for word in words_to_exclude:
            if word not in words:
                new_text += word
        result = count_words(new_text)

    else:
        result = count_words(text)

    print_result(sorted(result.items()))


else:
    print(f"\nThe file doesn't exist.")
    print("Make sure the path or the file name is correct.")
    print(f"The path you provided is: '{path}'\n")
