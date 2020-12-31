from imports import *

with open ("insults.txt", 'r', encoding='utf-8') as insults:
    all_insults = insults.read()
    insult_split = all_insults.split('\n')

#print(quote_split[22])
print (insult_split[22])