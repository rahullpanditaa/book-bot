from stats import number_of_words, count_characters, list_of_dict
import sys
def main():
    book_path = get_book_path()
    book_text = get_book_text(book_path)
    num_of_words = number_of_words(book_text)
    chars = count_characters(book_text)
    list_of_chars = list_of_dict(chars)
    report(book_path, number_of_words=num_of_words, chars=list_of_chars)

def get_book_text(filepath):
    # takes a file path as input
    # returns the contents of the file as a string
    with open(filepath, "r") as f:
        text = f.read()
    return text

def get_book_path():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]

def report(book_path, number_of_words=0, chars=[]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for character in chars:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")

if __name__ == "__main__":
    main()