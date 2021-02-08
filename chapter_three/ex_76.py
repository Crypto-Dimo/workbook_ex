x = input('Enter the word or sentence: ')

w = ''

bad_char = [';', ':', ',', '.', '!', '?', ' ']

for b in bad_char:
    x = x.replace(b, '')

for i in x:
    w = i + w

if x == w:
    print('This is a palindrome.')
else:
    print('This is not a palindrome.')