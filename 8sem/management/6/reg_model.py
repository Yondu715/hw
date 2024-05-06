import pandas as pd
from car_parser import Column
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import Ridge

df = pd.read_csv('kem_cars.csv', sep=';')
df = df.dropna()

X_dict = df[[
    Column.brand.value,
    Column.model.value,
    Column.year.value,
    Column.odometer.value,
    Column.transmission.value,
    Column.fuel.value,
    Column.horse_power.value,
    Column.engine.value
]].to_dict('records')

enc = DictVectorizer()
X = enc.fit_transform(X_dict)

y = df[Column.price.value]

Модель = Ridge(alpha=0.1)
Модель.fit(X, y)

new_car = {
    Column.brand.value: 'toyota',
    Column.model.value: 'camry',
    Column.year.value: 2020,
    Column.odometer.value: 50000,
    Column.transmission.value: 'автомат',
    Column.fuel.value: 'бензин',
    Column.horse_power.value: 181,
    Column.engine.value: 2.0
}

new_car_X = enc.transform([new_car])
predicted_price = Модель.predict(new_car_X)[0]
print(f"Предсказанная цена автомобиля: {predicted_price}")