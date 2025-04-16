
path_to_file = "./books/frankenstein.txt"


def get_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def word_count(filepath):
    
    text = get_text(filepath)
    
    total_word_count =len(text.split())
    
    return total_word_count

def character_count(filepath):
    text = get_text(filepath)
    character_dict = {}
    
    for char in text.lower():
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    
    return character_dict

def sort_char_dict(filepath):
    unsorted_dict = character_count(filepath)
    alpha_dict = {}
      
    for char in unsorted_dict:
        count = unsorted_dict[char]
        if char.isalpha():
            alpha_dict[char] = count  

    sorted_list = sorted(alpha_dict.items(), key=lambda item: item[1], reverse=True)

    return sorted_list