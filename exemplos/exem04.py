def pesquisa(lista, valor):
  for i, e in enumerate(lista):
    if e == valor:
      return i
  return None
l = [10, 20, 25, 30]
print(pesquisa(l, 25))
print(pesquisa(l, 27))