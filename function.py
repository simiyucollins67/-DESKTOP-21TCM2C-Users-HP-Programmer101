def ongeza(a):
    a=1
    yield a
    a+=a
    if a > 100:
        print(a)