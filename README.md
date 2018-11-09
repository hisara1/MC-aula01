# MC-aula01
Trabalho da primeira aula

import numpy
a = numpy.arange(4.0) 
b = a * 23.4 
c = b/(a+1) 
c += 10 
print (c)  

arr = numpy.arange(100, 200) 
select = [5, 25, 50, 75, -5] 
print(arr[select])  # can use integer lists as indices  

arr = numpy.arange(10, 20 )
div_by_3 = arr%3 == 0  # comparison produces boolean array 
print(div_by_3) 

print(arr[div_by_3])  # can use boolean lists as indices 

arr = numpy.arange(10, 20) . reshape((2,5))
