words = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,'
         ' dignissim vitae libero')
words_list = words.split()
print(words_list)
del_words = []


for word in words_list:
    if ',' in word:
        word = word.rstrip(',')
        word = word + 'ing,'
        del_words.append(word)
    elif '.' in word:
        word = word.rstrip('.')
        word = word + 'ing.'
        del_words.append(word)
    else:
        word = word + 'ing'
        del_words.append(word)


print(' '.join(del_words))
