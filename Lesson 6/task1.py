# Make a program that has some sentence (a string) on input\
# and returns a dict containing all unique words as keys and the number of occurrences as values.

text_string = input("Введіть текст: ")

split_string = text_string.split()

word_list = dict()

for words in split_string:
    if word_list.get(words) == None:
        word_list[words] = 1
    else:
        word_list[words] += 1

print(word_list)
