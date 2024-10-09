#mortgage repayment calculator

def mortgage(total, payment, interest):
    interest = (interest / 12) / 100
    month = 0
    paid = 0
    total_interest = 0
    if payment > (total * interest):
        while total >= 0:
            total = (total * interest) + total
            total_interest = (total * interest) + total_interest
            total = total - payment
            paid = paid + payment
            month += 1
        year = month / 12
    else:
        print(f'The loan will never be paid off')
        year = "error"
        paid ="error"
        total_interest = "error"
    return year, paid, total_interest

price = 100000
interest = 7
payment = 23

response = mortgage(price, payment, interest)

print(f' Repayment years: {response[0]} \n Total Paid: {response[1]} \n Interest paid: {response[2]}')