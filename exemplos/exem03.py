def e_par(x):
  return x%2 == 0
def par_ou_impar(x):
  if e_par(x) == True:
    return("Par")
  else:
    return("Impar")
print(par_ou_impar(5))
print(par_ou_impar(10))