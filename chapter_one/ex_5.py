one_liter = int(input('How many 1L containers do you have?'))
one_liter_plus = int(input('How many 1L+ containers do you have?'))
refund_1L = 0.10 * one_liter
refund_1L_plus = 0.25 * one_liter_plus
print(refund_1L + refund_1L_plus, '$')

