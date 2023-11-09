import yfinance as yf
from tabulate import tabulate
import pyfiglet

print(pyfiglet.figlet_format("CS50P \nKRISHNA PRASADH S \nFinal Project", font= "digital"))

def stock_data(symbol, start_date, end_date):
    stock_data = yf.Ticker(symbol).history(period="1d", start=start_date, end=end_date)
    if not stock_data.empty:
        return stock_data["Close"].values[0]
    else:
        return None

def track_stock_portfolio(stock_portfolio, symbol, shares, start_date, end_date):
    stock_value = stock_data(symbol, start_date, end_date)

    if stock_value is not None:
        total_investment = stock_value * shares
        stock_portfolio.append({
            "symbol": symbol,
            "shares": shares,
            "start_date": start_date,
            "end_date": end_date,
            "total_investment": total_investment
        })
    else:
        print(f"Failed to track {symbol}. Please check the symbol or date range.")

def calculate_portfolio_value(stock_portfolio):
    total_portfolio_value = sum(stock["total_investment"] for stock in stock_portfolio)
    return total_portfolio_value

def list_added_stocks(stock_portfolio):
    if stock_portfolio:
        headers = ["Series No.", "Symbol", "Shares", "Start Date", "End Date", "Total Investment"]
        data = [(i + 1, stock['symbol'], stock['shares'], stock['start_date'], stock['end_date'], f"${stock['total_investment']:.2f}") for i, stock in enumerate(stock_portfolio)]
        print(tabulate(data, headers, tablefmt="grid"))
    else:
        print("No stocks have been added yet.")

def edit_existing_stock(stock_portfolio, series_number):
    if 1 <= series_number <= len(stock_portfolio):
        stock = stock_portfolio[series_number - 1]
        shares = float(input("Enter the new number of shares: "))
        start_date = input("Enter the new start date (yyyy-mm-dd): ")
        end_date = input("Enter the new end date (yyyy-mm-dd): ")

        stock['shares'] = shares
        stock['start_date'] = start_date
        stock['end_date'] = end_date
        stock['total_investment'] = stock_data(stock['symbol'], start_date, end_date)

        print("Stock edited successfully!")
    else:
        print("Invalid series number. Please enter a valid series number.")

def delete_stock(stock_portfolio, series_number):
    if 1 <= series_number <= len(stock_portfolio):
        stock_portfolio.pop(series_number - 1)
        print("Stock deleted successfully!")
    else:
        print("Invalid series number. Please enter a valid series number.")

def main():
    stock_portfolio = []

    while True:
        print("\nOptions:")
        print("1. Track a Stock")
        print("2. Calculate Portfolio Value")
        print("3. List Added Stocks")
        print("4. Edit an Existing Stock")
        print("5. Delete a Stock")
        print("6. Quit")
        choice = input("Enter the option number: ")

        if choice == '1':
            symbol = input("Enter the stock symbol: ")
            shares = float(input("Enter the number of shares: "))
            start_date = input("Enter the start date (yyyy-mm-dd): ")
            end_date = input("Enter the end date (yyyy-mm-dd): ")

            track_stock_portfolio(stock_portfolio, symbol, shares, start_date, end_date)
            print("Stock added to the portfolio successfully!")

        elif choice == '2':
            portfolio_value = calculate_portfolio_value(stock_portfolio)
            print(f"Total portfolio value: ${portfolio_value:.2f}")

        elif choice == '3':
            list_added_stocks(stock_portfolio)

        elif choice == '4':
            series_number = int(input("Enter the series number of the stock you want to edit: "))
            edit_existing_stock(stock_portfolio, series_number)

        elif choice == '5':
            series_number = int(input("Enter the series number of the stock you want to delete: "))
            delete_stock(stock_portfolio, series_number)

        elif choice == '6':
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()