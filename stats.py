def number_of_words(book_text):
    return f"{len(book_text.split())} words found in the document"

def count_characters(text):
    characters = {}
    for c in text:
        if c.lower() not in characters:
            characters[c.lower()] = 1
        else:
            characters[c.lower()] += 1

    return characters
