import csv

profit=[]
month=[]

with open('budget_data.csv','r') as file:
        reader=csv.reader(file)
        next(reader)#skip heading
        for row in reader:
            month.append(row[0])
            profit.append(int(row[1]))

total_months=len(month)
total_profits=sum(profit)

changes=[]
increase=0
decrease=0

for i in range(1,len(profit)):
        change=profit[i] - profit[i-1]
        changes.append(change)
        if change > increase:
            increase=change
            increase_month=month[i]
        if change < decrease:
            decrease=change
            decrease_month=month[i]            

average_change=sum(changes) / len(changes)

print('Financial Analysis')
print('----------------------------')
print('Total Months: %d' % (total_months))
print('Total: %d' % (total_profits))
print('Average  Change: $%.2f' % (average_change))
print('Greatest Increase in Profits: %s ($%d)' % (increase_month,increase))
print('Greatest Decrease in Profits: %s ($%d)' % (decrease_month,decrease))

with open("bank_output.txt","w") as txt:
    txt.write('Financial Analysis\n')
    txt.write('----------------------------\n')
    txt.write('Total Months: %d\n' % (total_months))
    txt.write('Total: %d\n' % (total_profits))
    txt.write('Average  Change: $%8.2f\n' % (average_change))
    txt.write('Greatest Increase in Profits: %s ($%d)\n' % (increase_month,increase))
    txt.write('Greatest Decrease in Profits: %s ($%d)\n' % (decrease_month,decrease))








    
    















    




