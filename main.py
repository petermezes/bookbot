book_path = "books/frankenstein.txt"

def get_char_counts(text: str) -> dict:
    temp_chars = {}
    for char in text:
        if not char.isalpha():
            continue
        if char in temp_chars:
            temp_chars[char] += 1
        else: 
            temp_chars[char] = 1
    return temp_chars
    
def zip_dict_into_list(d: dict) -> list:
    final_list = []
    for key, value in d.items():
        final_list.append({key: value })
    return final_list

def report_msg(body_message, report_name, word_count):
    header = f"--- Begin report of {report_name} ---\n"
    sub_header = f"{word_count} words found in the document\n\n"
    footer = "--- End report ---"
    
    body = ""
    sorted_list = sorted(body_message, key=lambda x: list(x.values())[0], reverse=True)
    for item in sorted_list:
        key, value = item.popitem()
        body += f"The '{key}' character was found {value} times\n"
    
    return header + sub_header + body + footer
    
            
def main():
    letters_count = {}
    word_count = 0
    with open(book_path) as f:
        file_contents = f.read().lower()
        word_count = len(file_contents.split())
        letters_count = get_char_counts(file_contents)
 
    list_of_chars = zip_dict_into_list(letters_count) 
    print(report_msg(list_of_chars, book_path, word_count))

main()