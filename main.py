# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename) as the_file:
        txt_lines = the_file.read()
        txt_lines = " ".join(txt_lines.split())
        return txt_lines

def count_words():
    text = read_file_content("./story.txt")
    punctuation_mark = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for x in text:
        if x in punctuation_mark:
            text = text.replace(x, "")
    text = text.lower()
    text = text.split()
    text_dict = {}
    for word in text:
        if word not in text_dict:
            text_dict[word] = text.count(word)
    return text_dict

print(count_words())