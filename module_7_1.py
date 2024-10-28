# Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.
# Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables')
# и обладать следующими свойствами:
# Атрибут name - название продукта (строка).
# Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
# Атрибут category - категория товара (строка).

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    """
    Метод __str__ возвращает строку в формате '<название>, <вес>, <категория>'.
    Все данные в строке разделены запятой с пробелами.
    """

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

    """
    Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
    Инкапсулированный атрибут __file_name = 'products.txt'.
    """
class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'

    """
    Метод get_products(self) считывает всю информацию из файла __file_name, закрывает его
    и возвращает единую строку со всеми товарами из файла __file_name.
    """
    def get_products(self):
            with open(self.__file_name, 'r') as file:   # считывает информацию и закрывает файл
                return file.read()


    """
    Метод add(self, *products) принимает неограниченное количество объектов класса Product.
    Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
    Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине'.
    """

    def add(self, *products):
        stock_products = self.get_products().splitlines()
        stock_product_names = {product.split(', ')[0] for product in stock_products}

        for product in products:
            if product.name in stock_product_names:
                print(f"Продукт {product.name} уже есть в магазине")
            else:
                with open(self.__file_name, 'a') as file:       # считывает информацию и закрывает файл
                    file.write(f"{product}\n")                  # Запись продукта в файл


# Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

# Вывод на консоль:
# Первый запуск:
# Spaghetti, 3.4, Groceries
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables

# Второй запуск:
# Spaghetti, 3.4, Groceries
# Продукт Potato, 50.5, Vegetables уже есть в магазине
# Продукт Spaghetti, 3.4, Groceries уже есть в магазине
# Продукт Potato, 5.5, Vegetables уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables

# Как выглядит файл после запусков:
# products.txt
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables
