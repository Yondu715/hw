import re
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from data_shower import DataShower
from dataframe_config import Column
from fake_useragent import UserAgent
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from regexp_vars import brand_models, dict_models, dict_param_separate, transmission_regex, odometer_regex, fuel_regex, horse_power_regex, engine_regex


class CarParser:
    __driver: webdriver.Chrome = None

    brand: str = None

    data: pd.DataFrame = pd.DataFrame(
        columns=[column.value for column in Column]
    )

    def __init__(self, brand: str = None) -> None:
        if brand is not None:
            self.brand = brand.lower()
        else:
            self.brand = None
        self.__driver = self.__setup_driver()
    
    def __del__(self):
        self.__driver.quit()
    
    def __create_user_agent(self) -> str:
        ua = UserAgent(
            browsers=['chrome'],
            platforms=['pc']
        )
        return ua.random

    
    def __setup_driver(self) -> webdriver.Chrome:
        service = ChromeService(ChromeDriverManager().install())

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-geolocation")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument(f"--user-agent={self.__create_user_agent()}")

        driver = webdriver.Chrome(service=service, options=options)
        return driver


    def __setup_parser(self, content: str) -> BeautifulSoup:
        return BeautifulSoup(content, features='lxml')
        
    def __print_progress(self, site: str, page: int) -> None:
        print(f"Сайт: {site}; Страниц просканировано - {page}")
    
    def to_csv(self, filename: str, separator: str):
        self.data.to_csv(f"{filename}.csv", index=False, encoding='utf-8', sep=separator)

    def add_data(
            self,
            brand: str = None,
            price: str = None,
            model: str = None,
            year: str = None,
            odometer: str = None,
            transmission: str = None,
            fuel: str = None,
            horse_power: str = None,
            engine: str = None
        ) -> None:
        new_row = pd.Series({
            Column.brand.value: brand,
            Column.price.value: price,
            Column.model.value: model,
            Column.year.value: year,
            Column.odometer.value: odometer,
            Column.transmission.value: transmission,
            Column.fuel.value: fuel,
            Column.horse_power.value: horse_power,
            Column.engine.value: engine
        })
        self.data = pd.concat([self.data, new_row.to_frame().T], ignore_index=True)
    
    def norm_data(self):
        self.data = self.data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

        self.data[Column.price.value] = self.data[Column.price.value].astype(str).str.replace('₽', '').str.replace('\u00a0', '').str.replace(' ', '')
        self.data[Column.odometer.value] = self.data[Column.odometer.value].astype(str).str.replace('км', '').str.replace(' ', '')
        self.data[Column.horse_power.value] = self.data[Column.horse_power.value].astype(str).str.replace('л.с.', '').str.replace(' ', '')
        self.data[Column.engine.value] = self.data[Column.engine.value].astype(str).str.replace('л', '').str.replace(' ', '')

        for key, value in dict_models.items():
            pattern = re.compile(value, re.IGNORECASE)
            self.data[Column.model.value] = self.data[Column.model.value].str.replace(pattern, key, regex=True)
    
    def norm_brand(self, site: str):
        separator = dict_param_separate[site]
        return separator.join(self.brand.split())
    
    def find_by_regex(self, pattern: str, text: str):
        regex = re.compile(pattern, re.IGNORECASE)
        match = re.search(regex, text)
        if match:
            return match.group().lower()
        return None


    def parse_drom(self, start_page: int = 1, end_page: int = 1) -> None:
        for page in range(start_page, end_page + 1):
            if self.brand:
                self.__driver.get(f'https://auto.drom.ru/{self.norm_brand('drom')}/all/page{page}/?pts=2&damaged=2&unsold=1')
            else:
                self.__driver.get(f'https://auto.drom.ru/all/page{page}/?pts=2&damaged=2&unsold=1')

            content = self.__driver.page_source
            soup = self.__setup_parser(content)

            ads_blocks = soup.find_all('a', attrs={'data-ftid': 'bulls-list_bull'})
            for ads in ads_blocks:
                title_block = ads.find('div', attrs={'data-ftid': 'bull_title'})
                price_block = ads.find('span', attrs={'data-ftid': 'bull_price'})
                description_block = ads.find_all('span', attrs={'data-ftid': 'bull_description-item'})
                info = ''.join(block.text for block in description_block)

                data = title_block.text.split(',')

                year = data[1]
                price = price_block.text
                brand = self.find_by_regex(r'|'.join(brand_models.keys()), title_block.text)
                model = self.find_by_regex(brand_models.get(brand, ''), title_block.text)
                odometer = self.find_by_regex(odometer_regex, info)
                transmission = self.find_by_regex(transmission_regex, info)
                fuel = self.find_by_regex(fuel_regex, info)
                horse_power = self.find_by_regex(horse_power_regex, info)
                engine = self.find_by_regex(engine_regex, info)

                self.add_data(brand=brand, price=price, model=model, year=year, odometer=odometer, transmission=transmission, fuel=fuel, horse_power=horse_power, engine=engine)

            self.__print_progress('drom.ru', page)


    def parse_sberauto(self, start_page: int = 1, end_page: int = 1):
        for page in range(start_page, end_page + 1):
            if self.brand:
                self.__driver.get(f'https://sberauto.com/cars/{self.norm_brand('sberauto')}?isCreditSearchEnabled=false&isWarrantySearchEnabled=false&page={page}')
            else:
                self.__driver.get(f'https://sberauto.com/cars?page={page}')

            content = self.__driver.page_source
            soup = self.__setup_parser(content)

            ads_blocks = soup.find_all('a', attrs={'data-test-id': re.compile('car_card_')})
            for ads in ads_blocks:
                name_block = ads.find('h6', attrs={'data-testid': 'carName'})
                price_block = ads.find('span', attrs={'data-testid': 'carPrice'})
                info_blocks = ads.find('ul', attrs={'data-testid': 'carInfo'}).find_all('li')
                odometer_block = info_blocks[0]
                transmission_block = info_blocks[1]
                det_info = info_blocks[2].text

                name = name_block.text.split(',')

                brand = self.find_by_regex(r'|'.join(brand_models.keys()), name[0])
                model = self.find_by_regex(brand_models.get(brand, ''), name[0])
                odometer = self.find_by_regex(odometer_regex, odometer_block.text)
                transmission = self.find_by_regex(transmission_regex, transmission_block.text)
                fuel = self.find_by_regex(fuel_regex, det_info)
                horse_power = self.find_by_regex(horse_power_regex, det_info)
                engine = self.find_by_regex(engine_regex, det_info)
                year = name[1]
                price = price_block.text

                self.add_data(brand=brand, price=price, model=model, year=year, odometer=odometer, transmission=transmission, fuel=fuel, horse_power=horse_power, engine=engine)
            self.__print_progress('sberauto.com', page)


    def parse_avito(self, start_page: int = 1, end_page: int = 1):
        for page in range(start_page, end_page + 1):
            time.sleep(1.5)
            if self.brand:
                self.__driver.get(f'https://www.avito.ru/all/avtomobili/{self.norm_brand('avito')}?p={page}')
            else:
                self.__driver.get(f'https://www.avito.ru/all/avtomobili?p={page}')
            content = self.__driver.page_source
            soup = self.__setup_parser(content)
            ads_blocks = soup.find_all('div', attrs={'data-marker': 'item'})
            for ads in ads_blocks:
                name_block = ads.find(attrs={'itemprop': 'name'})
                price_block = ads.find('p', attrs={'data-marker': 'item-price'})
                info_block = ads.find('p', attrs={'data-marker': 'item-specific-params'})

                name = name_block.text.split(',', 3)
                info = info_block.text.split(',')
                brand = self.find_by_regex(r'|'.join(brand_models.keys()), name[0])
                model = self.find_by_regex(brand_models.get(brand, ''), name[0])
                odometer = self.find_by_regex(odometer_regex, info[0])
                fuel = self.find_by_regex(fuel_regex, info[-1])
                transmission = self.find_by_regex(transmission_regex, info[-2])
                horse_power = self.find_by_regex(horse_power_regex, info[1])
                engine = self.find_by_regex(engine_regex, info[1])     

                year = name[1]
                price = price_block.text

                self.add_data(brand=brand, price=price, model=model, year=year, odometer=odometer, fuel=fuel, horse_power=horse_power, engine=engine)
            self.__print_progress('avito.ru', page)


if __name__ == '__main__':
    FILENAME = "kem_cars"
    SEPARATOR = ";"

    df = pd.read_csv(f"{FILENAME}.csv", sep=SEPARATOR)
    # parser = CarParser()
    # parser.parse_drom(start_page=1, end_page=1000)
    # parser.parse_sberauto(start_page=1, end_page=1000)
    # parser.parse_avito(start_page=1, end_page=1)
    # parser.norm_data()
    # parser.to_csv(FILENAME, SEPARATOR)
    shower = DataShower()
    shower.show_data(df)


