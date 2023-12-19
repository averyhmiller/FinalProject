import statistics
f = open("APPL.txt", "r")
listItems = f.read().splitlines()
prices=list(map(float,listItems))

def buy_and_sell(prices):
    max_profit_val, current_max_val=0, 0
    for price in reversed(prices):
        current_max_val=max(current_max_val, price)
        potential_profit=current_max_val - price
        max_profit_val=max(potential_profit, max_profit_val)
    return max_profit_val

print(buy_and_sell(prices))