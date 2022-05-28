class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'The product is {self.name},price is {self.price}'

    def __repr__(self):
        return f'<{type(self)},the product is {self.name},price is {self.price}>'

    def __add__(self, other):
        if isinstance(other, Product):
            return [self, other]
        elif isinstance(other, str):
            str_ = other + self.name
            self.name = str_
        elif isinstance(other, int):
            self.price += other

class ShoppingCart:
    def __init__(self, products):
        self.products = products

    def __str__(self):
        return f'There are {len(self.products)} kind of products!!!'

    def __repr__(self):
        count = 1
        str_ = ''
        if not self.products:
            return 'No products in the list!!!'
        else:
            for product in self.products:
                if  isinstance(product,Product) and len(self.products) > count:
                    str_ = str_ + product.name + ':$' + str(product.price) + ','
                elif isinstance(product,Product) and len(self.products) == count:
                    str_ = str_ + product.name + ':$' + str(product.price)
                count += 1
        return f'{type(self)}There are {len(self.products)} kind of products({str_})!!!'

    def __getitem__(self, key):
        if not self.products:
            return 'No products in the list!!!'
        else:
            if key > len(self.products) - 1 :
                return 'Index error!!!'
            else:
                return self.products[key]

p1 = Product(name = '珍珠奶茶', price = 55)
p2 = Product(name = '紅茶拿鐵', price = 60)
p3 = Product(name = '四季春茶', price = 30)
s1 = ShoppingCart([p1, p2, p3])
print(s1)
print(repr(s1))
print(s1[0])
p1 + '白玉'
print(p1 + p2)
print(p1)
