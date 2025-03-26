import numpy as np
import matplotlib.pyplot as plt

class Derivative:
    def __init__(self):
        self.h = 1e-5
    def __get__(self, instance, owner):
        return self
    def __call__(self, x):
        f_x_plus_h = x + self.h
        f_x_minus_h = x - self.h
        return (instance(f_x_plus_h) - instance(f_x_minus_h)) / (2 * self.h)

class ExponentialFunction:
    def __init__(self, a):
        self.a = a
        self.derivative = Derivative()
    def __call__(self, x):
        return self.a * np.exp(x)

    def plot(self):
        x_values = np.linspace(-2, 2, 400)
        f_values = self(x_values)  # Значения функции
        df_values = self.derivative(x_values)  # Значения производной


        plt.figure(figsize=(10, 6))
        plt.plot(x_values, f_values, label='f(x) = a * e^x', color='blue')
        plt.plot(x_values, df_values, label="f'(x) ≈ Derivative", color='red', linestyle='dashed')
        plt.title('Графики функции и её производной')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
        plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
        plt.legend()
        plt.grid()
        plt.show()
exp_func = ExponentialFunction(a=2)
print(exp_func(0))
print(exp_func.derivative(0))
exp_func.plot()