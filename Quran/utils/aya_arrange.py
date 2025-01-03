import re
from chapters import chapters as surahs

def replace_and_pad(text):
    # Match patterns like "1|23|"
    pattern = r'(\d+)\|(\d+)\|'
    
    # Function to pad the matched groups
    def pad_match(match):
        first = match.group(1).zfill(3)  # Pad the first number to 3 digits
        second = match.group(2).zfill(3)  # Pad the second number to 3 digits
        return first + second
    
    # Use re.sub to replace the matched patterns with padded versions
    result = re.sub(pattern, pad_match, text)
    return result

with open('quran-simple.txt', 'r', encoding='UTF-8') as file:
    with open('quran-text.txt', 'a', encoding='UTF-8') as writefile:
        for line in file.readlines():
            writefile.write(replace_and_pad(line))
'''
# Example usage
text = "1|23|"
padded_text = replace_and_pad(text)
print(padded_text)  # Output: "001023"
'''