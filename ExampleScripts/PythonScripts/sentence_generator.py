import math 
import nltk
import random
nltk.download('brown')
from nltk.corpus import brown
word_list = brown.words()
sin_square = lambda a : math.sin(a) * a - a

def make_sentence(length):
  sentence = []
  count = 0
  start = ["The", "A", "As", "When", "They", "You", "Afterwards,", "However"]
  objects = ["are the", "is a", "became a", "changed to", "bought some", "needed to", "bought", "exist for", "made the", "said that", "knew how"]
  suffix = ["er", "ent", "om", "it", "la", "ir", "re", "oc", "ed", "ate", "en", "ize", "to", "ant", "unk", "ify", "ise", "in", "ing", "by", "tar", "it", "to", "and", "id"]
  first_word = random.randint(0,len(start)-1)
  sentence.append(start[first_word])
  second_word = random.randint(0,len(word_list)-1)
  sentence.append(word_list[second_word])
  third_word = random.randint(0,len(objects)-1)
  sentence.append(objects[third_word])
  while (count < length):
    for e in range(len(suffix)):
      i = random.randint(0,len(word_list)-1)
      if (suffix[e] in word_list[i] and len(word_list[i]) < 17):
        sentence.append(word_list[i])
        if (sentence[len(sentence)-1] == sentence[len(sentence)-2]):
          sentence.pop()
        count = count + 1
    bool_word = random.randint(1,4)
    if (random.randint(1,3) == 1):
      if (bool_word != 1):
        sentence.append(objects[random.randint(0,len(objects) - 1)])
        count = count + 1
        if (sentence[len(sentence)-1] == sentence[len(sentence)-2]):
          sentence.pop()
      else:
        sentence.append(start[random.randint(0,len(start) - 1)])
        count = count + 1
        if (sentence[len(sentence)-1] == sentence[len(sentence)-2]):
          sentence.pop()
    if (sentence[len(sentence)-1] in sentence[len(sentence)-2]):
      sentence.pop()
    if (sentence[len(sentence)-2] in sentence[len(sentence)-1]):
      sentence.pop()
  final_sentence = ''
  for i in range(len(sentence)):
    final_sentence = final_sentence + sentence[i] + " "
  final_sentence = final_sentence + "."
  return final_sentence

for i in range(300):
  length = random.randint(4,13)
  print(make_sentence(length))