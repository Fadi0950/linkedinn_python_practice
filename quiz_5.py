"""
What code should come instead of the ???
placeholders to have a function that takes the amount of local currency and a varying number of exchange rates,
 and prints the value of the currency at each provided exchange rate?
"""
def calc(currency,*rates):
    for i in rates:
        print(currency*i)
currency=174
rates=20
calc(currency,rates)
