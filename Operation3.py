#Switches two sets of every character, given by two position parameters

def encryption_3(word,index_1,index_2): 
  # encryption
  array_with_indexes = [-1]
  char_1 = word[index_1] #f
  char_2 = word[index_2] #r
  for x in range(0,len(word)-1):
    if (word[x] == char_2):
      array_with_indexes.append(x)
  sqapped_word = word.replace(char_1,char_2)
  swapped_word_list = list(sqapped_word)
  for x in range(1,len(array_with_indexes)): #[-1,0]
    swapped_word_list[array_with_indexes[x]] = char_1
  return ''.join(swapped_word_list)

def decryption_3(word, index_1, index_2):
  array_with_indexes = [-1]
  char_1 = word[index_1] #f
  char_2 = word[index_2] #r
  for x in range(0,len(word)-1):
    if (word[x] == char_2):
      array_with_indexes.append(x)
  sqapped_word = word.replace(char_1,char_2)
  swapped_word_list = list(sqapped_word)
  for x in range(1,len(array_with_indexes)): #[-1,0]
    swapped_word_list[array_with_indexes[x]] = char_1
  return ''.join(swapped_word_list)
  