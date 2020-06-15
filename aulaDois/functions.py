
def ola(nome, maiusculo=False):
    if maiusculo:
        msg= f"Ola, {nome}".upper()
    else:
        msg= f"Ola, {nome}"
    print(msg)


ola("Igor")
ola("Marcela", maiusculo=True)
ola("Jan")