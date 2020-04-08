# importing matplotlib.myplot libary as storing it as plt 
import matplotlib.pyplot as plt

#### Program to analyze exprenses to produce visualization

## expenses over a 6 month period Jan-June
carInsurance = (196, 196, 196, 196, 196, 196)
phoneBill = (67, 77, 99, 85, 72, 100)
groceries = (215,189,250,205,239,199)
gymMembership = (67.17, 67.17, 67.17, 67.17, 67.17, 67.17)
misc = (102,97,45,150,200,175)
amazon = (44,155,69,78,99,56)

# sums for each category stored in a tuple
cost = [sum(carInsurance), sum(phoneBill), sum(groceries), sum(gymMembership), sum(misc), sum(amazon)]

# labels to match the indices of the tuple cost
labels = 'Car Insurance', 'Phone Bill', 'Groceries', 'Gym Membership', 'Amazon', 'Misc.'

## pie Chart

# creating pie chart using cost, adding percentages and changing wedge colors
plt.pie(cost, autopct='%1.1f%%', colors= ('r', 'g','b', 'y', 'c', 'm'))

# creating the legend, labeling and positioning legend
plt.legend(labels= labels, title = 'Category', loc="right",  bbox_to_anchor=(1, 0, 0.5, 1)
          )
# adding a title to pie chart
plt.title('Average Monthly Expenses')

# creating finsihed pie chart 
plt.show()

## Plot

# month labels for 6 month period
month = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'

# plotting each category over the 6 month period and assigning marker symbols
plt.plot(month, carInsurance, marker='+')
plt.plot(month, phoneBill,  marker=11)
plt.plot(month, groceries,  marker='^')
plt.plot(month,gymMembership,  marker=4)
plt.plot(month, misc, marker = 'o')
plt.plot(month, amazon, marker = '*')

# labeling x-axis
plt.xlabel("Month")

# labeling y-axis
plt.ylabel("Amount ($)")

# creating a legend
plt.legend(labels = labels, bbox_to_anchor=(.5, .1, .6, .8))

# adding a title 
plt.title("Spending Trends")

# creating th finished plot
plt.show()

## Histogram 

# creating a tuple of lists that store all categories of expenses
expenses = carInsurance, phoneBill, groceries, gymMembership, misc, amazon

# plotting a histogram with the data from expenses 
plt.hist(expenses)

# labeling the x-axis
plt.xlabel("Amount ($)")

# labeling the y-axis
plt.ylabel("# of Months")

# creating the legend
plt.legend(labels = labels, bbox_to_anchor= (.5, .1, .6, .8 ))

# adding a title 
plt.title("Expenses")

# Creating the finsihed histogram
plt.show()
