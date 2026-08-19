import re

text = "Python is a programming language. Python is easy to learn. Programming languages are useful."

sentences = text.split(".")

sentences = [s.strip().lower() for s in sentences if s.strip()]

scores = []

for i in range(len(sentences) - 1):
    words1 = set(re.findall(r"\b\w+\b", sentences[i]))
    words2 = set(re.findall(r"\b\w+\b", sentences[i + 1]))

    common = words1.intersection(words2)

    score = len(common) / len(words1)
    scores.append(score)

average = sum(scores) / len(scores)

print("Text:")
print(text)

print("\nCoherence Score:", round(average, 2))

if average >= 0.2:
    print("Text is Coherent")
else:
    print("Text is Less Coherent")