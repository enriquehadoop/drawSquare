#serie de fibonacci
x = 1
y = 1
suma = 0
print(x)
print(y)
for i in range(15):
  suma = x + y
  y = x
  x = suma
  print(suma)