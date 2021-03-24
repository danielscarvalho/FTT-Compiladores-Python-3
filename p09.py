d = {"Nome":"José", \
    "Valor":234.23, \
    "Time":"Conrinthians", \
    "Dezenas":[10, 33, 44, 22, 1, "Pi"], \
    "ID": 2048,
    "Objeto":{"Filho":"Marcio","Filha":"Mariana","Esposa":"Rita"}}

print(type(d))
print(d.keys())

for v in d.values():
    print(v, type(v))