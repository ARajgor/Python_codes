import pandas
import numpy
series1=numpy.array([10,20,30])
series2=numpy.array(["ABC","DEF","GHI"])

s1=pandas.Series(series1)
s2=pandas.Series(series2)

data={'series 1 ': s1,'series 2':s2}
print(pandas.DataFrame(data))