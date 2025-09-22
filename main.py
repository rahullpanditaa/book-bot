def main():
    print(get_book_text("books/frankenstein.txt"))

def get_book_text(filepath):
    # takes a file path as input
    # returns the contents of the file as a string
    with open(filepath, "r") as f:
        text = f.read()
    return text

if __name__ == "__main__":
    main()