class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        open(self.__file_name, 'a').close()

    def get_products(self):
        with open(self.__file_name, 'r') as f:
            return f.read()

    def add(self, *products):
        with open(self.__file_name, 'r') as f:
            existing_products = f.read().splitlines()

        existing_name = {line.split(', ')[0] for line in existing_products}

        with open(self.__file_name, 'a') as f:
            for product in products:
                if product.name in existing_name:
                    print(f'{product.name} уже есть в магазине')
                else:
                    f.write(str(product) + '\n')
    #  if __name__ == '__main__':


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)
print(s1.get_products())
