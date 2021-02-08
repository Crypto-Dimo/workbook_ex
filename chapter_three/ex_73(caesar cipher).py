# caesar cipher encryption rule:
# c = (x + n) % 26, where:
# c = encoded character
# x = actual character
# n = positions to shift
# 26 = number of letters in the english alphabet
# for decription, the rule changes to c = (x - n) % 26


choice = input('Do you want to encrypt or decrypt a message? ')

if choice == 'encrypt':
    message = input('Enter your message: ')
    shift = int(input('Enter the shift amount: '))

    encryption = ''

    for c in message:
        if c.isupper():

            # find position in 0-25 (1-26)
            c_unicode = ord(c)
            c_index = ord(c) - ord('A')

            # perform the shift using the caesar cipher encryption rule:  c = (x + n) % 26
            new_index = (c_index + shift) % 26

            # convert to to new character
            new_unicode = new_index + ord('A')
            new_character = chr(new_unicode)

            # append to encrypted string (encryption = '')
            encryption = encryption + new_character

        elif c.islower():

            # find position in 0-25 (1-26)
            c_unicode = ord(c)
            c_index = ord(c) - ord('a')

            # perform the shift using the caesar cipher encryption rule:  c = (x + n) % 26
            new_index = (c_index + shift) % 26

            # convert to to new character
            new_unicode = new_index + ord('a')
            new_character = chr(new_unicode)

            # append to encrypted string (encryption = '')
            encryption = encryption + new_character

        else:
            encryption += c

elif choice == 'decrypt':
    message = input('Enter your message: ')
    shift = int(input('Enter the shift amount: '))

    encryption = ''

    for c in message:
        if c.isupper():

            # find position in 0-25 (1-26)
            c_unicode = ord(c)
            c_index = ord(c) - ord('A')

            # perform the shift using the caesar cipher encryption rule:  c = (x + n) % 26
            new_index = (c_index - shift) % 26

            # convert to to new character
            new_unicode = new_index + ord('A')
            new_character = chr(new_unicode)

            # append to encrypted string (encryption = '')
            encryption = encryption + new_character

        elif c.islower():

            # find position in 0-25 (1-26)
            c_unicode = ord(c)
            c_index = ord(c) - ord('a')

            # perform the shift using the caesar cipher encryption rule:  c = (x + n) % 26
            new_index = (c_index - shift) % 26

            # convert to to new character
            new_unicode = new_index + ord('a')
            new_character = chr(new_unicode)

            # append to encrypted string (encryption = '')
            encryption = encryption + new_character

        else:
            encryption += c

else:
    print('Invalid choice, enter a valid choice.')


print(f'The original message was: {message}')
print(f'The encrypted/decrypted message is: {encryption}')
