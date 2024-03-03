# -*- coding: utf-8 -*-
from configs.config import CFG
from model.mymodel import MyModel
from model.analysis import DataAnalyzer
import pandas as pd


def run():
    model = MyModel(CFG)
    model.make_connection()
    model.load_data()
    model.validate_schema()
    model.load_api_data()
    model.validate_api_schema()
    model.merge_user_data()
    model.merge_user_and_weather_data()
    final_df = pd.read_csv("final_data.csv")
    data_analyzer = DataAnalyzer(final_df)
    data_analyzer.total_sales_amount_per_customer()
    data_analyzer.average_order_quantity_per_product()
    data_analyzer.top_selling_products(top_n=5)
    data_analyzer.top_customers(top_n=5)
    data_analyzer.top_sales_by_city(top_n=5)
    data_analyzer.sales_trends_over_time(time_period='monthly')
    data_analyzer.weather_data_in_analysis()
    data_analyzer.max_sale_per_weather_and_city()


if __name__ == "__main__":
    run()