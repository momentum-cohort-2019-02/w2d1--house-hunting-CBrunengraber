# inputs from the user
print("Want to know how many months will you have to save money to get a down payment for a home?")
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
percentage_down = input("Enter the percent of your home's cost to save as a down payment [0.25]: ")
rate = input("Enter the expected annual rate of return [0.04]: ")

# values to be calculated

if rate == '':
    rate = .04
else:
    rate = float(rate)
if percentage_down == '':
    percentage_down = .25
else:
    percentage_down = float(percentage_down)

portion_down_payment = total_cost * percentage_down

# current_savings must be set to zero, because it starts gaining money after month 1.

current_savings = 0
monthly_salary = annual_salary / 12

# months starts at zero, and will count up from there until reaching the monetary amount needed in the rest of the program. 

months = 0
monthly_saving = monthly_salary * portion_saved

#saving up for down payment

while current_savings < portion_down_payment:
    investments = current_savings*rate/12
    current_savings = monthly_saving + investments + current_savings
    months += 1

print("Number of months: " + str(months))