# with if statement

word = input('Enter the word: ')
if word == word[::-1]:
    print('This is a palindrome.')
else:
    print('This is not a palindrome.')


# or with for loop

x = input('Enter the word: ')

w = ""
for i in x:
    w = i + w  # very different from (w = w + i) which has a different result

if x == w:
    print('This is a palindrome.')
else:
    print('This is not a palindrome.')