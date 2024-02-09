# Python program to illustrate
# creating a data frame using CSV files
# import pandas module
import pandas as pd
# creating a data frame
df = pd.read_csv("C:\\Users\\Sumedha\\OneDrive\\Desktop\\biodata.csv")
print(df.head())


# Python program to illustrate
# creating a data frame using CSV files

# import pandas module
import pandas as pd

# creating a data frame
df = pd.read_table("C:\\Users\\Sumedha\\OneDrive\\Desktop\\biodata.csv", delimiter=", ")
print(df.head())

# Python program to illustrate
# creating a data frame using CSV files
# import pandas module
import pandas as pd
# import csv module
import csv
with open("C:\\Users\\Sumedha\\OneDrive\\Desktop\\biodata.csv") as csv_file:
    # read the csv file
    csv_reader = csv.reader(csv_file)

    # now we can use this csv files into the pandas
    df = pd.DataFrame([csv_reader], index=None)
# iterating values of first column
for val in list(df[2]):
    print(val)











