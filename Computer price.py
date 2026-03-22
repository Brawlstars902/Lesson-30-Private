class computer:

    def __init__(self):
        self.__maxprice=500

    def sell(self):
        print('Selling price is {}'.format(self.__maxprice))

    def seMaxPrice(self, price):
        self.__maxprice=price

c=computer()
c.sell()

c.__maxprice=1000
c.sell()

c.seMaxPrice(1000)
c.sell
