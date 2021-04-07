def find_most_common_words(txt, n=10):
    word_dct = {}
    words = txt.lower().split(' ')
    for word in words:
        if word.endswith('.') or word.endswith('?') or word.endswith('!'):
            word = word[0:-1]
        if word in word_dct:
            word_dct[word] = word_dct[word] + 1
        else:
            word_dct[word] = 1
    sorted_list = sorted(
        word_dct.items(), key=lambda x: x[1], reverse=True)[0:n]
    return sorted_list
    # return { k:v for k,v in sorted_list }

