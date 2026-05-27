import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

df=pd.read_csv("C:/Users/hp/OneDrive/Desktop/FUTURE-ML-01/Sample-Superstore.csv",encoding='ISO-8859-1')
df.columns=df.columns.str.replace(' ', '_').str.lower()
df=df.fillna(0)
df['order_date']=pd.to_datetime(df['order_date'])
df['year']=df['order_date'].dt.year
df['month']=df['order_date'].dt.month
df['day']=df['order_date'].dt.day
df['day_of_week']=df['order_date'].dt.dayofweek
daily_sales=df.groupby('order_date').agg({'sales':'sum','year':'first','month':'first','day':'first','day_of_week':'first'}).reset_index()

X=daily_sales[['year','month','day','day_of_week']]
y=daily_sales['sales']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,shuffle=False)
model=LinearRegression()
model.fit(X_train,y_train)
predictions=model.predict(X_test)
mae=mean_absolute_error(y_test,predictions)
plt.figure(figsize=(12,6))
plt.plot(daily_sales['order_date'].iloc[-len(y_test):],y_test,label='Actual Sales',color='blue')
plt.plot(daily_sales['order_date'].iloc[-len(y_test):],predictions,label='Predicted Sales',color='red',linestyle='--')
plt.title('Actual vs Predicted Demand/Sales')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.savefig('sales_forecast.png')
plt.show()