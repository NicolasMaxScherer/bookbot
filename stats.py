def get_num_words(path):
    with open(path) as file:
        content = file.read()
        num = len(content.split())
        print(f"'Found {num} total words.")


def count_characters(path):
    with open(path) as file:
        content = file.read().lower()

    characters_count = {}

    for char in content:
        if char.isalpha():
            if char in characters_count:
                characters_count[char] += 1
            else:
                characters_count[char] = 1

    return characters_count


def sort_on(item):
    return item["num"]


def sort_characters(char_dict):

    chars_list = []

    for char, count in char_dict.items():
        if char.isalpha():  
            chars_list.append({"char": char, "num": count})
        else:
            continue

 
    chars_list.sort(key=sort_on, reverse=True)

    return chars_list