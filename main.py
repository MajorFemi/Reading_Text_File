# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename, 'r') as filename:
        text = filename.read()
    
    return text


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    new_text = text.lower()
    file = new_text.replace('?',"").replace('.',"").replace(',',"")
    count = dict()
    words = file.split()
    
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    
    return count
