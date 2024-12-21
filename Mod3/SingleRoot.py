def  single_root_words(root_word, *other_words):
    same_words = []
    Root_left_or_right = True
    for i in range(len(other_words)):
        if len(root_word) <= len(other_words[i]):
            for j in range(len(other_words[i])):
                if root_word[0].lower() == other_words[i][j].lower():
                    checker = True
                    for letter in range(len(root_word)):
                        if root_word[letter].lower() == other_words[i][j].lower():
                            j += 1
                        else:
                            checker = False
                            break
                    if checker == True:
                        same_words.append(other_words[i])
        else:
            Root_left_or_right = False
            for j in range(len(root_word)):
                if root_word[j].lower() == other_words[i][0].lower():
                    checker = True
                    for letter in range(len(other_words[i])):
                        if other_words[i][letter].lower() == root_word[j].lower():
                            j += 1
                        else:
                            checker = False
                            break
                    if checker == True:
                        same_words.append(other_words[i])
    if not Root_left_or_right:
        print(f'Слово "{root_word}" содержат корни:')
    else:
        print(f'Корень "{root_word}" содержат слова:')
    return same_words
print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))