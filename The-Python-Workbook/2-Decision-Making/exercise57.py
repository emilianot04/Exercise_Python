""" 
A particular cell phone plan includes 50 minutes of air time and 50 text messages for $15.00 a month. Each additional minute of air time costs $0.25, while additional text messages cost $0.15 each. All cell phone bills include an additional charge of $0.44 to support 911 call centers, and the entire bill (including the 911 charge) is subject to 5 percent sales tax.
Write a program that reads the number of minutes and text messages used in a month from the user. Display the base charge, additional minutes charge (if any),additional text message charge (if any), the 911 fee, tax and total bill amount. Only display the additional minute and text message charges if the user incurred costs in these categories. Ensure that all of the charges are displayed using 2 decimal places.
"""

minutes = int(input('Insert minutes: '))
messages = int(input('Insert messages: '))
month = 15
plan_minutes = 50
plan_message = 50
add_minutes = 0.25
add_messages = 0.15
call_center = 0.44
sales_tax = 0.05

if(minutes > 50):
    price_minutes = (minutes - plan_minutes) * add_minutes
else:
    price_minutes = 0
if(messages > 50):
    price_messages = (messages - plan_message) * add_messages
else:
    price_messages = 0

total = month + price_minutes + price_messages + call_center
total_tax = total * sales_tax
total_final = total_tax + total

print('Cost total : ' + '%.2f ' % float(total_final))
