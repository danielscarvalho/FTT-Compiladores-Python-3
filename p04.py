def maior(v):
    return max(v)

def menor(v):
    return min(v)

def primeiro(v):
    return v[0]

def último(v):
    return v[-1]

def tamanho(v):
    return len(v)

lst = range(10,40)
mensagem = "Vai Corinthians!!!"

print(último(lst))
print(maior(lst))
print(primeiro(mensagem), type(primeiro(mensagem)))
print(primeiro(lst), type(primeiro(lst)))
print(tamanho(lst))
print(tamanho(mensagem))