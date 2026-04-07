import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import pickle

# Load data
data = pd.read_csv("canteen_data.csv")

# Encode Day
le = LabelEncoder()
data['Day'] = le.fit_transform(data['Day'])

# Features & Target
X = data[['Day','Students','Queue_Length']]
y = data['Waiting_Time_Min']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained & saved!")