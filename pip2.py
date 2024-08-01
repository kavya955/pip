import pandas as p
d=p.DataFrame([[2,6,5],[4,2,8],[9,6,1]],columns=["maths","java","py"])
print(d)
c=d.agg(['sum','min','max','count','mean','median','std','size'])
print()
print(c)
