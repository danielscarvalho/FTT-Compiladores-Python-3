def check_int(potential_int):
    try:
        int(potential_int)
        return True
    except ValueError:
        return False

def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False

lst = []

while True:
    v = input("Entre com o valor: ")
    print(v, type(v))

    if check_int(v):
        lst.append(int(v))
    elif check_float(v):
        lst.append(float(v))
    else:
        lst.append(v)

    if v == "":
        break

print(lst)

for i in lst:
    print(i, type(i))