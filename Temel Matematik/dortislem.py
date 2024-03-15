def toplam(*args):
    return sum(args)

def cikartma(cikarilan, cikarim):
    return cikarilan - cikarim

def carpma(*args):
    sonuc=1
    for arg in args:
        sonuc*=arg
    return sonuc

def bolme(bolunen,bolen):
    return bolunen/bolen


print(carpma(1,2,3,4,5,6))
print(toplam(15, 4), " ve ", toplam(48, 4, 78, 74))
print(cikartma(4, 48))
print(bolme(8,2))