def read_file_content(filename):
    # [assignment] Add your code here 
    f = open(filename)
    file_content = f.read()

    return filename


def count_words():
    text = read_file_content('./story.txt')
    # [assignment] Add your code here
    text = text.translate(str.maketrans("", "", string.punctuation))
    count = {}
    words_of_text = text.split()
    
    for word in words_of_text :
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    return count

print(count_words())
