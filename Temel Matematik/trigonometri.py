import math
import matplotlib.pyplot as plt
import numpy as np

def solve_trig_equation(equation):
    if equation.startswith("sin"):
        angle = math.degrees(math.asin(float(equation.split('=')[1])))
        return angle
    elif equation.startswith("cos"):
        angle = math.degrees(math.acos(float(equation.split('=')[1])))
        return angle
    elif equation.startswith("tan"):
        angle = math.degrees(math.atan(float(equation.split('=')[1])))
        return angle
    else:
        return "Bu denklem desteklenmiyor."


def solve_trig_inequality(inequality):
    if inequality.startswith("cos"):
        return "-90 < x < 90"
    else:
        return "Bu eşitsizlik desteklenmiyor."


# Trigonometrik Fonksiyonların Grafikleri ve Özellikleri
def plot_trig_function(function_name):
    x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    if function_name == "sin":
        y = np.sin(x)
    elif function_name == "cos":
        y = np.cos(x)
    elif function_name == "tan":
        y = np.tan(x)
    else:
        return "Bu fonksiyon desteklenmiyor."

    plt.plot(x, y, label=f"{function_name}(x)")
    plt.title(f"{function_name} Fonksiyonu")
    plt.xlabel('x')
    plt.ylabel(f'{function_name}(x)')
    plt.legend()
    plt.grid(True)
    plt.show()


# Örnek Kullanım
angle = 45
print("Sin(45°):", math.sin(math.radians(angle)))
print("Cos(45°):", math.cos(math.radians(angle)))
print("Tan(45°):", math.tan(math.radians(angle)))
print("Cot(45°):", (1 / math.tan(math.radians(angle))))
print("Sec(45°):", (1 / math.cos(math.radians(angle))))
print("Csc(45°):", (1 / math.sin(math.radians(angle))))

equation = "sin(x) = 0.5"
print("Denklem çözümü:", solve_trig_equation(equation))

inequality = "cos(x) < 0"
print("Eşitsizlik çözümü:", solve_trig_inequality(inequality))

plot_trig_function("sin")
plot_trig_function("cos")
plot_trig_function("tan")
