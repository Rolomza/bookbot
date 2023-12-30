def main():
    book_path = "books/frankestein.txt"
    book_text = get_book_text(book_path)
    word_count = get_words_count(book_text)
    char_data = get_chars(book_text)
    alphabet_data = filter_and_sort_alphabet_data(char_data)
    print_report(book_path, word_count, alphabet_data)

def get_book_text(path):
    with open(path) as file:
        return file.read()

def get_words_count(text):
    words = text.split()
    return len(words)

def get_chars(text):
    chars = {}
    for letter in text.lower():
        if letter in chars:
            chars[letter] += 1
        else:
            chars[letter] = 1
    return chars

def sort_on(d):
    return d["num"]

def filter_and_sort_alphabet_data(chars_dict):
    chars_keys = list(chars_dict.keys())
    alphabet_dict = {}

    for char in chars_keys:
        if char.isalpha():
            alphabet_dict[char] = chars_dict[char]

    sorted_alphabet_list = []

    for ch in alphabet_dict:
        sorted_alphabet_list.append({"char": ch, "num": alphabet_dict[ch]})

    sorted_alphabet_list.sort(reverse=True, key=sort_on)
    return sorted_alphabet_list

def print_report(book_path, word_count, alphabet_data):
    print(f"--- Report of {book_path} ---")
    print(f"{word_count} words found in the document.")
    print()
    for item in alphabet_data:
        print(f"The {item["char"]} letter was found {item["num"]} times")


main()