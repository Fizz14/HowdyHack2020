#Cycles characters a certain amount within a certain range


def checkBetweenBounds(original,translation,base):
    temp = base
    x = original + translation
    while(x > 126):
      x = x - 93
      temp = x

    while(x < 32):
      x = x + 93
      temp = x

    return temp


def encryption_1(word,translation_val, para_3 = -1):
    translation_val = int(translation_val)
    op_1_string_final = ""
    if (para_3 == -1 or para_3 > len(word)):
        for character in range(0,len(word)):
            ascii_value = ord(word[character]) + translation_val
            op_1_string_final += chr(checkBetweenBounds(ord(word[character]),translation_val,ascii_value))
    else:
        for character in range(0,para_3+1):
            ascii_value = ord(word[character]) + translation_val
            op_1_string_final += chr(checkBetweenBounds(ord(word[character]),translation_val,ascii_value))
   
        op_1_string_final += word[para_3+1:]
    return op_1_string_final



def decryption_1(word, translation_val, para_3 = -1):
    translation_val = int(translation_val)
    translation_val = -translation_val
    op_1_string_final = ""
    if (para_3 == -1 or para_3 > len(word)):
        for character in range(0,len(word)):
            ascii_value = ord(word[character]) + translation_val
            op_1_string_final += chr(checkBetweenBounds(ord(word[character]),translation_val,ascii_value))
    else:
        for character in range(0,para_3+1):
            ascii_value = ord(word[character]) + translation_val
            op_1_string_final += chr(checkBetweenBounds(ord(word[character]),translation_val,ascii_value))
    
        op_1_string_final += word[para_3+1:]

    return op_1_string_final