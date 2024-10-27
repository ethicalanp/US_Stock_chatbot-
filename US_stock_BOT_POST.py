from flask import Flask , request, jsonify
import requests
import os 

app = Flask(__name__)

API_KEY = "0VQPWGPHKTXU37JR"
BASE_URL = "https://www.alphavantage.co/query?"

def get_stock_price(symbol):
    params = {
        "function":"TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey":API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "Time Series (Daily)" in data:
        latest_data = next(iter(data['Time Series (Daily)']))
        price = data['Time Series (Daily)'][latest_data]['4. close']
        return f'Latest price for {symbol} on {latest_data} is $(price).'
    else:
        return "Sorry, I couldn't fetch the stock price. Please check the symbol and try again."
    

@app.route('/chat', methods = ['POST'])
def chat():
    user_input = request.json.get("message")

    if user_input.lower().startswith(""):
        symbol = user_input.split()[-1]
        response = get_stock_price(symbol)
    else:
        response = "Please ask for the stock price by saying 'stock price of ___"

    return jsonify({'response':response})

if __name__ =='__main__':
    app.run(debug=True)