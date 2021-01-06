import requests

"""class CurrencyConverter():
    def __init__(self,url):
        self.data= requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        # first convert it into USD if it is not in USD.
        # because our base currency is USD
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

            # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount
converter = CurrencyConverter(url)
print(converter.convert('INR','USD',100))"""


def converter(from_curr, to_curr, amt):
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    data = requests.get(url).json()
    currencies = data['rates']
    from_currency = from_curr
    to_currency = to_curr
    amount = amt

    if from_currency != 'USD':
        amount = amount / currencies[from_currency]
    amount = round(amount * currencies[to_currency], 4)
    return amount

#print (type(converter('USD','JPY',100)))
