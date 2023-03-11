from math import factorial

def p_cal(p, n): 
  temp = p
  for i in range(1, n):
    if(i % 2 == 1):
      temp * (p - i)
    else:
      temp * (p + i)
  return temp

x = [0,0.2,0.4]
n = len(x)
y = [1,1.4,1.9]

for i in range(n):
    y[i][0] = x[i] ** 5

for i in range(1, n):
  for j in range(n - i):
    y[j][i] = round((y[j + 1][i - 1] - y[j][i - 1]), 4)

value = float(input('Enter х: '))
sum = y[int(n/2)][0]
p = (value - x[int(n/2)]) / (x[1] - x[0])

for i in range(1,n): 
  sum += (p_cal(p, i) * y[int((n-i)/2)][i]) / factorial(i)

print("\nValue at", value, "is", round(sum, 4))