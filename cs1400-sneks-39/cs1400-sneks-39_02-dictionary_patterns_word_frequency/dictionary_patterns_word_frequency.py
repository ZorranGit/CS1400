from cisc108 import assert_equal
def count_words(words):
    word_counts={}
    words=words.split(",")
    for word in words:
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1
    return word_counts



assert_equal(count_words("Potato,Dream,Couch,Potato,Couch,Potato,Dream,Couch"),{'Potato': 3, 'Dream': 2, 'Couch': 3})
assert_equal(count_words("Potato,Dream,Couch,Potato,Couch,Potato,Dream,Couch,Potato"),{'Potato': 4, 'Dream': 2, 'Couch': 3})
