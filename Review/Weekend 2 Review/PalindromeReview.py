word = raw_input("Please enter the word you would like to check.  ")

revWord = ""

##Still not 100% sure how this for loop works.
for index in range(len(word)-1,-1,-1):
    revWord += word[index]

print(revWord)

if revWord == word:
    print("You entered a palindrome!")

else:
    print("This is not a palindrome.")
