import pandas as pd
from car_parser import Column
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression


df = pd.read_csv('kem_cars.csv', sep=';')
df_test = pd.read_csv('kem_cars_test.csv', sep=';')

df[Column.odometer.value] = df.apply(
    lambda row: 0 if pd.isna(row[Column.odometer.value]) and row[Column.year.value] == [2024, 2023] else row[Column.odometer.value],
    axis=1
)

df = df.dropna()

label_encoder = LabelEncoder()

# train
df[Column.brand.value] = label_encoder.fit_transform(df[Column.brand.value])
df[Column.model.value] = label_encoder.fit_transform(df[Column.model.value])
df[Column.fuel.value] = label_encoder.fit_transform(df[Column.fuel.value])
df[Column.transmission.value] = label_encoder.fit_transform(df[Column.transmission.value])
print(df)

#test
df_test[Column.brand.value] = label_encoder.fit_transform(df_test[Column.brand.value])
df_test[Column.model.value] = label_encoder.fit_transform(df_test[Column.model.value])
df_test[Column.fuel.value] = label_encoder.fit_transform(df_test[Column.fuel.value])
df_test[Column.transmission.value] = label_encoder.fit_transform(df_test[Column.transmission.value])

X = df.drop([Column.price.value], axis=1)
y = df[Column.price.value]

model = LinearRegression()
model.fit(X, y)

predicted_price = model.predict(df_test)[0]
print(f"Предсказанная цена автомобиля: {predicted_price}")