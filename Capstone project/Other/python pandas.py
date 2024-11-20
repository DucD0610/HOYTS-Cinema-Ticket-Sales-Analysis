import pandas as pd

#create series with a list using pandas
list_value = [10, 20, 30, 40, 50]
pd.Series(list_value)

#note: the number of customized index must be the same as the number in the data frame
pd.Series(list_value, index=['a','b','d','e','f'])

#create data frame from dictionary
dict_value = {'a': 1, 'b':2, 'c':3, 'd':4, 'e':5}
pd.Series(dict_value)

value_count = s.value_counts()
print(value_count)

#pandas has build-in function describe (similar to R summarize)
s.describe()

'''Series'''
s = pd.Series(list_value)
s[1] #Access using index

dict_value['b'] #Access using label

s[0:5] #Access using slicing

s[s > 30] #Access using filter. E.g. data >30
#get data >30 AND % 4
s[(s > 30) & (s % 4 == 0)]

## Sorting
s.sort_values() #default ascending
s.sort_values(ascending = False)

## Operators + - * / > < =
s1 = [1,2,3,4,5]
s1 = pd.Series(s1)
s2 = [6,7,8,9,0]
s2 = pd.Series(s2)
s1 + s2 #however in a list, the 2 list will be concatenated instead of sum 2 values in the same index ; + - * /
s1 = s2 #boolean

## Common aggregated functions
print("Count: ", s.count())
print("Sum: ", s.sum())
print("Mean: ", s.mean())
print("Min:", s.min())
print("Max:", s.max())
print("Standard Deviation:", s.std())

## Common statistics
print("Frequency distribution: ", s.value_counts())
print("Describe data: ", s.describe()) #similar to R summarize.

'''Data frame'''
dict_value = {"name": ["Tony", "Alex", "Brian", "Kim", "Vu"],
              "age" : [25, 20, 18, 24, 15]
              }
students = pd.DataFrame(dict_value)
students['name']
students['age']

## read from file
help(pd.read_csv)
print(dir(pd))

df_campaign = pd.read_csv('D:/PyBI/pandas_exercises-master/MazPythonData/Dataset/campaign.csv')

df_customer = pd.read_csv('D:/PyBI/pandas_exercises-master/MazPythonData/Dataset/customer.csv')

df_device= pd.read_csv('D:/PyBI/pandas_exercises-master/MazPythonData/Dataset/device_detail.csv')

df_status = pd.read_csv('D:/PyBI/pandas_exercises-master/MazPythonData/Dataset/status_detail.csv')

df_ticket = pd.read_csv('D:/PyBI/pandas_exercises-master/MazPythonData/Dataset/ticket_history.csv')

######################################## EXTRACTION ##################################
# Viewing data
df_ticket.info() #to view structure and data organization (how many rows columns, data types)
df_ticket.head() 
df_ticket.tail()
df_ticket.describe()

# Truy xuat theo cot (dataframe)
df_ticket[['ticket_id', 'movie_name', 'time']]
df_ticket['ticket_id'] #note: return result as series without [[]]
df_ticket[['ticket_id']]

# Truy xuat theo hang (index, label)
df_ticket.loc[0]
df_ticket.loc[[0,2,4,7]]
df_ticket.loc[0:4]

# Truy xuat du lieu theo dieu kien
## Get records  that have discount value > 0
df_ticket[df_ticket['discount_value'] > 0]

## Get records that have paying_method = bank account & have discount
df_ticket[(df_ticket['paying_method'] == 'bank account') &
           (df_ticket['discount_value'] > 0 )]

## Get information of ticket_id, movie_name, paying_method of transactions that have discount
df_ticket[['ticket_id', 'movie_name', 'paying_method']][df_ticket['discount_value'] > 0]

######################################## INSERT #####################################
# Create a new column calls promote rate
df_ticket['promote_rate'] = df_ticket['discount_value'] / df_ticket['original_price']

##################################### SORT ##########################################
# Sap xep theo 1 cot
df_ticket.sort_values(by = 'time') #ascending
df_ticket.sort_values(by = 'time', ascending = False) #descending

# Sap xep theo nhieu cot
# Example: Giam dan ve mkt_campaign_code, va tang dan theo original_price
df_ticket.sort_values(by=['mkt_campaign_code','original_price'], ascending=[False, True])

########################### GROUP BY & AGGREGATION ##################################
# Group by 1 cot
# Example: Tinh doanh thu amount, so luong giao dich, so luong khach hang cua cac bo phim
# va sap xep theo thu tu giam dan theo doanh thu
df_ticket.groupby('movie_name').agg(
    total_sale = ('original_price', 'sum'), #use comma, if we have many aggregate functions
    total_transaction = ('ticket_id', 'nunique'),
    total_customer = ('customer_id', 'nunique')   
).reset_index()

# Group by nhieu cot
# Example: Tinh doanh thu amount, so luong giao dich, so luong khach hang cua cac bo phim
# theo tung hinh thuc thanh toan
# va sap xep theo thu tu giam dan theo doanh thu
df_ticket.groupby(['movie_name', 'paying_method']).agg(
    total_sale = ('original_price', 'sum'), #use comma, if we have many aggregate functions
    total_transaction = ('ticket_id', 'nunique'),
    total_customer = ('customer_id', 'nunique')   
).reset_index().sort_values(by = 'total_sale', ascending=False)

##################################### MERGE ##########################################
# Xu ly data tu nhieu dataframe
# Merge
df_ticket.head(1)
df_status.head(1)
pd.merge(df_ticket, df_status, how='inner', on='status_id')

# Concat
pd.concat([df_ticket, df_ticket], axis=1)
df_ticket