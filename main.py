def main():
    print(number_of_words(get_book_text("books/frankenstein.txt")))

def get_book_text(filepath):
    # takes a file path as input
    # returns the contents of the file as a string
    with open(filepath, "r") as f:
        text = f.read()
    return text

def number_of_words(book_text):
    return f"{len(book_text.split())} words found in the document"

if __name__ == "__main__":
    main()