# Multiplicacion de matrices N*M
# Nathalia Silvera 12-10921

#Defino el tipo
type Matrix[M, N: static[int]] = array[M, array[N, float]]

#Asigno al arreglo a el valor de las matrices
let a = [[1.0,  1.0,  1.0],
         [2.0, 4.0,  8.0]]
 
let b = [[4.0, -3.0 ,  4/3.0, -1/4.0],
         [-13/3.0, 19/4.0 ,-7/3.0, 11/24.0],
         [3/2.0, -2.0 , 7/6.0, -1/4.0]]

proc `*`[m, n, p](a: Matrix[m, n], b: Matrix[n, p]): Matrix[m, p] =
  for i in result.low .. result.high:
    for j in result[0].low .. result[0].high:
      for k in a[0].low .. a[0].high:
        result[i][j] = a[i][k] * b[k][j]
        
when isMainModule:
  echo "matriz a :",a
  echo "matriz b: ",b
  echo "resultado a*b: ",a * b
