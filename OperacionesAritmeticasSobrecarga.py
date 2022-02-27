"""Sobrecarga de operaciones con Python 
    Nathalia Silvera 12-10921"""

import math

class Vector(object):
    def __init__(self, *args):
        """ Crea un vector, ejemplo: v = Vector(1,2,3) """
        if len(args)==0: self.values = (0,0)
        else: self.values = args

    def __add__(self, v):
        """ Suma vectores coordenada a coordenada y un vector con un 
        float coordenada a coordenada """
        if isinstance(v, Vector):
            added = tuple( a + b for a, b in zip(self, v) )
        elif isinstance(v, (int, float)):
            added = tuple( a + v for a in self )
        else:
            raise ValueError("Addition with type {} not supported".format(type(v)))
        
        return self.__class__(*added)
    
    def __radd__(self, v):
        """ Llamado para instancias 4 +  """
        return self.__add__(v)

    def __sub__(self, v):
        """ Resta  vectores coordenada a coordenada y un vector con un 
            float coordenada a coordenada """
        if isinstance(v, Vector):
            subbed = tuple( a - b for a, b in zip(self, v) )
        elif isinstance(v, (int, float)):
            subbed = tuple( a - v for a in self )
        else:
            raise ValueError("Subtraction with type {} not supported".format(type(v)))
        
        return self.__class__(*subbed)
    
    def __rsub__(self, v):
        """ Llamado para instancias  4- """
        return self.__sub__(v)   
 
    def __mod__(self, v):
        """ Retorna el producto punto de un vector
        """
        if not isinstance(v, Vector):
            raise ValueError('El producto punto requiere otro vector')
        return sum(a * b for a, b in zip(self, v))
    
    def __mul__(self, v):
        """ Multiplica un entero o flotante por el vector y calcula el producto cruz.
    """
        if isinstance(v, (int, float)):
            product = tuple( a * v for a in self )
            return self.__class__(*product)
        elif isinstance(v, Vector):
            return Vector((a[1]*b[2]-b[1]*a[2]), (-(a[0]*b[2]-b[0]*a[2])), (a[0]*b[1]-b[0]*a[1]))
        else:
            raise ValueError("Multiplicacion con tipo {} no suportado".format(type(v)))

    def __rmul__(self, v):
        """ Llamado para instancias  4* """
        return self.__mul__(v)
            
    def __iter__(self):
        return self.values.__iter__()
      
    def __getitem__(self, key):
        return self.values[key]

    def __repr__(self):
        return str(self.values)

a = Vector (1,2,3)  
b = Vector (2, 3,4)
c = Vector (1,1,1)
print("------------Expresiones aritmeticas--------")
print("------------Operaciones basicas--------")
print("Vector a:", a, "Vector b: ", b, "Vector c", c)
print("\n")
print("suma de vectores")
print("a+b: ", a+b)
print("resta de vectores")
print("a-b: ", a-b)
print("Producto Punto")
print("a%b: ",a%b)
print("Producto Cruz")
print("a*b: ", a*b)
print("\n")
print("-------------Operaciones que deben cumplir------------")
print("b + c: ",b + c)
print("a * b + c: ",a * b + c)
print("(b + b) * (c - a): ",(b + b) * (c - a))
print("c*b: ", c*b)
print("a % (c * b): ",a % (c * b))
print("b + 3: ", b + 3)
print("a * 3.0 + 7.0: ",a * 3.0 + 7.0)
print("(b + b) * (c % a): ",(b + b) * (c % a))

