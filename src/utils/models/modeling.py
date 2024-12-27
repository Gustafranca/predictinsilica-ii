"""Linear regression to predict % Silica concentrated"""
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

train_data = pd.read_csv('data/interim/train_MiningProcess.csv')
test_data = pd.read_csv('data/interim/test_MiningProcess.csv')

features = ['% Silica Feed', 'Amina Flow', 'Ore Pulp pH',
            'Flotation Column 01 Air Flow', 'Flotation Column 02 Air Flow',
             'Flotation Column 03 Air Flow']
target = '% Silica Concentrate'

X_train = train_data[features]
y_train = train_data[target]
X_test = test_data[features]
y_test = test_data[target]

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Erro: {mse}")
print(f"R^2 Score: {r2}")
