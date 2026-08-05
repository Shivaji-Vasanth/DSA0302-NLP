words = ["create", "creates", "creating"]

for word in words:

    suffix = "None"
    feature = ""

    if word == "create":
        root = word
        feature = "Base Form"

    elif word.endswith("s"):
        root = word[:-1]
        suffix = "-s"
        feature = "Third Person Singular"

    elif word.endswith("ing"):
        root = word[:-3]

        # creating -> create
        if root.endswith("t"):
            root += "e"

        suffix = "-ing"
        feature = "Present Participle"

    print("--------------------------------")
    print("Original :", word)
    print("Suffix   :", suffix)
    print("Feature  :", feature)
    print("Root     :", root)
    print("Normalized :", root)