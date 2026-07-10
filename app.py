from flask import Flask, render_template, request, redirect, url_style
import csv

app = Flask(__name__)

STOCK_PRICES = {
    "AAPL": 180.00, "TSLA": 250.00, "GOOGL": 175.00, "MSFT": 420.00, "AMZN": 185.00
}

# Temporary database in memory
user_portfolio = {}

@app.route('/')
def index():
    grand_total = sum(user_portfolio.get(ticker, 0) * price for ticker, price in STOCK_PRICES.items())
    return render_template('index.html', stock_prices=STOCK_PRICES, portfolio=user_portfolio, grand_total=grand_total)

@app.route('/add', methods=['POST'])
def add_stock():
    ticker = request.form.get('ticker').upper()
    try:
        quantity = int(request.form.get('quantity', 0))
    except ValueError:
        return redirect('/')

    if ticker in STOCK_PRICES and quantity > 0:
        user_portfolio[ticker] = user_portfolio.get(ticker, 0) + quantity
    return redirect('/')

@app.route('/clear')
def clear_portfolio():
    user_portfolio.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
