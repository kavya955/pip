import numpy as n
import pandas as p
d=p.DataFrame(
    {"date":p.date_range(start="2024-07-01",periods=5,freq="D"),"temp":n.random.randint(18,30,size=5)}
)
d["f"]=d["temp"].shift(1)
print("shift:\n",d)
print("\n resamping:\n",d)