import ipdb

class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if (hasattr(self, "name")):
            AttributeError
        elif isinstance(new_name, str) and len(new_name) >= 3:
            self._name = new_name
        else:
            raise Exception
    
    def orders(self):
        return [coffee for coffee in Order.all if coffee.coffee == self]
    
    def customers(self):
        uniq_customer = []
        for customer in self.orders():
            if not customer.customer in uniq_customer: 
                uniq_customer.append(customer.customer)
        return uniq_customer
    
    def num_orders(self):
        coffees = [customer.coffee for customer in self.orders()]
        return coffees.count(self)
        
    
    def average_price(self):
        total_price = sum([order.price for order in self.orders()])
        avg_price = total_price / self.num_orders()
        return avg_price

    def __repr__(self):
       return f'<name = {self.name}>'

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15:
            self._name = new_name

    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        uniq_coffee = []
        for customer in self.orders():
            if not customer.coffee in uniq_coffee:
                uniq_coffee.append(customer.coffee)
        return uniq_coffee
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    def __repr__(self):
       return f'<customer_name = {self.name}>'  
    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if (hasattr(self, "price")):
            # ipdb.set_trace()
            AttributeError
        elif isinstance(new_price, float) and 1.0 <= new_price <= 10.0:
            self._price = new_price
        else:
            raise Exception
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, new_customer):
        if isinstance(new_customer, Customer):
            self._customer = new_customer
        else: 
            raise Exception
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, new_coffee):
        if isinstance(new_coffee, Coffee):
            self._coffee = new_coffee
        else:
            raise Exception
        

    def __repr__(self):
       return f'<customer = {self.customer} coffee = {self.coffee} price = {self.price}>'    


# coffee = Coffee("Mocha")
# customer = Customer('Steve')
# order_1 = Order(customer, coffee, 2.0)
# order_1.price = 3.0