def main():
    path_to_open = "books/frankenstein.txt"
    text = get_file_text(path_to_open)
    words = get_text_word_count(text)
    char_counts = get_char_counts(text)
    print_report_of_file(path_to_open)


def get_file_text(path_to_file):
    with open(path_to_file, "r") as f:
        file_contents = f.read()
    return file_contents


def get_text_word_count(text):
    words = text.split()
    return words


def get_char_counts(text):
    char_dict = {x: 0 for x in list(map(chr, range(97, 123)))}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
    return char_dict


def print_report_of_file(path_to_file):
    print(f"--- Begin report of file {path_to_file} ---")
    text = get_file_text(path_to_file)
    word_count = get_text_word_count(text)
    char_count = get_char_counts(text)
    char_count_list = [{"char": x, "num": y} for x, y in char_count.items()]
    def on_sort(dictionary):
        return dictionary["num"]
    char_count_list.sort(key=on_sort, reverse=True)
    print(f"{word_count} words found in the document")
    [print(f"The {x['char']} character was found {x['num']} times") for x in char_count_list]
    print(f"--- End report of file {path_to_file} ---")


if __name__ == "__main__":
    main()
