while True:
    word = input()
    word_list = list(word)
    reverse_list = word_list[::-1]
    if word_list == reverse_list:
        print('yes')
    else:
        print('no')
