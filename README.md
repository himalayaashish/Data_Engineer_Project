## Hello World! <img alt="wave" src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="30px">

<div align="center"> 🚀 Welcome to my git repo :BreadcrumbsData_Engineer_Project:</div>

### Data_Engineer_Project 
<img src="https://github.com/himalayaashish/Data_Engineer_Project/blob/main/i1234.jpg?raw=true" alt="Lumbar Detection" width="500"/>


#### Data Pipeline for AIQ Data Engineer Assignment
###### This data pipeline processes sales data, user data, and weather data to generate actionable insights and visualizations. The pipeline is designed to be executed through the main.py script, which orchestrates the entire flow from data extraction to analysis.

###### I utilized advanced data engineering techniques, integrating multiple data sources like sales, user, and weather data to build a seamless pipeline. The pipeline automates data validation, transformation, and analysis, ensuring accurate insights and efficient processing.

###### This project showcases how combining data pipeline automation with real-time data processing can drive actionable insights and improve decision-making.

---

### Languages and Tools 

### Languages
  **Python**:
  ![Langchain](https://img.shields.io/badge/LangChain-ffffff?logo=langchain&logoColor=green)
  ![PyPdf](https://img.shields.io/badge/PyPdf-red)
  ![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model-blue)
  ![Llama](https://img.shields.io/badge/Llama-3.2-yellow?style=flat-square&logo=meta&logoColor=white)
  ![ChromaDB](https://img.shields.io/badge/ChromaDB-blue)
  ![Python](https://img.shields.io/badge/-Python-black?style=flat&logo=python)
  ![Keras](https://img.shields.io/badge/-Keras-D00000?style=flat&logo=Keras)
  ![Tensorflow](https://img.shields.io/badge/-Tensorflow-gray?style=flat&logo=tensorflow)
  ![PyTorch](https://img.shields.io/badge/-PyTorch-EE4C2C?style=flat&logo=PyTorch&logoColor=white)
  

  **JavaScript**: 
  ![JavaScript](https://img.shields.io/badge/-JavaScript-black?style=flat&logo=javascript)
  ![HTML5](https://img.shields.io/badge/-HTML5-E34F26?style=flat&logo=html5&logoColor=white) 
  ![CSS3](https://img.shields.io/badge/-CSS3-1572B6?style=flat&logo=css3) 
  ![Bootstrap](https://img.shields.io/badge/-Bootstrap-purple?style=flat&logo=bootstrap) 

  **SQL:**
  ![SQL](https://img.shields.io/badge/-SQL-orange?style=flat&logo=sql)
  ![MySQL](https://img.shields.io/badge/-MySQL-lightgray?style=flat&logo=mysql)
  ![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-blue?style=flat&logo=postgresql)

### Tools

**Software Development:**
![Pycharm IDE](https://img.shields.io/badge/PyCharm-000000?logo=PyCharm&logoColor=white)
![IntelliJ IDEA](https://img.shields.io/badge/-red?style=flat&logo=IntelliJ-IDEA&logoColor=white)
![Docker](https://img.shields.io/badge/-2496ED?style=flat&logo=Docker&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-gray?style=flat&logo=jenkins) 
![XML](https://img.shields.io/badge/-XML-orange?style=flat&logo=xml)
![JSON](https://img.shields.io/badge/-JSON-lightgray?style=flat&logo=json)
![Vim](https://img.shields.io/badge/-019733?style=flat&logo=Vim&logoColor=white)

**SDLC:**
![Agile](https://img.shields.io/badge/Agile-blue?style=flat&logo=Agile&logoColor=white) ![Scrum](https://img.shields.io/badge/Scrum-green?style=flat&logo=Scrum&logoColor=white) ![Kanban](https://img.shields.io/badge/Kanban-red?style=flat&logo=Kanban&logoColor=white)

**Software Engineering:**
[![Jira](https://img.shields.io/badge/-Jira-0052CC?style=flat&logo=jira&logoColor=white&link=https://github.com/Quananhle)](https://github.com/Quananhle)
[![Travis](https://img.shields.io/badge/-Travis-red?style=flat&logo=travis&logoColor=white&link=https://github.com/Quananhle)](https://github.com/Quananhle) 

**Version Control:**
![Bitbucket](https://img.shields.io/badge/-Bitbucket-blue?style=flat&logo=bitbucket)
![Git](https://img.shields.io/badge/-Git-black?style=flat&logo=git) 
![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat&logo=github)

---

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

### Data Pipeline for AIQ Data Engineer Assignment
#### Overview
This data pipeline processes sales data, user data, and weather data to generate insights and visualizations. It is designed to be run using the main.py script, which orchestrates the entire pipeline.

##### Note 1 - Create a table "sales" in mysql and load "AIQ - Data Engineer Assignment - Sales data.csv" using Import wizard.
##### Note 2 - Edit config.py with your credientials and information.

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

---


<!--START_SECTION:waka-->
<div style="display: flex; justify-content: space-between; align-items: center;">
  <img src="http://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=himalayaashish&theme=apprentice" alt="Profile Details" />
  <img src="http://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=himalayaashish&theme=apprentice&utcOffset=8" alt="Productive time" />
  <img align="left" src="http://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=himalayaashish&theme=apprentice" alt="Repos per language" />
  <img align="left" src="http://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=himalayaashish&theme=apprentice" alt="Most commit language" />
  <img align="center" src="http://github-profile-summary-cards.vercel.app/api/cards/stats?username=himalayaashish&theme=apprentice" alt="Stats" />
</div>


---
<div align="center">
  <h3 align="center">Connect with me<img align="center" src="https://github.com/rajput2107/rajput2107/blob/master/Assets/Handshake.gif" height="33px" /></h3> 
</div>
<p align="center">
 <a href="https://www.linkedin.com/in/himalayaashish/" target="blank">
  <img align="center" alt="Pramod's LinkedIn" width="30px" src="https://www.vectorlogo.zone/logos/linkedin/linkedin-icon.svg" /> &nbsp; &nbsp;
 </a>
 <a href="https://www.kaggle.com/himalayaashish" target="blank">
  <img align="center" alt="Gumalaya's Kaggle" width="60px" src="https://www.vectorlogo.zone/logos/kaggle/kaggle-ar21.svg" /> &nbsp; &nbsp;
 </a>
 <a href="https://twitter.com/himalayaashish" target="blank">
  <img align="center" alt="Pramod's Twitter" width="30px" src="https://www.vectorlogo.zone/logos/twitter/twitter-official.svg" /> &nbsp; &nbsp;
 </a>
 <a href="https://medium.com/@himalayaashish" target="blank">
  <img align="center" alt="Himalaya's Twitter" width="30px" src="https://www.vectorlogo.zone/logos/medium/medium-tile.svg" />
 </a>
