def soma(a):
  soma = 0
  for i in a:
    soma += i
  return soma
def media(a):
  return soma(a)/len(a)
list = [4, 6, 5, 10, -5]
print(media(list))

#outra forma de fazer

def media(a):
  soma = 0
  for i in a:
    soma += i
  return soma/len(a)
print(media(list)) 