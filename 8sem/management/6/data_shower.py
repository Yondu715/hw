import matplotlib.pyplot as plt
from dataframe_config import Column
import pandas as pd

class DataShower():

    def show_data(self, data: pd.DataFrame):
        top_brands = data[Column.brand.value].value_counts().head(10)
        plt.figure(figsize=(10, 6))
        plt.bar(top_brands.index, top_brands.values)
        plt.xlabel('Марка')
        plt.ylabel('Количество объявлений')
        plt.title(f'Топ 10 марок')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()