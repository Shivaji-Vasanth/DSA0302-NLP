words = ["govern", "government", "governance"]

for word in words:

    if word == "govern":
        root = "govern"
        suffix = "None"
        level = "Base Word"

    elif word.endswith("ment"):
        root = word[:-4]
        suffix = "-ment"
        level = "Level 1 Derivation"

    elif word.endswith("ance"):
        root = word[:-4]
        suffix = "-ance"
        level = "Level 1 Derivation"

    print("--------------------------------")
    print("Original Word :", word)
    print("Root Word     :", root)
    print("Suffix        :", suffix)
    print("Hierarchy     :", level)
    print("Normalized    :", root)