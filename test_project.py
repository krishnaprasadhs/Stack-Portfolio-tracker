from project import track_stock_portfolio, calculate_portfolio_value, list_added_stocks, edit_existing_stock, delete_stock

def test_track_stock_portfolio():
    stock_portfolio = []
    track_stock_portfolio(stock_portfolio, "AAPL", 10, "2023-01-01", "2023-01-10")
    assert len(stock_portfolio) == 1
    assert stock_portfolio[0]["symbol"] == "AAPL"

def test_calculate_portfolio_value():
    stock_portfolio = [
        {"symbol": "AAPL", "shares": 10, "start_date": "2023-01-01", "end_date": "2023-01-10", "total_investment": 1500.0},
        {"symbol": "GOOGL", "shares": 5, "start_date": "2023-01-01", "end_date": "2023-01-10", "total_investment": 2500.0}
    ]
    portfolio_value = calculate_portfolio_value(stock_portfolio)
    assert portfolio_value == 4000.0


def test_delete_stock():
    stock_portfolio = [
        {"symbol": "AAPL", "shares": 10, "start_date": "2023-01-01", "end_date": "2023-01-10", "total_investment": 1500.0},
        {"symbol": "GOOGL", "shares": 5, "start_date": "2023-01-01", "end_date": "2023-01-10", "total_investment": 2500.0}
    ]
    delete_stock(stock_portfolio, 1)
    assert len(stock_portfolio) == 1
    assert stock_portfolio[0]["symbol"] == "GOOGL"