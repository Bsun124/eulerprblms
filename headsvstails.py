import matplotlib.pyplot as plt
import random
                       #Makes a Tail and Head Counter

Headcount=0
Tailcount=0

while Headcount != Tailcount +4:
    runresult=random.choice(['H', 'T'])
    if runresult=='T':
        Tailcount+=1
    if runresult=='H':
        Headcount+=1
x=Headcount
y=Tailcount
plt.title('Number of Headcount vs Tailcount Runs')
plt.plot(x, y, marker='x')
plt.xlabel('Number of Headcount Runs')
plt.ylabel('Number of Tailcount Runs')
plt.show()
plt.savefig('headsvscounts.jpg')
