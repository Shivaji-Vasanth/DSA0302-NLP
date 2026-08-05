words = ["disagree", "agreement", "agreeable"]

for word in words:

    prefix = "None"
    suffix = "None"
    root = word
    category = ""
    meaning = ""

    if word.startswith("dis"):
        prefix = "dis"
        root = word[3:]
        category = "Prefix Derivation"
        meaning = "Negative"

    elif word.endswith("ment"):
        suffix = "ment"
        root = word[:-4]
        category = "Suffix Derivation"
        meaning = "Noun Formation"

    elif word.endswith("able"):
        suffix = "able"
        root = word[:-4]
        category = "Suffix Derivation"
        meaning = "Adjective Formation"

    print("--------------------------------")
    print("Original :", word)
    print("Prefix   :", prefix)
    print("Root     :", root)
    print("Suffix   :", suffix)
    print("Category :", category)
    print("Meaning  :", meaning)
    print("Normalized :", root)