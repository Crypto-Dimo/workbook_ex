saving_account = float(input('How much do you have in your saving account? '))
interest_1st_year = saving_account * 4 / 100 + saving_account
interest_2nd_year = interest_1st_year * 4 / 100 + saving_account
interest_3rd_year = interest_2nd_year * 4 / 100 + saving_account
print('You will have', round(interest_1st_year, 2), 'in your saving account after 1 year')
print('You will have', round(interest_2nd_year, 2), 'in your saving account after 2 years')
print('You will have', round(interest_3rd_year, 2), 'in your saving account after 3 years')