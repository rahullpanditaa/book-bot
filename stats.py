def number_of_words(book_text):
    return len(book_text.split())

def count_characters(text):
    characters = {}
    for c in text:
        if c.lower() not in characters:
            characters[c.lower()] = 1
        else:
            characters[c.lower()] += 1

    return characters

def list_of_dict(dict_of_chars):
    # take dict of characters
    # return sorted list of dictionaries
    # each dict --> {"char" : __, "num" : __}
    l = []
    for char in dict_of_chars:
        l.append({"char" : char, "num" : dict_of_chars[char]})
    l.sort(key=lambda chars : chars["num"], reverse=True)
    return l