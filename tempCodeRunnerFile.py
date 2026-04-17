import random

empty=[]
total=0
for i in range(20):
    rmd=random.randint(1,100)
    empty.append(rmd)
    total=total+empty[i]
    
print(empty)