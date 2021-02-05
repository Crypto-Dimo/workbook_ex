
group8bits = input('Enter 8 bits: ')

while group8bits != '':
    if group8bits.count('0') + group8bits.count('1') != 8 or len(group8bits) != 8:
        print('Invalid group of bits.')
    else:
        ones = group8bits.count('1')
        if ones % 2 == 0:
            parity = '0'
        else:
            parity = '1'
        print(f'The parity bit should be {parity}.')

    group8bits = input('Enter the group of 8 bits (enter blank to end): ')

if group8bits == '':
    print('End')

