def soma(lista):
  soma = 0
  for i in lista:
    soma += i
  return soma
l = list(range(1, 5))
print(soma(l))