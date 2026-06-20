def popular_words(text, words):

    t = text.lower().split()
    r = {}
    for word in words:
        r[word] = t.count(word)
    return r

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print("OK")
