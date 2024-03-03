USE AIQ;

CREATE TABLE AverageOrderQuantity (
    product_id INT PRIMARY KEY,
    average_order_quantity DECIMAL(10, 8)
);

CREATE TABLE WeatherSales (
    id INT PRIMARY KEY AUTO_INCREMENT,
    weather_conditions VARCHAR(255),
    city VARCHAR(255),
    price DECIMAL(10, 2)
);

CREATE TABLE SalesTrends (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_date DATE,
    total_sales DECIMAL(10, 2)
);

CREATE TABLE TopCustomers (
    customer_id INT PRIMARY KEY,
    total_purchase DECIMAL(10, 2)
);

CREATE TABLE TopSalesByCity (
    city VARCHAR(255) PRIMARY KEY,
    total_sales DECIMAL(10, 2)
);

CREATE TABLE ProductQuantity (
    product_id INT PRIMARY KEY,
    quantity INT
);

CREATE TABLE CustomerTotalSales (
    customer_id INT PRIMARY KEY,
    total_sales_amount DECIMAL(10, 2)
);

CREATE TABLE WeatherAverageSales (
    weather_conditions VARCHAR(255) PRIMARY KEY,
    average_sales_amount DECIMAL(10, 2)
);




LOAD DATA INFILE 'AnalysisOutputResults/avg_order_quantity_per_product.csv'
INTO TABLE AverageOrderQuantity
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE 'AnalysisOutputResults/max_sale_per_weather_and_city.csv'
INTO TABLE WeatherSales
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE 'AnalysisOutputResults/sales_trends_over_time.csv'
INTO TABLE SalesTrends
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(order_date, total_sales);

LOAD DATA INFILE 'AnalysisOutputResults/top_customers.csv'
INTO TABLE TopCustomers
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(customer_id, total_purchase);

LOAD DATA INFILE 'AnalysisOutputResults/top_sales_by_city.csv'
INTO TABLE TopSalesByCity
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(city, total_sales);

LOAD DATA INFILE 'AnalysisOutputResults/top_selling_products.csv'
INTO TABLE ProductQuantity
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(product_id, quantity);

LOAD DATA INFILE 'AnalysisOutputResults/total_sales_per_customer.csv'
INTO TABLE CustomerTotalSales
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(customer_id, total_sales_amount);

LOAD DATA INFILE 'AnalysisOutputResults/weather_data_in_analysis.csv'
INTO TABLE WeatherAverageSales
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(weather_conditions, average_sales_amount);
