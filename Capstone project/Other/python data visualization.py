import pandas as pd
import matplotlib.pyplot as plt

df_sale = pd.read_csv('D:/PyBI/pandas_exercises-master/MazPythonData/Dataset/sales.csv')

################################## BAR CHART ##################################
df_sale.info()
df_sale.head()

# create a dataframe using pandas   
data = pd.DataFrame({'category':['bike', 'clothing', 'accessories'], 
                     'sale':[1000,2000,1500]})

# bieu do cot doc
plt.bar(data['category'], #data x-axis
        data['sale'])     #data y-axis   

plt.figure(figsize = (8,5)) #thay doi chieu dai & rong cua hinh (vd: chieu dai 10, chieu rong 5)
plt.title('Doanh so cua moi category')
plt.xlabel('Category')
plt.ylabel('Doanh thu (USD)')
plt.bar(data['category'], 
        data['sale'], color = 'skyblue', width=0.5)    #colour bar chart, thay doi do rong cua bar

# bieu do cot ngang
plt.barh(data['category'], #data x-axis
        data['sale'], height=0.5)     #data y-axis, thay doi do rong bar now height

# bieu do cot chong
data = pd.DataFrame({'X':['A', 'B', 'C', 'D'],
                     'Y1':[10, 20, 10, 30],
                     'Y2':[20, 25, 15, 25]
                     })

data = pd.DataFrame({'X':['A', 'B', 'C', 'D'],
                     'Y1':[10, 20, 10, 30],
                     'Y2':[20, 25, 15, 25]
                     })
plt.figure(figsize = (8,5))
data.plot(kind='bar', x = 'X', y = ['Y1', 'Y2'], stacked = True)
plt.title('Doanh thu cua Y1 va Y2 theo X')
plt.legend(loc = 'upper right') #di chuyen legend

# bieu do gom nhom
data.plot(kind='bar', x = 'X', y = ['Y1', 'Y2'], stacked = False)
plt.title('Doanh thu cua Y1 va Y2 theo X')
plt.legend(loc = 'upper right') #di chuyen legend

#Homework: O bang sale, hay ve bieu do thong ke doanh thu tung category
df = df_sale.groupby('Category').agg(
        total_sale = ('Sales', 'sum')
    ).reset_index()
plt.figure(figsize= (8,5))
plt.title('Sales by Category')
plt.xlabel('Categories')
plt.ylabel('Sales in USD')
plt.bar(df['Category'],
        df['total_sale'], color = 'skyblue', width=0.5
        )

################################## LINE CHART ##################################
data = pd.DataFrame({'year':['2015', '2016', '2017', '2018', '2019', '2020'],
                     'sale':[1000, 2000, 1500, 2100, 3000, 3500],
                     'profit':[500, 700, 1000, 1500, 2000, 2500]
                     })
plt.plot(data['year'], data['sale'], label='sale')
plt.plot(data['year'], data['profit'], label='profit')
plt.title('Sale and Profit by Years')
plt.xlabel('Years')
plt.ylabel('USD')
plt.legend() #need to define label in plt.plot

# Homework 1: Draw a chart showing sales of the shop by years
df_sale.head() #no year attribute.

df_sale['year'] = df_sale['Order Date'].str[-4:] #We can create year based on order date

df = df_sale.groupby('year').agg(
    total_sales = ('Sales', 'sum')).reset_index()
df

plt.plot(df['year'], df['total_sales'])
plt.ylim([0, 1000000]) #limit y to 1,000,000

# Homework 2: Draw a chart showing sales of categories by year
df_sale.head()

df = df_sale.groupby(['Category', 'year']).agg(
    total_sales = ('Sales', 'sum')).reset_index()

df_Technology = df[df['Category'] == 'Technology']
df_Furniture = df[df['Category'] == 'Furniture']
df_Office_Supplies = df[df['Category'] == 'Office Supplies']

plt.plot(df_Technology['year'], df_Technology['total_sales'], label = 'Technology')
plt.plot(df_Furniture['year'], df_Furniture['total_sales'], label = 'Furniture')
plt.plot(df_Office_Supplies['year'], df_Office_Supplies['total_sales'], label = 'Office_Supplies')
plt.ylim(0, 400000)
plt.legend()
plt.title('Category Sales by Years')
plt.xlabel('Years')
plt.ylabel('USD')

################################## PIE CHART ###############################



################################## HISTOGRAM ##################################
import numpy as np

data = np.random.randn(1000) #create 1000 random numbers
plt.hist(data, bins = 30) #bin is number of segments of data. bin 30 means 30 segments

#Homework: draw a chart to show the distribution of sale value of orders in Technology category
df_sale_technology = df_sale[df_sale['Category'] == 'Technology']['Sales']
df_sale_technology.describe()
plt.hist(df_sale_technology, bins = 50)
plt.xlim(0, 6000)
plt.title('Sale Values Distribution of Technology Orders')
plt.xlabel('USD Amount ')
plt.ylabel('Order Numbers')