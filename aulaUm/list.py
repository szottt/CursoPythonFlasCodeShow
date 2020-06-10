cores = ["azul", "vermelho", "verde"]
numeros = [1,2,3]
mistura = [1, "Igor", True, cores, numeros, [1,2,3]]

cores.append("laranja")
cores.insert(1,"branco")
cores.remove('azul')
print(cores)
print('#' * 20)
#Tuplas

identidade = ("Igor", "456782345-9",15)
print(f'Nome é {identidade[0]}')
print(f'CPF é {identidade[1]}')
print(f'Idade é {identidade[2]}')

print('#' * 20)
#desempacotamento
nome, cpf, idade = identidade
print(nome,cpf,idade)

print('#' * 20)
# Dicionario (Array associativo, HasMap Object)

pessoa = {
        "nome":"Igor",
        "CPF":"495686769-9",
        "idade":18,
        "cores_preferidas":cores,
        "numeros_preferidos":numeros
        }

pessoa["idade"] = 19
pessoa["canal"] = "@sztao"

print(f'Ola, o {pessoa["nome"]} tem {pessoa["idade"]} anos, e suas cores preferidas são {pessoa["cores_preferidas"]} e numeros {pessoa["numeros_preferidos"]}')

print('#' * 20)
#Iteração(pegar um elemento de cada vez)

for cor in cores:
    print(cor.upper())

print('#' * 20)

for letra in "Igor":
    if letra == "g":
        continue
    print(letra)

print('#' * 20)
print("Igor"[0])
print("Igor"[-1])

print('#' * 20)

# List Comprehension
print([letra for letra in "Igor"])

# List Comprehension Filtrada
print([letra for letra in "Igor" if letra != "g"])

print('#' * 20)
for chave in pessoa:
    print(chave, ":", pessoa[chave])

print('#' * 20)

for chave, valor, in pessoa.items():
    print(chave, ":", valor)