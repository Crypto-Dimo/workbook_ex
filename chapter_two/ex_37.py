letter = input("Enter a vowel or a consonant: ")
letter = letter.lower()

if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print("The letter you entered is a vowel.")
elif letter == 'y':
    print("The letter 'Y' is sometimes a vowel and sometimes a consonant.")
else:
    print("the letter you entered is a consonant.")