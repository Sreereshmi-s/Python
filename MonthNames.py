# List of month names (index 0 is empty for easy mapping)
month_names = ["", "January", "February", "March", "April", "May", "June", 
               "July", "August", "September", "October", "November", "December"]

# Get user input
month_number = int(input("Enter the month: "))

# print the corresponding month name
if 1 <= month_number <= 12:
    print("Month " + str(month_number) +" is " + month_names[month_number])
else:
    print("Invalid month! Please enter a number between 1 and 12.")