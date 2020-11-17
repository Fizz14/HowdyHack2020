#pushes the letters in a string by a certain number of characters

def encryption_2(word, translation_value):
    # translate
    translation_value = int(translation_value)
    return word[-translation_value:] + word[:-translation_value]

def decryption_2(word, translation_value):
    translation_value = int(translation_value)
    translation_value = -translation_value
    return word[-translation_value:] + word[:-translation_value]