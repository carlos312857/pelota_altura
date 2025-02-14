# input 
h=int (input("ingrese la altura: "))

# processing

q = h/5
n = 0

while h >= q:
    h = 0.9 * h

    n = n + 1

# output 

print("la pelota rebota la quinta parte en el rebote " + str (n))