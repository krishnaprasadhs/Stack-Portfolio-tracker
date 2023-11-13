# Stock Portfolio Tracker
### Video Demo: [click here ](https://youtu.be/85OTIf7gJhs)

#### Description:

The Stock Portfolio Tracker is a versatile Python project designed to empower users in monitoring and managing their stock investments. This financial tool offers a comprehensive set of features that enable users to efficiently track their stock portfolio, retrieve historical stock data, calculate investment values, and assess the total value of their stock holdings. Whether you're a novice or an experienced investor, this application provides valuable insights and aids in making informed financial decisions.

## Key Features

### Fetching Stock Data

- Users can easily access historical stock data by providing a stock symbol, start date, and end date.
- The application leverages the `yfinance` library to fetch accurate and up-to-date stock information from Yahoo Finance, ensuring reliability and data integrity.

### Calculating Investment Value

- For individual stocks in the portfolio, users can calculate the total investment value by specifying the number of shares they own.
- The application retrieves the latest stock price, allowing users to make informed investment decisions by understanding the current value of their holdings.

### Tracking Stocks in Portfolio

- Users can maintain a comprehensive record of multiple stocks in their portfolio.
- For each stock, they input the stock symbol, the quantity of shares owned, the start date, and the end date. This data is used to calculate and store the total investment value for each stock.

### Calculating Total Portfolio Value

- The application enables users to assess the cumulative value of their entire stock portfolio.
- By summing up the total investment values of all the stocks in the portfolio, users gain a holistic view of the financial performance of their investments.

## The project consists of two main files:

- `project.py`: This file contains the core functionality of the Stock Portfolio Tracker. It includes functions for fetching stock data, calculating investment values, tracking stocks in the portfolio, editing the socks and calculating the total portfolio value. The main function allows users to interact with the application via a console-based menu.

- `test_project.py`: This file includes unit tests for the core functions of the Stock Portfolio Tracker. The tests are implemented using the `pytest` framework and help ensure the correctness of the project's functionality.

## Installation & Use

1. **Clone the Code**:
   - Begin by cloning the project's source code from the repository.

2. **Install Required Libraries**:
   - Navigate to the project directory and execute the command `pip install -r requirements.txt` to install the necessary Python libraries, including `yfinance`, `pytest`, `pyfiglet`, and `tabulate`.

3. **Running the Application**:
   - Execute `python3 project.py` to launch the Stock Portfolio Tracker.
   - Interact with the application using the intuitive console-based menu.
   - Follow on-screen instructions to utilize the project's functionalities effectively.

## Design Choices

- **Data Retrieval with yfinance**:
  - The project utilizes the `yfinance` library for retrieving stock data due to its simplicity and accuracy in accessing historical stock prices from Yahoo Finance.

- **User-Friendly Interface**:
  - The menu-driven interface in the main function ensures a user-friendly and intuitive way to interact with the application. Users can effortlessly navigate and perform tasks.

- **Code Quality and Style**:
  - The project adheres to the PEP 8 style guidelines for code formatting and structure, ensuring readability and maintainability.


Feel free to watch the video demo to see the Stock Portfolio Tracker in action!

## Overview:
```
project/ $ python project.py
+-+-+-+-+-+
|C|S|5|0|P|
+-+-+-+-+-+
+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+ +-+
|K|R|I|S|H|N|A| |P|R|A|S|A|D|H| |S|
+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+ +-+
+-+-+-+-+-+ +-+-+-+-+-+-+-+
|F|i|n|a|l| |P|r|o|j|e|c|t|
+-+-+-+-+-+ +-+-+-+-+-+-+-+


Options:
1. Track a Stock
2. Calculate Portfolio Value
3. List Added Stocks
4. Edit an Existing Stock
5. Delete a Stock
6. Quit
Enter the option number: 1
Enter the stock symbol: AAPL
Enter the number of shares: 9
Enter the start date (yyyy-mm-dd): 2000-03-01
Enter the end date (yyyy-mm-dd): 2023-09-07
Stock added to the portfolio successfully!

Options:
1. Track a Stock
2. Calculate Portfolio Value
3. List Added Stocks
4. Edit an Existing Stock
5. Delete a Stock
6. Quit
Enter the option number: 1
Enter the stock symbol: MSFT
Enter the number of shares: 4
Enter the start date (yyyy-mm-dd): 2013-09-05
Enter the end date (yyyy-mm-dd): 2019-01-01
Stock added to the portfolio successfully!

Options:
1. Track a Stock
2. Calculate Portfolio Value
3. List Added Stocks
4. Edit an Existing Stock
5. Delete a Stock
6. Quit
Enter the option number: 1
Enter the stock symbol: AMZN
Enter the number of shares: 10
Enter the start date (yyyy-mm-dd): 2001-01-01
Enter the end date (yyyy-mm-dd): 2019-09-09
Stock added to the portfolio successfully!

Options:
1. Track a Stock
2. Calculate Portfolio Value
3. List Added Stocks
4. Edit an Existing Stock
5. Delete a Stock
6. Quit
Enter the option number: 2
Total portfolio value: $120.44

Options:
1. Track a Stock
2. Calculate Portfolio Value
3. List Added Stocks
4. Edit an Existing Stock
5. Delete a Stock
6. Quit
Enter the option number: 3
+--------------+----------+----------+--------------+------------+--------------------+
|   Series No. | Symbol   |   Shares | Start Date   | End Date   | Total Investment   |
+==============+==========+==========+==============+============+====================+
|            1 | AAPL     |        9 | 2000-03-01   | 2023-09-07 | $8.89              |
+--------------+----------+----------+--------------+------------+--------------------+
|            2 | MSFT     |        4 | 2013-09-05   | 2019-01-01 | $104.61            |
+--------------+----------+----------+--------------+------------+--------------------+
|            3 | AMZN     |       10 | 2001-01-01   | 2019-09-09 | $6.94              |
+--------------+----------+----------+--------------+------------+--------------------+

Options:
1. Track a Stock
2. Calculate Portfolio Value
3. List Added Stocks
4. Edit an Existing Stock
5. Delete a Stock
6. Quit
Enter the option number: 4
Enter the series number of the stock you want to edit: 3
Enter the new number of shares: 20
Enter the new start date (yyyy-mm-dd): 2001-01-01
Enter the new end date (yyyy-mm-dd): 2019-09-09
Stock edited successfully!

Options:
1. Track a Stock
2. Calculate Portfolio Value
3. List Added Stocks
4. Edit an Existing Stock
5. Delete a Stock
6. Quit
Enter the option number: 3
+--------------+----------+----------+--------------+------------+--------------------+
|   Series No. | Symbol   |   Shares | Start Date   | End Date   | Total Investment   |
+==============+==========+==========+==============+============+====================+
|            1 | AAPL     |        9 | 2000-03-01   | 2023-09-07 | $8.89              |
+--------------+----------+----------+--------------+------------+--------------------+
|            2 | MSFT     |        4 | 2013-09-05   | 2019-01-01 | $104.61            |
+--------------+----------+----------+--------------+------------+--------------------+
|            3 | AMZN     |       20 | 2001-01-01   | 2019-09-09 | $0.69              |
+--------------+----------+----------+--------------+------------+--------------------+

Options:
1. Track a Stock
2. Calculate Portfolio Value
3. List Added Stocks
4. Edit an Existing Stock
5. Delete a Stock
6. Quit
Enter the option number: 5
Enter the series number of the stock you want to delete: 3
Stock deleted successfully!

Options:
1. Track a Stock
2. Calculate Portfolio Value
3. List Added Stocks
4. Edit an Existing Stock
5. Delete a Stock
6. Quit
Enter the option number: 3
+--------------+----------+----------+--------------+------------+--------------------+
|   Series No. | Symbol   |   Shares | Start Date   | End Date   | Total Investment   |
+==============+==========+==========+==============+============+====================+
|            1 | AAPL     |        9 | 2000-03-01   | 2023-09-07 | $8.89              |
+--------------+----------+----------+--------------+------------+--------------------+
|            2 | MSFT     |        4 | 2013-09-05   | 2019-01-01 | $104.61            |
+--------------+----------+----------+--------------+------------+--------------------+

Options:
1. Track a Stock
2. Calculate Portfolio Value
3. List Added Stocks
4. Edit an Existing Stock
5. Delete a Stock
6. Quit
Enter the option number: 6
project/ $
```
---

## Certification:
![CS50P](https://github.com/krishnaprasadhs/Stack-Portfolio-tracker/assets/74102278/24276277-aad6-4916-b296-d2cf8e0a56b9)

