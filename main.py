def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        generate_report(file_contents)



def count_words(text):
    return len(text.split())

def count_characters(text):
    lowered_text = text.lower()
    char_counts = {}
    for char in lowered_text:
        if not char_counts.get(char):
            char_counts[char] = 1
        else:
            char_counts[char] = char_counts[char] + 1
    return char_counts

def convert_to_list(char_count_dict):
    char_count_list = []
    for item in char_count_dict:
        temp_dict = {"char": item, "count" : char_count_dict[item]}
        char_count_list.append(temp_dict)
    return char_count_list

def sort_on(dict):
    return dict["count"]

def generate_report(book):
    print("--- Begin report of books/frankenstein.txt ---")
    word_count = count_words(book)
    print(f"The book contains {word_count} words.")
    print("\n")
    character_count = count_characters(book)
    character_info = convert_to_list(character_count)
    character_info.sort(key=sort_on, reverse=True)
    for item in character_info:
        char_to_print = item["char"]
        count_to_print = item["count"]
        if char_to_print.isalpha():
            print(f"The '{char_to_print}' character was found '{count_to_print}' times.")
    print("--- End report ---")


main()
