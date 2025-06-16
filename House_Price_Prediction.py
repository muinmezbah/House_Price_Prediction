import pandas as pd
from sklearn.linear_model import LinearRegression

#Sample Data=
data= {
    'area': [1000,1500,2000,2500,3000],
    'price': [25000,37500,50000,62500,75000]
}

df=pd.DataFrame(data)
print("Data Preview")
print(df.head())

x=df[['area']]
y=df[['price']]

model=LinearRegression()
model.fit(x,y)

#user import
area=float(input("Enter Area: \n"))

#predict

predicted_price=model.predict([[area]])

#output
print(f"Predicted Price: Tk {predicted_price[0][0]:,.2f}")