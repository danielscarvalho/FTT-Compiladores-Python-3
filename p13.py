import random

f = open("out.csv", "a")

for i in range(100):
    f.write("info," + str(i) + "," + str(random.randint(10,100)) + "\n" )

f.close()