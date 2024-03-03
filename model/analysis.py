import pandas as pd
import matplotlib.pyplot as plt


class DataAnalyzer:
    def __init__(self, merged_df):
        self.merged_df = merged_df.copy()

    def total_sales_amount_per_customer(self, filename='AnalysisOutputResults/total_sales_per_customer.csv'):
        total_sales_per_customer = self.merged_df.groupby('customer_id')['price'].sum().reset_index()
        total_sales_per_customer = total_sales_per_customer.rename(columns={'price': 'total_sales_amount'})
        total_sales_per_customer.to_csv(filename, index=False)
        self.plot_and_save_bar_chart(total_sales_per_customer['customer_id'],
                                     total_sales_per_customer['total_sales_amount'],
                                     'Total Sales Amount per Customer',
                                     filename.replace('.csv', '_visualization.png'))

    def average_order_quantity_per_product(self, filename='AnalysisOutputResults/avg_order_quantity_per_product.csv'):
        avg_order_quantity_per_product = self.merged_df.groupby('product_id')['quantity'].mean().reset_index()
        avg_order_quantity_per_product = avg_order_quantity_per_product.rename(
            columns={'quantity': 'average_order_quantity'})
        avg_order_quantity_per_product.to_csv(filename, index=False)
        self.plot_and_save_bar_chart(avg_order_quantity_per_product['product_id'],
                                     avg_order_quantity_per_product['average_order_quantity'],
                                     'Average Order Quantity Per Product',
                                     filename.replace('.csv', '_visualization.png'))

    def top_selling_products(self, top_n=5, filename='AnalysisOutputResults/top_selling_products.csv'):
        """
                Identify the top-selling products based on the quantity sold.
                """
        # Ensure that the 'quantity' column is numeric
        self.merged_df['quantity'] = pd.to_numeric(self.merged_df['quantity'], errors='coerce')

        # Group by product_id and sum the 'quantity' for each product
        total_quantity_per_product = self.merged_df.groupby('product_id')['quantity'].sum().reset_index()

        # Sort the products based on total quantity sold
        top_selling_products = total_quantity_per_product.sort_values(by='quantity', ascending=False).head(top_n)

        top_selling_products.to_csv(filename, index=False)
        self.plot_and_save_bar_chart(top_selling_products['product_id'],
                                     top_selling_products['quantity'],
                                     'Top selling products',
                                     filename.replace('.csv', '_visualization.png'))

    def top_customers(self, top_n=5, filename='AnalysisOutputResults/top_customers.csv'):
        """
        Identify the top customers based on their total purchase amount.
        """
        # Ensure that the 'price' column is numeric
        self.merged_df['price'] = pd.to_numeric(self.merged_df['price'], errors='coerce')

        # Group by customer_id and sum the 'price' for each customer
        total_sales_per_customer = self.merged_df.groupby('customer_id')['price'].sum().reset_index()

        # Sort the customers based on total sales
        top_customers = total_sales_per_customer.sort_values(by='price', ascending=False).head(top_n)

        top_customers.to_csv(filename, index=False)
        self.plot_and_save_bar_chart(top_customers['customer_id'],
                                     top_customers['price'],
                                     'Top customers',
                                     filename.replace('.csv', '_visualization.png'))

    def top_sales_by_city(self, top_n=5, filename='AnalysisOutputResults/top_sales_by_city.csv'):
        """
        Identify the top sales by city based on the total purchase amount.
        """
        # Ensure that the 'price' column is numeric
        self.merged_df['price'] = pd.to_numeric(self.merged_df['price'], errors='coerce')

        # Group by city and sum the 'price' for each city
        total_sales_by_city = self.merged_df.groupby('city')['price'].sum().reset_index()

        # Sort the cities based on total sales
        top_sales_by_city = total_sales_by_city.sort_values(by='price', ascending=False).head(top_n)

        top_sales_by_city.to_csv(filename, index=False)
        self.plot_and_save_bar_chart(top_sales_by_city['city'],
                                     top_sales_by_city['price'],
                                     'Top sales city',
                                     filename.replace('.csv', '_visualization.png'))

    def sales_trends_over_time(self, time_period='monthly',
                               filename='AnalysisOutputResults/sales_trends_over_time.csv'):
        # Convert order_date to datetime
        self.merged_df['order_date'] = pd.to_datetime(self.merged_df['order_date'])

        if time_period == 'monthly':
            sales_trends = self.merged_df.groupby(self.merged_df['order_date'].dt.to_period("M"))[
                'price'].sum().reset_index()
        elif time_period == 'quarterly':
            sales_trends = self.merged_df.groupby(self.merged_df['order_date'].dt.to_period("Q"))[
                'price'].sum().reset_index()
        else:
            raise ValueError("Invalid time_period. Supported values: 'monthly', 'quarterly'.")

        # Convert period back to timestamp for plotting
        sales_trends['order_date'] = sales_trends['order_date'].dt.to_timestamp()

        sales_trends = sales_trends.rename(columns={'price': 'total_sales'})
        sales_trends.to_csv(filename, index=False)
        plt.figure(figsize=(12, 6))
        plt.plot(sales_trends['order_date'], sales_trends['total_sales'], marker='o', linestyle='-', color='blue')
        plt.xlabel('Time Period')
        plt.ylabel('Total Sales')
        plt.title('Sales Trends Over Time')
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save the plot as an image
        plt.savefig(filename.replace('.csv', '_plot.png'))

    def weather_data_in_analysis(self,filename='AnalysisOutputResults/weather_data_in_analysis.csv'):
        # Example: Calculate average sales amount per weather condition
        avg_sales_per_weather = self.merged_df.groupby('weather_conditions')['price'].mean().reset_index()
        avg_sales_per_weather = avg_sales_per_weather.rename(columns={'price': 'average_sales_amount'})
        avg_sales_per_weather.to_csv(filename,index=False)
        self.plot_and_save_bar_chart(avg_sales_per_weather['weather_conditions'],
                                     avg_sales_per_weather['average_sales_amount'],
                                     'Avg sales per weather',
                                     filename.replace('.csv', '_visualization.png'))

    def max_sale_per_weather_and_city(self, filename='AnalysisOutputResults/max_sale_per_weather_and_city.csv'):
        # Ensure that the 'price' column is numeric
        self.merged_df['price'] = pd.to_numeric(self.merged_df['price'], errors='coerce')

        # Group by weather_conditions and city and find the maximum sale for each group
        max_sale_per_weather_and_city = self.merged_df.groupby(['weather_conditions', 'city'])[
            'price'].max().reset_index()

        max_sale_per_weather_and_city.to_csv(filename, index=False)
        self.plot_max_sale_per_weather_and_city(max_sale_per_weather_and_city,
                                                filename.replace('.csv', '_visualization.png'))

    def plot_and_save_bar_chart(self, x, y, title, filename):
        plt.figure(figsize=(10, 6))
        plt.bar(x, y, color='skyblue')
        plt.xlabel('X-Axis Label')  # Customize as needed
        plt.ylabel('Y-Axis Label')  # Customize as needed
        plt.title(title)
        plt.xticks(x)
        plt.savefig(filename)
        plt.close()

    def plot_max_sale_per_weather_and_city(self, data, filename):
        plt.figure(figsize=(12, 8))
        for weather_condition, group in data.groupby('weather_conditions'):
            plt.bar(group['city'], group['price'], label=weather_condition, alpha=0.7)

        plt.xlabel('City')
        plt.ylabel('Max Sale Price')
        plt.title('Max Sale of Products in Each Weather and Each City')
        plt.legend(title='Weather Conditions', bbox_to_anchor=(1, 1))
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()


