def get_num_words(content):
    return len(content.split())

def get_num_char(content):
    character_count = {}

    for char in (content):
        char_lowercase = char.lower()
        if char_lowercase in character_count:
            character_count[char_lowercase] += 1
        else:
            character_count[char_lowercase] = 1
    
    return character_count

def get_count(entry):
    return entry["num"]

def get_sorted_chars(characters_dict):
    sorted_list = []

    for key in characters_dict:
        entry = {}
        entry["char"] = key
        entry["num"] = characters_dict[key]
        sorted_list.append(entry)
    
    sorted_list.sort(key=get_count, reverse=True)
    return sorted_list




# Add a new function to your stats.py file that takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
# Each dictionary should have two key-value pairs: one for the character itself and one for that character's count (e.g. {"char": "b", "num": 4868}).
# Sort the list from greatest to least by the count.
# The .sort() method will be helpful here (see the hint).