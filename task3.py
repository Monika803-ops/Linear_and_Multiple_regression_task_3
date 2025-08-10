import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("Housing.csv")
print(df.head())

df = pd.get_dummies(df, drop_first=True)

X_simple = df[['area']]
y = df['price']

X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(X_simple, y, test_size=0.2, random_state=42)

lr_simple = LinearRegression()
lr_simple.fit(X_train_s, y_train_s)

y_pred_s = lr_simple.predict(X_test_s)

print("\nSimple Linear Regression:")
print(f"MAE: {mean_absolute_error(y_test_s, y_pred_s):.2f}")
print(f"MSE: {mean_squared_error(y_test_s, y_pred_s):.2f}")
print(f"R_square: {r2_score(y_test_s, y_pred_s):.4f}")

plt.scatter(X_test_s, y_test_s, color='blue', label='Actual')
plt.plot(X_test_s, y_pred_s, color='red', linewidth=2, label='Predicted Line')
plt.xlabel('Area')
plt.ylabel('Price')
plt.title('Simple Linear Regression (Area vs Price)')
plt.legend()
plt.show()

X_multi = df.drop(['price'], axis=1)
y = df['price']

X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(X_multi, y, test_size=0.2, random_state=42)

lr_multi = LinearRegression()
lr_multi.fit(X_train_m, y_train_m)

y_pred_m = lr_multi.predict(X_test_m)

print("\nMultiple Linear Regression:")
print(f"MAE: {mean_absolute_error(y_test_m, y_pred_m):.2f}")
print(f"MSE: {mean_squared_error(y_test_m, y_pred_m):.2f}")
print(f"R_Square: {r2_score(y_test_m, y_pred_m):.4f}")

print("\nModel Coefficients Interpretation:")
coeff_df = pd.DataFrame(lr_multi.coef_, X_multi.columns, columns=['Coefficient'])
print(coeff_df)

print("\nInterpretation ")
print(f"If 'area' increases by 1 sq ft, price changes by {coeff_df.loc['area','Coefficient']:.2f} units (holding other variables constant).")

plt.scatter(y_test_m, y_pred_m, color='green')
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted Prices (Multiple Regression)")
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.show()

print("Intercept (constant term) of the model is:", lr_multi.intercept_)
