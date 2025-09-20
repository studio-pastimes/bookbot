import sys
from stats import get_word_count, get_character_count, sort_character_count

if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

path = sys.argv[1]

def get_book_text(filepath):
    book_text = ""

    with open(filepath) as f:
        book_text = f.read()

    return book_text

def print_report(data):

    return

def main(path):


    # path = 'books/frankenstein.txt'
    book = get_book_text(path)
    word_count = get_word_count(book)
    # print(str(word_count) + " words found in the document")

    character_count = get_character_count(book)
    # print(character_count)

    sorted_character_count = sort_character_count(character_count)
    # print(sorted_character_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at " + path)
    print("----------- Word Count ----------")
    print("Found " + str(word_count) + " total words")
    print("--------- Character Count -------")
    for item in sorted_character_count:
        if item["char"].isalpha():
            print(item["char"] + ": " + str(item["count"]))
        else:
            continue


main(path)
