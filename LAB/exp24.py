dialog = [
    "Hello",
    "What is your name?",
    "My name is Rahul.",
    "Thank you",
    "Goodbye"
]

print("Dialog Act Recognition:\n")

for sentence in dialog:
    text = sentence.lower()

    if "hello" in text or "hi" in text:
        act = "Greeting"
    elif "?" in sentence:
        act = "Question"
    elif "thank" in text:
        act = "Thanking"
    elif "goodbye" in text or "bye" in text:
        act = "Closing"
    else:
        act = "Statement"

    print(sentence, "->", act)