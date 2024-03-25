import math
def celciustofahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheittocelcius(fahrenheitt):
    return (fahrenheitt -32 ) * (5/9)


def karealanhesap(x):
    return x**2
def dikdortgenalanhesap(en,boy):
    return en * boy

def ucgenalan(birinci,ikinci,ucuncu):
    s=(birinci+ikinci+ucuncu)/2
    return math.sqrt(s*(s-birinci)*(s-ikinci)*(s-ucuncu))

def dairealan(yaricap):
    sonuc=math.pi*(yaricap**2)
    return sonuc

def getir(x):
    return 2**x

print(ucgenalan(3,4,5))
print(getir(5))
print(math.asin(0.8))
#print(celciustofahrenheit(42))