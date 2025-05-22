print('number2')
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return self.radius * 2
    def area(self):
        return math.pi * self.radius ** 2
circle = Circle(5)
print(f"Радиус: {circle.radius}")
print(f"Диаметр: {circle.diameter}")
print(f"Площадь: {circle.area()}")

print('number2')

class Employee:
    def __init__(self):
        self._employees = []
    def add_employee(self, name, salary):
        self._employees.append({"name": name, "salary": salary})
    @property
    def average_salary(self):
        total_salary = sum(emp["salary"] for emp in self._employees)
        return total_salary / len(self._employees) if self._employees else 0
    def get_sorted_employees(self):
        return sorted(self._employees, key=lambda emp: emp["salary"])
if __name__ == "__main__":
    company = Employee()
    company.add_employee("Иван Петров", 50000)
    company.add_employee("Анна Смирнова", 70000)
    company.add_employee("Сергей Иванов", 60000)
    print(f"Средняя зарплата: {company.average_salary}")
    sorted_employees = company.get_sorted_employees()
    print("Сотрудники, отсортированные по зарплате:")
    for emp in sorted_employees:
        print(f"{emp['name']}: {emp['salary']}")