# Importing the relevant libraries.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Uploading all the csv files that represents my monthly expenses using Pandas.
january=pd.read_csv("january.csv",encoding = 'unicode_escape')
february=pd.read_csv("february.csv",encoding = 'unicode_escape')
march=pd.read_csv("march.csv",encoding = 'unicode_escape')
april=pd.read_csv("april.csv",encoding = 'unicode_escape')
may=pd.read_csv("may.csv",encoding = 'unicode_escape')
june=pd.read_csv("june.csv",encoding = 'unicode_escape')
july=pd.read_csv("july.csv",encoding = 'unicode_escape')
august=pd.read_csv("august.csv",encoding = 'unicode_escape')
september=pd.read_csv("september.csv",encoding = 'unicode_escape')
october=pd.read_csv("october.csv",encoding = 'unicode_escape')
november=pd.read_csv("november.csv",encoding = 'unicode_escape')
december=pd.read_csv("december.csv",encoding = 'unicode_escape')
# Calculating the sum of my expenses for each month.
total_cost1=january["total price"].sum()
total_cost2=february["total price"].sum()
total_cost3=march["total price"].sum()
total_cost4=april["total price"].sum()
total_cost5=may["total price"].sum()
total_cost6=june["total price"].sum()
total_cost7=july["total price"].sum()
total_cost8=august["total price"].sum()
total_cost9=september["total price"].sum()
total_cost10=october["total price"].sum()
total_cost11=november["total price"].sum()
total_cost12=december["total price"].sum()
# Creating a list of all the calculations above.
costs=[total_cost1,total_cost2,total_cost3,total_cost4,total_cost5,total_cost6,total_cost7,total_cost8,total_cost9,total_cost10,total_cost11,total_cost12]
# Creating a dictionary as follow: numbers represents the keys and the names represents the months.
months={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
# Creating a list from the dictionary keys.
months_list=list(months.keys())
# Creating the x_axis values using Numpy.
index=np.arange(months_list[0],months_list[-1]+1)
# Creating a bar plot to show the yearly expenses on 2018 using Matplotlib.
plt.figure(figsize=(20,4))
plt.bar(index,costs,width=0.5)
plt.xticks(index,months.values())
plt.title("2018 Expenses")
plt.xlabel("months")
plt.ylabel("total cost")
plt.show()


