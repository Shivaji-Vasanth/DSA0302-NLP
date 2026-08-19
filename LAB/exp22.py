import re

text = "John went to the park. He played football."

sentences = text.split(".")

nouns = []

print("Text:")
print(text)

print("\nReference Resolution:")

for sentence in sentences:
    words = sentence.strip().split()

    for word in words:
        word = word.strip(",.!?")

        if word.lower() in ["he", "she", "it"]:
            if nouns:
                print(word, "->", nouns[-1])

        elif re.match(r"^[A-Z][a-z]+$", word):
            nouns.append(word)