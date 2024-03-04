# Data_Engineer_Project

## Table of Contents

- [Overview](#overview)
- [Components](#components)
  - [1. main.py](#1-mainpy)
  - [2. model](#2-model)
    - [a. mymodel.py](#a-mymodelpy)
    - [b. analysis.py](#b-analysispy)
  - [3. dataloader](#3-dataloader)
  - [4. configs](#4-configs)
  - [5. SQLQuery](#5-sqlquery)
  - [6. MyException](#6-myexception)
  - [7. utils](#7-utils)
  - [8. tests](#8-tests)
  - [9. AnalysisOutputResults](#9-analysisoutputresults)
- [Usage Instructions](#usage-instructions)
  - [Install Dependencies](#install-dependencies)
  - [Database Configuration](#database-configuration)
  - [API Configuration](#api-configuration)
  - [Run the Data Pipeline](#run-the-data-pipeline)
  - [View Results](#view-results)
  - [Unit Testing](#unit-testing)
- [Contributing](#contributing)
- [Area of Improvement](#area-of-improvement)

## Data Pipeline for AIQ Data Engineer Assignment
### Overview
This data pipeline processes sales data, user data, and weather data to generate insights and visualizations. It is designed to be run using the main.py script, which orchestrates the entire pipeline.

#### Note 1 - Create a table "sales" in mysql and load "AIQ - Data Engineer Assignment - Sales data.csv" using Import wizard.
#### Note 2 - Edit config.py with your credientials and information.

#### Components
##### 1. main.py
The main script that triggers the data pipeline. It performs the following steps:

Connects to the MySQL database.
Loads sales data from the database.
Validates the schema of the sales data.
Fetches user data from an API.
Validates the schema of the user data.
Merges user data with sales data.
Merges user and weather data based on location.
Outputs the final merged data to a CSV file.
After the data processing, it initializes a DataAnalyzer to perform various analyses on the final data.

##### 2. model
a. mymodel.py
Contains the MyModel class, responsible for interacting with the data sources, performing data operations, and managing the data pipeline.

b. analysis.py
Includes the DataAnalyzer class, which performs various analyses on the final merged data, such as calculating total sales amount per customer, average order quantity per product, and generating visualizations.

##### 3. dataloader
Contains utility functions for loading data. dataloader.py includes functions for making a connection to the MySQL database, loading sales data, and fetching user data from an API.

##### 4. configs
Stores configuration files for the data pipeline, including config.py for general configurations and logging_config.yaml for logging settings.

##### 5. SQLQuery
Includes SQL queries for creating and loading data into the MySQL database.

##### 6. MyException
Contains exception handling classes. exceptions.py defines custom exceptions for better error handling.

##### 7. utils
Contains utility functions and configurations, such as config.py for configuration settings and logger.py for logging setup.

##### 8. tests
Includes unit tests for the data pipeline components.

##### 9. AnalysisOutputResults
Stores the output of the data analysis, including CSV files and visualizations.

#### Usage Instructions
Install Dependencies:

Make sure you have Python 3.9 installed.

Install the required dependencies using:

bash
Copy code
``` bash
git clone https://github.com/himalayaashish/Data_Engineer_Project.git
```
```bash
cd Data_Engineer_Project
```
```python
pip install -r requirements.txt
```
Database Configuration:

Configure the MySQL database connection details in configs/config.py.
API Configuration:

Update the API endpoint in main.py with the desired endpoint for fetching user data.
Run the Data Pipeline:

Execute the following command in the terminal:

bash
Copy code
```python
python main.py
```
View Results:

The final merged data will be stored in final_data.csv.
Analysis results and visualizations will be saved in the AnalysisOutputResults directory.
Unit Testing
Run the unit tests using:

```bash
pytest
pandas
pymysql
jsonschema
pytest (for testing)
```
### Contributing
##### Feel free to contribute by opening issues or submitting pull requests.

### Area of improvement

1- Any third party software / tool like Tableau or power BI is good for data visualization. 

2- Data analysis can be done using plain sql query. We can create stored procedures and analysis.py can be further enhanced just to call these stored procedures when ever is required. 

3- Data drift has been mostly handled with SCHEMA checks but needs further modification to validate the range of each fields.
