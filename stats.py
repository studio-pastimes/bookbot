def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    characters = {}
    for letter in text:
        letter2 = letter.lower()
        # characters[letter2] += 1.
        if letter2 in characters:
           characters[letter2] += 1
        else:
           characters[letter2] = 1

    return characters

def sort_on(items):
    return items["count"]

def sort_character_count(list):
    new_list = []
    for item in list:
        # print(item)
        dict = {
            "char": item,
            "count": list[item]
        }
        # print(dict)
        # print(new_list)
        new_list.append(dict)
    # print(new_list.sort(reverse=True, key=sort_on))
    new_list.sort(reverse=True, key=sort_on)
    return new_list
