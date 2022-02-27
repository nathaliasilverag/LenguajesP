import math
# Calcula la potencia tal que 
# a^b si b = 0, entonces es 1
# si b>0 entonces a × a b−1
# Nathalia Silvera 12-10921  
var
    a: int = 2
    b: int = 4
    d: int = 0
echo "Potencia"
echo "variable a: ",a
echo "variable b: ",b
proc potencia(a: int, b: int): int =
  if b == 0:
    return 1 
  elif b > 0:
    var c: int = a * a^(b-1)
    return c
  

when isMainModule:
  d = potencia(a,b)
  echo "Potencia a^b: ", d