def buySell(price):
    profit=0
    max_profit=0
    min_price=price[0]
    for i in range(len(price)):
        if price[i]<min_price:
            min_price=price[i]
        else:
            profit=price[i]-min_price
            max_profit=max(profit,max_profit)

    return max_profit

print(buySell([2,2,1,4,5]))