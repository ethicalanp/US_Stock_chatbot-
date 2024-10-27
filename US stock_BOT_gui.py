import tkinter as tk
import requests

# Function to get stock price (same as before)
def get_stock_price(symbol):
    API_KEY = "0VQPWGPHKTXU37JR"
    BASE_URL = "https://www.alphavantage.co/query?"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "Time Series (Daily)" in data:
        latest_data = next(iter(data['Time Series (Daily)']))
        price = data['Time Series (Daily)'][latest_data]['4. close']
        return f'Latest price for {symbol} on {latest_data} is ${price}.'
    else:
        return "Sorry, I couldn't fetch the stock price. Please check the symbol and try again."


def on_submit():
    user_input = entry.get()
    if user_input.lower().startswith(""):
        symbol = user_input.split()[-1].upper()  # Extract symbol and make it uppercase
        response = get_stock_price(symbol)
    else:
        response = "Please ask for the stock price by saying 'stock price of ___'."
    
    output_label.config(text=response)

#gui
root = tk.Tk()
root.title("Stock Market Chatbot")

entry = tk.Entry(root, width=50)
entry.pack(pady=20)

submit_button = tk.Button(root, text="Get Price", command=on_submit)
submit_button.pack(pady=10)

output_label = tk.Label(root, text="", wraplength=400)
output_label.pack(pady=20)

root.mainloop()
