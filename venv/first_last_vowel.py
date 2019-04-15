word = "aaaaa"
#allows user to input data
print(word)


list = ["a", "e", "i", "o", "u"]
list2 = ["A", "E", "I", "O", "U"]

if word[0] in (list):
    print("True the first letter is a vowel")
elif word[0] in (list2):
    print("True the first letter is a vowel")
elif word[-1] in (list):
    print("True the last letter is a vowel")
elif word[-1] in (list2):
    print("True the last letter is a vowel")
else:
    print("False")


