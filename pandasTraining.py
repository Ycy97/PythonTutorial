#Pandas is a Pyton library used for working with data sets
#It has functions for analyzing, cleaning, exploring, and manipulating data

# import pandas as pd

# mydataset = {
#     'cars' : ["BMW","Volvo","Ford"],
#     'passings' : [3,7,2]
# }

# myvar = pd.DataFrame(mydataset)

# print(myvar)

#Pandas Series, like a column of data
#It is a one-dimensional array holding data of any type

# import pandas as pd

# a = [1,7,2]
# myvar = pd.Series(a)
# print(myvar)

# #If ntng else is specified, the values are labeled with their index number.
# #Label can be used to access a specified value
# print(myvar[0])

#Create Labels : index argument/parameter to name our own labels
# import pandas as pd
# a = [1,7,2]
# myvar = pd.Series(a,index=["x","y","z"])
# print(myvar)

# #thus we can access the item by referring to the label
# print(myvar["y"])

#Key/Value Objects as Series, the keys becomes the labels
# import pandas as pd
# calories = {"day1":420, "day2":380, "day3":390}
# myvar = pd.Series(calories)
# print(myvar)

#To select only some of the items in the dictionary, use the index argument
#and specify only the items we want to include in the Series
# import pandas as pd
# calories = {"day1":420, "day2":380, "day3":390}
# myvar = pd.Series(calories,index=["day1","day2"])
# print(myvar)

#DataFrames
#Data sets in Pandas are usually multi-dimensional tables called DataFrames
#Series is like a column, a DataFrame is the whole table with rows and columns
# import pandas as pd
# data = {
#     "calories":[420,380,390],
#     "duration":[50,40,45]
# }

# df = pd.DataFrame(data)
# print(df)

# #Locate Row
# print(df.loc[0]) #returns a Pandas Series

# #to return row 9 and 1, use a list of indexes
# print(df.loc[[0,1]])#when using [], returns Pandas Data Frame

#Named indexes for DataFrames
# import pandas as pd

# data = {
#     "calories" : [420,380,390],
#     "duration" : [50,40,45]
# }

# df = pd.DataFrame(data,index=["day1","day2","day3"])

# print(df)

# #locate named indexes
# print(df.loc["day1"])

# print(df.loc[["day1","day2"]])

#Pandas Read CSV
# import pandas as pd
# df = pd.read_csv('data.csv')
# print(df.to_string()) #to_string() method to print out the entire DataFrame, else by default will only return first 5 rows and last 5 rows

#max_rows
#the number of roes returned in defined in Pandas option settings
# import pandas as pd

# print(pd.options.display.max_rows)

##Pandas-Analyzing DataFrames##

#Viewing the Data
#one of the most used method for getting quick overview of the DataFrame : head(), returns specified no. of rows fron top
# import pandas as pd
# df = pd.read_csv('data.csv')
# print(df.head(10))

#to print the last rows : tail()
# print(df.tail(10))

#info about the data : info()
# print(df.info())

#Pandas - Cleaning Data
#Fixing bad data in data set
# Such as :
#   1) Empty cells
#   2) Data in wrong format
#   3) Wrong Data
#   4) Duplicates

#Cleaning Empty Cells
# import pandas as pd

# df = pd.read_csv('data.csv')
# new_df = df.dropna()
# print(df.to_string())
# print(new_df.to_string())

#if we want to change the original DataFrame, use inplace=True
# import pandas as pd

# df = pd.read_csv('data.csv')
# df.dropna(inplace=True)
# print(df.to_string())

#Replace Empty Values
#another way of dealing with empty cells is to insert a new value  : fillna()
# import pandas as pd

# df = pd.read_csv('data.csv')
# df.fillna(130, inplace=True)
# print(df.to_string())

#Replace only for specified Columns
# import pandas as pd
# df = pd.read_csv('data.csv')
# df["Calories"].fillna(130,inplace=True)
# print(df.to_string())

#Replace Using Mean, Median or Mode
#another common way is to calculate mean, median or mode of column and replace empty cells
# import pandas as pd
# df = pd.read_csv('data.csv')
# x = df["Calories"].mean()
# df["Calories"].fillna(x,inplace=True)
# print(f"{x} is the mean value")
# print(df.to_string())

#Median
# from statistics import median
# import pandas as pd
# df = pd.read_csv('data.csv')
# medianVal = df["Calories"].median()

# print(medianVal)

# df["Calories"].fillna(medianVal,inplace=True)

# print(df.to_string())

#Mode, mode()[0] because mode() returns a series and we only want a single val
# import pandas as pd
# df = pd.read_csv("data.csv")
# modeVal = df["Calories"].mode()[0]
# print(f"The mode value : {modeVal}")
# df["Calories"].fillna(modeVal,inplace=True)
# print(df["Calories"].to_string())

#Pandas - Fixing Wrong Data
#replacing single value : df.loc[7,'Duration'] = 45

#using for loops

# for x in df.index:
#     if df.loc[x, "Duration"] > 120:
#         df.loc[x, "Duration"] = 120

#Pandas - Removing Duplicates
#to discover duplicates : duplicated() will return true
# import pandas as pd

# df = pd.read_csv('data.csv')
# print(df.duplicated().to_string())
# df.drop_duplicates(inplace=True)
# print(df.to_string())

#Pandas - Data Correlations : corr()
# import pandas as pd

# df = pd.read_csv('data.csv')
# print(df.corr())

#Pandas - Plotting
#Pandas uses plot() method to create diagrams
#pyplot is a submodule of matplotlib to visualize diagram

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('data.csv')
# df.plot()
# plt.show()

#Scatter Plot
#specify type of plot with 'kind' argument, kind="scatter", scatter plot requires x and y-axis

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('data.csv')
# df.plot(kind='scatter', x = 'Duration', y = 'Calories')
# plt.show()

#Histogram
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('data.csv')
# df["Duration"].plot(kind='hist')
# plt.show()