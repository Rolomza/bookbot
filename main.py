def main():
    book_path = "books/frankestein.txt"
    book_text = get_book_text(book_path)
    words = get_words_count(book_text)
    print(f"Number of words: {len(words)}")
    letters_count = get_chars(book_text)
    print(f"Letters: {letters_count}")

def get_book_text(path):
    with open(path) as file:
        return file.read()

def get_words_count(text):
    return text.split()

def get_chars(text):
    chars = {}
    for letter in text.lower():
        if letter in chars:
            chars[letter] += 1
        else:
            chars[letter] = 1
    return chars  

main()