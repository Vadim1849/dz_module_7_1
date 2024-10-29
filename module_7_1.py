class Product:
    def __init__(self, name, weight, category):
        # Атрибут name - название продукта (строка).
        self.name = name
        # Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
        self.weight = weight
        # Атрибут category - категория товара (строка).
        self.category = category

    def __str__(self):
        # Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
        # Все данные в строке разделены запятой с пробелами.
        return f'{self.name}, {self.weight}, {self.category}'


# Класс Shop
class Shop:
    # Инкапсулированный атрибут __file_name = 'products.txt'.
    __file_name = 'products.txt'

    def get_products(self):
        # Метод get_products(self), который считывает всю информацию из файла __file_name,
        # закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return 'Ошибка «Файл не найден».'

    def add(self, *products):
        # Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
        existing_products = self.get_products().split('\n')
        existing_product_names = {line.split(', ')[0] for line in existing_products if line}

        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name in existing_product_names:
                    print(f'Продукт {product.name} уже есть в магазине')
                else:
                    file.write(str(product) + '\n')
                    existing_product_names.add(product.name)


# Пример работы программы
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())