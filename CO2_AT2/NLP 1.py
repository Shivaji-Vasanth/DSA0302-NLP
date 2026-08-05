# Morphological Processing for Search Engine Indexing

words = ["analyzing", "analysis", "analytical"]

for word in words:
    original = word

    if word.endswith("ing"):
        root = word[:-3]
        affix = "-ing"
        ttype = "Inflectional"

        # analyzing -> analyze
        if root.endswith("z"):
            root += "e"

    elif word.endswith("sis"):
        root = "analyze"
        affix = "-sis"
        ttype = "Derivational"

    elif word.endswith("ical"):
        root = "analyze"
        affix = "-ical"
        ttype = "Derivational"

    else:
        root = word
        affix = "None"
        ttype = "Root"

    print("----------------------------------------")
    print("Original Word :", original)
    print("Root Word     :", root)
    print("Affix         :", affix)
    print("Type          :", ttype)
    print("Normalized    :", root)