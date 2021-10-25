# Create a function which takes as input two dicts with structure mentioned\
# above, then computes and returns the total price of stock.


stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def total_price(stock: dict, prices: dict):
    total = 0
    for position in stock:
        if position in stock and position in prices:
            total = total + stock.get(position) * prices.get(position)
    return (total)

print(f"Загальна вартість товару: {total_price(stock, prices)} у.о.")