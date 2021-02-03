# 50 minutes and 50 sms free for $15.00
# additional minutes $0.25 each and $0.15 for each extra sms
# additional monthly charge $0.44 for 911 call centers
# 5% monthly sales tax

minutes = int(input("How many minutes did you use this month? "))
sms = int(input("How many sms did you use this month? "))

monthly_plan = 15.00
fee_911 = 0.44

minutes_charge = float()
sms_charge = float()

if minutes > 50:
    minutes_charge = (minutes - 50) * 0.25
if sms > 50:
    sms_charge = (sms - 50) * 0.15



total = monthly_plan + minutes_charge + sms_charge + fee_911
sales_tax = total * 5 / 100
monthly_total = total + sales_tax


print("\nYour plan includes 50 minutes and 50 sms for free at $15.00 per month.\n")
print(f"You consumed {minutes} minutes and {sms} sms this month.\n")

if minutes <= 50 and sms <= 50:
    print(f"You haven't used extra minutes or sms this month and your monthly total is: ${round(monthly_total, 2)}.\n")
    print(f"The monthly bill is divided as follows:\n\nMonthly plan: ${monthly_plan}.\n\n911 charge: ${fee_911}.\n\nSales tax: ${round(sales_tax, 2)}.\n\n")
elif sms > 50 and minutes <= 50:
    print(f"You have used extra sms this month and your monthly total is: ${round(monthly_total, 2)}.\n")
    print(f"The monthly bill is divided as follows:\n\nMonthly plan: ${monthly_plan}.\n\n911 charge: ${fee_911}.\n\nSales tax: ${round(sales_tax, 2)}.\n\nExtra sms charge: ${sms_charge}.\n\n")
elif minutes > 50 and sms <= 50:
    print(f"You have used extra minutes this month and your monthly total is: ${round(monthly_total, 2)}.\n")
    print(f"The monthly bill is divided as follows:\n\nMonthly plan: ${monthly_plan}.\n\n911 charge: ${fee_911}.\n\nSales tax: ${round(sales_tax, 2)}.\n\nExtra minutes charge: ${minutes_charge}.\n\n")
elif minutes > 50 and sms > 50:
    print(f"You have used extra minutes and extra sms this month and your monthly total is: ${round(monthly_total, 2)}.\n")
    print(f"The monthly bill is divided as follows:\n\nMonthly plan: ${monthly_plan}.\n\n911 charge: ${fee_911}.\n\nSales tax: ${round(sales_tax, 2)}.\n\nExtra minutes charge: ${minutes_charge}.\n\nExtra sms charge: ${sms_charge}.\n\n")
