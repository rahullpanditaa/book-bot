from stats import number_of_words, count_characters

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_of_words = number_of_words(book_text)
    chars = count_characters(book_text)
    print(f"{num_of_words} words found in this document")
    print(chars)

def get_book_text(filepath):
    # takes a file path as input
    # returns the contents of the file as a string
    with open(filepath, "r") as f:
        text = f.read()
    return text


if __name__ == "__main__":
    main()