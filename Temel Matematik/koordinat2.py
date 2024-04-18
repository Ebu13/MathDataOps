"""
`self`, bir sınıfın metotlarında kullanılan bir parametredir ve o sınıfın örneğini (instance) temsil eder.
Python'da, bir sınıfın metotlarını tanımlarken, metotların ilk parametresi genellikle `self` olarak adlandırılır.
Bu, metotların çağrıldığı örneğe erişim sağlar.

Örneğin, bir sınıfın içindeki bir metot, o sınıfın özelliklerine ve diğer metotlarına erişmek için `self` kullanır.
Bu sayede, her örnek kendi özel durumlarını tutabilir ve metotlar bu durumlara erişebilir.

Ayrıca, `self` kelimesiyle bir metot içinde örneğin kendisine erişim sağlanır.
Bu, herhangi bir örnek üzerinde metotların çağrılabilmesini ve
her örneğin kendi durumunu ve davranışını yönetebilmesini sağlar.

Örneğin, yukarıdaki Python kodunda `Nokta`, `Dogru` ve `Duzlem` sınıflarında `self`, her bir örneği temsil eder.
Bu sayede, her örnek kendi koordinatları, eğimi veya denklemleri gibi özelliklere sahip olabilir ve
bu özelliklere erişmek için `self` kullanılır.
"""

class Nokta:
    def __init__(self, x, y, z=None):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        if self.z is not None:
            return f"Nokta({self.x}, {self.y}, {self.z})"
        else:
            return f"Nokta({self.x}, {self.y})"


class Dogru:
    def __init__(self, m, b):
        self.m = m
        self.b = b

    def y_degeri(self, x):
        return self.m * x + self.b

    def __repr__(self):
        return f"Doğru(m={self.m}, b={self.b})"


class Duzlem:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def nokta_duzlemde_mi(self, nokta):
        return self.a * nokta.x + self.b * nokta.y + self.c * nokta.z == self.d

    def __repr__(self):
        return f"Duzlem(a={self.a}, b={self.b}, c={self.c}, d={self.d})"


# Noktaların oluşturulması
nokta1 = Nokta(3, 4)
nokta2 = Nokta(2, -1, 5)

print("Nokta 1:", nokta1)
print("Nokta 2:", nokta2)

# Doğrunun oluşturulması ve y değerinin hesaplanması
dogru = Dogru(2, 1)
x_degeri = 3
y_degeri = dogru.y_degeri(x_degeri)
print(f"Doğrunun ({x_degeri}, y) noktası:", y_degeri)

# Düzlemin oluşturulması ve bir noktanın düzlem üzerinde olup olmadığının kontrolü
duzlem = Duzlem(2, -3, 1, 5)
nokta = Nokta(1, 2, 3)
if duzlem.nokta_duzlemde_mi(nokta):
    print("Nokta düzlem üzerinde.")
else:
    print("Nokta düzlem üzerinde değil.")

# İki doğrunun kesişim noktasının bulunması
def kesisme_noktasi(dogru1, dogru2):
    x = (dogru2.b - dogru1.b) / (dogru1.m - dogru2.m)
    y = dogru1.y_degeri(x)
    return Nokta(x, y)

dogru1 = Dogru(2, 1)
dogru2 = Dogru(-1, 4)
kesisme = kesisme_noktasi(dogru1, dogru2)
print("Doğruların kesişim noktası:", kesisme)
