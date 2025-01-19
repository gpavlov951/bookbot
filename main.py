def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    chars = {}
    lowered_string = text.lower()

    for c in lowered_string:
        if c not in chars:
            chars[c] = 0

        chars[c] += 1

    return chars

def convert_dict_to_list_dicts(dict):
    list_of_dicts = [{"char": k, "count": v} for k, v in dict.items()]
    return list_of_dicts

def sort_on(dict):
    return dict["count"]

def report(path, num_words, sorted_list_dicts):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document\n")

    for d in sorted_list_dicts:
        if d["char"].isalpha():
            print(f"The '{d["char"]}' character was found {d["count"]} times")

    print("--- End report ---")

def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = count_words(text)
    count_c = count_characters(text)

    list_dicts = convert_dict_to_list_dicts(count_c)
    list_dicts.sort(reverse=True, key=sort_on)

    report(path_to_file, num_words, list_dicts)


main()

