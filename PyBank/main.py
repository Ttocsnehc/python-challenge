import os
import csv

budget_csv = os.path.join("Resources","budget_data.csv")

months = []
profit_losses = []
total_change = []
prev_profit = 0

print("Financial Analysis")
print("----------------------------")

with open(budget_csv, 'r') as budget_file:
    next(budget_file)
    csvreader= csv.reader(budget_file, delimiter=",")
    
    for row in csvreader:
        months.append(row[0])
        profit_losses.append(row[1])
        current_total = int(row[1])
        
        current_profit = current_total
        change_profit = current_profit - prev_profit
        total_change.append(change_profit)
        prev_profit = current_profit

    int_total = [eval(i) for i in profit_losses]

    total_months = len(months)
    print(f"Total Months: {total_months}")

    total_money = sum(int_total)
    print(f"Total: ${total_money}")

    total_change = total_change[1:]

    average_change = sum(total_change)/len(total_change) 
    rounded_avg = round(average_change, 2)
    print(f"Average Change: ${rounded_avg}")

  
    greatest = max(total_change)
    print(f"Greatest Increase in Profits: {months[total_change.index(max(total_change))+1]} (${greatest})")

    lowest = min(total_change)
    print(f"Greatest Decrease in Profits: {months[total_change.index(min(total_change))+1]} (${lowest})")


txt = open("results.txt", "w")
txt.write("Financial Analysis" + "\n")
txt.write("----------------------------" + "\n")
txt.write(f"Total Months: {total_months}" + "\n")
txt.write(f"Total: ${total_money}" + "\n")
txt.write(f"Average Change: ${rounded_avg}" + "\n")
txt.write(f"Greatest Increase in Profits: {months[total_change.index(max(total_change))+1]} (${greatest})" + "\n")
txt.write(f"Greatest Decrease in Profits: {months[total_change.index(min(total_change))+1]} (${lowest})" + "\n")







        








    
    
    
    
    
    
    
    


 











