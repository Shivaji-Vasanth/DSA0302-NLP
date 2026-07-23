import re

text = "John's email is john25@gmail.com. His phone number is 9876543210 and he is 21 years old."

email = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", text)
phone = re.findall(r"\b\d{10}\b", text)
number = re.findall(r"\d+", text)

print("Text:")
print(text)

print("\nEmails:", email)
print("Phone Numbers:", phone)
print("Numbers:", number)