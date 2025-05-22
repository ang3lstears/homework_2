print('number2')
import timeit
import sys

class NormalPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
class SlotPoint:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
def create_points():
    normal_points = [NormalPoint(i, i) for i in range(1000)]
    slot_points = [SlotPoint(i, i) for i in range(1000)]
    return normal_points, slot_points
def measure_time(points, class_name):
    time_taken = timeit.timeit(
        'point.move(1, 1)',
        setup=f'from __main__ import {class_name}; point = {class_name}(0, 0)',
        number=1000000
    )
    return time_taken

normal_points, slot_points = create_points()
normal_point_time = measure_time(normal_points, 'NormalPoint')
slot_point_time = measure_time(slot_points, 'SlotPoint')
normal_point_size = sys.getsizeof(normal_points[0]) * 1000
slot_point_size = sys.getsizeof(slot_points[0]) * 1000
print(f"Время выполнения метода move для NormalPoint: {normal_point_time:.6f} секунд")
print(f"Время выполнения метода move для SlotPoint: {slot_point_time:.6f} секунд")
print(f"Размер памяти для NormalPoint (1000 экземпляров): {normal_point_size} байт")
print(f"Размер памяти для SlotPoint (1000 экземпляров): {slot_point_size} байт")

print('number 3')

class Student:
    __slots__ = ['name', 'age', 'grade']
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
def calculate_average_grade(students):
    total_grade = 0
    for student in students:
        total_grade += student.grade
    average_grade = total_grade / len(students) if students else 0
    return average_grade
students = [
    Student("Alice", 20, 5),
    Student("Sanya", 21, 2.4),
    Student("Denis", 22, 4.3),
    Student("Diana", 20, 3.7)
]
average = calculate_average_grade(students)
print(f"Средняя оценка студентов: {average:.2f}")

print('number4')

class Product:
    __slots__ = ['name', 'price', 'quantity']
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
def get_products_above_threshold(products, threshold_price):
    above_threshold = []
    for product in products.values():
        if product.price > threshold_price:
            above_threshold.append(product.name)
    return above_threshold

inventory = {
    "Apple": Product("Apple", 1.2, 50),
    "Banana": Product("Banana", 0.5, 100),
    "Cherry": Product("Cherry", 2.0, 30),
    "Date": Product("Date", 3.0, 20),
    "Elderberry": Product("Elderberry", 1.5, 15)
}

threshold = 1.0
expensive_products = get_products_above_threshold(inventory, threshold)
print(f"Товары с ценой выше {threshold}: {', '.join(expensive_products)}")