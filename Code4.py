# Text Analyzer, I decided to analyze the vocaulary, but if needed, we can add more characters.

vocabulary = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",)

text = input("Please write the text you want to analyze: ")

print("The text that will be analyzed is: ")
print(text)

for v in vocabulary:
    count = 0
    for t in text:
        if v == t:
            count += 1
    if count != 0:
        print("For the letter", v, "there are: ", count)

