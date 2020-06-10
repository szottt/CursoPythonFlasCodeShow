a = 0
b = 10

try:
    b.upper()
    print(b // a)
except AttributeError as e:
    print('Nao pode Transfomormar numero em Maiusculo',str(e))
except ZeroDivisionError as e:
    print('Deu erro tenta de novo',str(e))