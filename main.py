def get_word_count(content: str) -> int:
    return len(content.split())


def get_char_freq(content: str) -> dict:
    char_dict = {}

    for c in content.lower():
        if c.isalpha():
            try:
                char_dict[c] += 1
            except Exception:

                char_dict[c] = 1

    return dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))


def main():
    book = "books/frankenstein.txt"

    with open(book) as f:
        content = f.read()

    print(f"--- Begin report of {book} ---")
    print(f"{get_word_count(content)} words found in document")
    print("")
    for k, v in get_char_freq(content).items():
        print(f"The '{k}' character found {v} times")
    print("--- End report ---")


if __name__ == '__main__':
    main()
