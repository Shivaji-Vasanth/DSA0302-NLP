import nltk

text = "The smart boy reads a book."

words = nltk.word_tokenize(text)
tags = nltk.pos_tag(words)

grammar = "NP: {<DT>?<JJ>*<NN>}"

parser = nltk.RegexpParser(grammar)
tree = parser.parse(tags)

print("Sentence:")
print(text)

print("\nNoun Phrases:")

for subtree in tree.subtrees():
    if subtree.label() == "NP":
        phrase = " ".join(word for word, tag in subtree.leaves())
        print(phrase, "-> Person or Object")