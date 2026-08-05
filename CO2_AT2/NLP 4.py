words = ["activate", "activation", "reactivation"]

for word in words:

    prefix = "None"
    suffix = "None"
    root = ""

    if word == "activate":
        root = "activate"
        sequence = "Base Word"

    elif word == "activation":
        root = "activate"
        suffix = "-ion"
        sequence = "activate + ion"

    elif word == "reactivation":
        prefix = "re"
        root = "activate"
        suffix = "-ion"
        sequence = "re + activate + ion"

    print("------------------------------------")
    print("Original :", word)
    print("Prefix   :", prefix)
    print("Root     :", root)
    print("Suffix   :", suffix)
    print("Sequence :", sequence)
    print("Normalized :", root)