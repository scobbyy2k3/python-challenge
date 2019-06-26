import os
import csv

#path for file
filepath = os.path.join("C:\\Users\\HADEORLAH\\Desktop\\python-challenge\\pyBank\\Resources\\budget_data.csv")


month_count = 0
total_revenue = 0
currentmonth_revenue = 0
previous_revenue = 0
revenue_change = 0
revenue_changes = []
months = []

# open csv file
with open(filepath,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    # gather monthly changes in revenue
    for row in csvreader:

# number of months in dataset
        month_count = month_count + 1

#revenue change by month
        months.append(row[0])
        currentmonth_revenue = int(row[1])
        total_revenue = total_revenue + currentmonth_revenue

        if month_count > 1:
            revenue_change = currentmonth_revenue - previous_revenue
            revenue_changes.append(revenue_change)


        previous_revenue = currentmonth_revenue

#  month to month calcualtion of revenue change
sum_rev_changes = sum(revenue_changes)

average_change = sum_rev_changes / (month_count - 1)

max_change = max(revenue_changes)

min_change = min(revenue_changes)

max_month_index = revenue_changes.index(max_change)

min_month_index = revenue_changes.index(min_change)

max_month = months[max_month_index]

min_month = months[min_month_index]


# print summary to user
print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {month_count}")
print(f"Total Revenue: ${total_revenue}")
print(f"Average Revenue Change: ${average_change}")
print(f"Greatest Increase in Revenue: {max_month} (${max_change}) ")
print(f"Greatest Decrease in Revenue: {min_month} (${min_change}) ")

 # Name white file
output_file = filepath [0:-4]

write_budget_dataCSV = f"{output_file}_pybank_results.txt"

       # Open write file
text = open(write_budget_dataCSV, mode = 'w')
text.write("Financial Analysis" + "\n")
text.write("----------------------------------------" + "\n")
text.write(f"Total Months: {month_count}" + "\n")
text.write(f"Total Revenue: ${total_revenue}" + "\n")
text.write(f"Average Revenue Change: ${average_change}" + "\n")
text.write(f"Greatest Increase in Revenue: {max_month} (${max_change})" + "\n")
text.write(f"Greatest Decrease in Revenue: {min_month} (${min_change})" + "\n") 