'''function return max,low and avarage from prices list
return in nice format new line and index'''


def mullt_return(price):
    high = max(price)
    low = min(price)
    average= (sum(price) / len(price))
    return high, low, average

prices = [12.34, 44.35, 10.36, 64.50]

response = mullt_return(prices)

# lame resppnse
#print(response)

print(f' max: {response[0]} \n min: {response[1]} \n average: {response[2]}')
