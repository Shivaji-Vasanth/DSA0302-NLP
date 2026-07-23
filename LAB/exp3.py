from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "studies", "running", "happiness"]

print("Original Words:", words)

print("\nStemmed Words:")
for word in words:
    print(word, "->", ps.stem(word))