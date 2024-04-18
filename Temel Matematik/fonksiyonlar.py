# Normal fonksiyon
def greet():
    print("Hello!")


greet()


# Doğrusal fonksiyon: f(x) = ax + b
def linear_function(x, a, b):
    return a * x + b


# Örnek kullanım
result = linear_function(3, 2, 1)
print(result)  # Çıktı: 7


# Kuadratik fonksiyon: f(x) = ax^2 + bx + c
def quadratic_function(x, a, b, c):
    return a * x ** 2 + b * x + c


# Örnek kullanım
result = quadratic_function(2, 1, -3, 2)
print(result)  # Çıktı: 0


# Üstel fonksiyon: f(x) = a^x
def exponential_function(x, a):
    return a ** x


# Örnek kullanım
result = exponential_function(2, 3)
print(result)  # Çıktı: 9
import math


# Trigonometrik fonksiyon: f(x) = sin(x)
def sine_function(x):
    return math.sin(x)


# Örnek kullanım
result = sine_function(math.pi / 2)  # 90 derece
print(result)  # Çıktı: 1.0


# Tanım kümesi: x >= 0
# Değer kümesi: {0, 1, 2, ...}
def positive_integer(x):
    if x >= 0:
        return x
    else:
        return None


# Örnek kullanım
result = positive_integer(5)
print(result)  # Çıktı: 5


# Teklik kontrolü
def is_odd(number):
    return number % 2 != 0


# Çiftlik kontrolü
def is_even(number):
    return number % 2 == 0


# Örnek kullanım
print(is_odd(3))  # Çıktı: True
print(is_even(4))  # Çıktı: True

"""
# Artan fonksiyon kontrolü

def is_increasing(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] > sequence[i + 1]:
            return False
    return True
"""


def is_increasing(sequence):
    return all(sequence[i] <= sequence[i + 1] for i in range(len(sequence) - 1))


"""
# Azalan fonksiyon kontrolü
def is_decreasing(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] < sequence[i + 1]:
            return False
    return True
"""


def is_decreasing(sequence):
    return all(sequence[i] >= sequence[i + 1] for i in range(len(sequence) - 1))


# Örnek kullanım
print(is_increasing([1, 2, 3, 4]))  # Çıktı: True
print(is_decreasing([4, 3, 2, 1]))  # Çıktı: True
