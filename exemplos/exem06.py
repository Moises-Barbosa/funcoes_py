def fatorial(n):
  fat = 1
  for i in list(range(n)):
    fat *= i+1
  return fat
print(fatorial(4))