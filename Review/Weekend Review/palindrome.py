
word = raw_input("Please enter a word to test.")
revWord = ""

##for index in range(len(word)-1,-1,-1):
for index in range(len(word)-1,-1,-1):
    revWord += word[index]

print(revWord)
print(word)

if revWord.lower() == word.lower():
   print("{0} is a Palindrome!").format(word)

else: print("{0} is not a Palindrome!").format(word)
