# importing pandas
import pandas as pd
# Creating dataframe a
a = pd.DataFrame()
# Creating Dictionary
d = {'id': [1, 2, 10, 12],
     'val1': ['a', 'b', 'c', 'd']}
a = pd.DataFrame(d)
# printing the dataframe
print (a)

# importing pandas
import pandas as pd

# Creating dataframe b
b = pd.DataFrame()

# Creating dictionary
d = {'id': [1, 2, 9, 8],
     'val1': ['p', 'q', 'r', 's']}
b = pd.DataFrame(d)

# printing the dataframe
print(b)
# importing pandas
import pandas as pd
# Creating dataframe a
a = pd.DataFrame()
# Creating Dictionary
d = {'id': [1, 2, 10, 12],
     'val1': ['a', 'b', 'c', 'd']}
a = pd.DataFrame(d)
# Creating dataframe b
b = pd.DataFrame()
# Creating dictionary
d = {'id': [1, 2, 9, 8],
     'val1': ['p', 'q', 'r', 's']}
b = pd.DataFrame(d)
# inner join
df = pd.merge(a, b, on='id', how='inner')
# display dataframe
print(df)
# importing pandas
import pandas as pd
# Creating dataframe a
a = pd.DataFrame()
# Creating Dictionary
d = {'id': [1, 2, 10, 12],
     'val1': ['a', 'b', 'c', 'd']}
a = pd.DataFrame(d)
# Creating dataframe b
b = pd.DataFrame()
# Creating dictionary
d = {'id': [1, 2, 9, 8],
     'val1': ['p', 'q', 'r', 's']}
b = pd.DataFrame(d)
# left outer join
df = pd.merge(a, b, on='id', how='left')
# display dataframe
print(df)

# importing pandas
import pandas as pd
# Creating dataframe a
a = pd.DataFrame()
# Creating Dictionary
d = {'id': [1, 2, 10, 12],
     'val1': ['a', 'b', 'c', 'd']}
a = pd.DataFrame(d)
# Creating dataframe b
b = pd.DataFrame()
# Creating dictionary
d = {'id': [1, 2, 9, 8],
     'val1': ['p', 'q', 'r', 's']}
b = pd.DataFrame(d)
# right outer join
df = pd.merge(a, b, on='id', how='right')
# display dataframe
print(df)

# importing pandas
import pandas as pd
# Creating dataframe a
a = pd.DataFrame()
# Creating Dictionary
d = {'id': [1, 2, 10, 12],
     'val1': ['a', 'b', 'c', 'd']}
a = pd.DataFrame(d)
# Creating dataframe b
b = pd.DataFrame()
# Creating dictionary
d = {'id': [1, 2, 9, 8],
     'val1': ['p', 'q', 'r', 's']}
b = pd.DataFrame(d)
# full outer join
df = pd.merge(a, b, on='id', how='outer')
# display dataframe
print(df)

# importing pandas
import pandas as pd
# Creating dataframe a
a = pd.DataFrame()
# Creating Dictionary
d = {'id': [1, 2, 10, 12],
     'val1': ['a', 'b', 'c', 'd']}
a = pd.DataFrame(d)
# Creating dataframe b
b = pd.DataFrame()
# Creating dictionary
d = {'id': [1, 2, 9, 8],
     'val1': ['p', 'q', 'r', 's']}
b = pd.DataFrame(d)
# index join
df = pd.merge(a, b, left_index=True, right_index=True)
# display dataframe
print(df)






















