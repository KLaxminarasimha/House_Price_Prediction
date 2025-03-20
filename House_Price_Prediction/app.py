import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df=pd.read_csv("Housing.csv")
binary_colums=['mainroad','guestroom','basement','hotwaterheating','airconditioning','prefarea']
for col in binary_colums:
  df[col]=df[col].map({'yes':1,'no':0})
df['furnishingstatus']=df['furnishingstatus'].map({'furnished':1,'semi-furnished':2,'unfurnished':3})
X = df.drop(columns=['price'])
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
with open("model.pkl","wb") as file:
	pickle.dump(model,file)
print("Model Trained successfully")