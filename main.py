def read_file_content(filename):
    # [assignment] Add your code here 
    f = open('story.txt', 'r')
    filename = f.read()

    return filename
print(read_file_content('filename'))


def count_words():
    text = read_file_content('story.txt')
    # [assignment] Add your code here
    words_of_text = text.split()
    count = dict()
    for word in words_of_text :
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    return count
a = count_words()
print(a)
