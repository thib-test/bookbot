import sys
from stats import get_num_words, get_num_char, get_sorted_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_content = get_book_text(sys.argv[1])
    number_of_words = get_num_words(file_content)
    sorted_chars = get_sorted_chars(get_num_char(file_content))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")

    print("----------- Word Count ---------")
    print(f"Found {number_of_words} total words")

    print("--------- Character Count ------")
    for char in sorted_chars:
        if (char["char"].isalpha()):
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")


main()