# 2-boyutlu ve 3-boyutlu koordinat sistemleri için noktaların temsili
# 2-boyutlu: (x, y), 3-boyutlu: (x, y, z)
nokta_2d = (3, 4)
nokta_3d = (2, -1, 5)

# Doğrunun denklemi: y = mx + b
# m: eğim, b: y-kesişimi
# Verilen x değerleriyle y değerlerini hesaplayabiliriz.
m = 2
b = 1
x_degeri = 3
y_degeri = m * x_degeri + b

# Düzlemin denklemi: ax + by + cz = d
# a, b, c: normal vektör, d: bir noktanın düzleme olan uzaklığı
# Verilen bir noktanın düzlem üzerinde olup olmadığını kontrol edebiliriz.
a = 2
b = -3
c = 1
d = 5
x_nokta = 1
y_nokta = 2
z_nokta = 3
if a*x_nokta + b*y_nokta + c*z_nokta == d:
    print("Nokta düzlem üzerinde.")
else:
    print("Nokta düzlem üzerinde değil.")

# Verilen iki doğrunun kesişim noktasını bulma
def kesisme_noktasi(m1, b1, m2, b2):
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x, y

m1 = 2
b1 = 1
m2 = -1
b2 = 4
kesisme = kesisme_noktasi(m1, b1, m2, b2)
print("Doğruların kesişim noktası:", kesisme)
