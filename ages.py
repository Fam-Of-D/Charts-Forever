import matplotlib.pyplot as plt

p1 = [25,75,95]

p2 = [25,50,75]
                  
p3 = [25,25,25,20,5]
                  
p4 = [25,5,5]
cola = ['c','m','r','k','g']
labels = ['A' , 'C', 'G', 'U', '-']
#plt.scatter(x,y, label = Scatterbitch)

days = [1,2,3]
plt.pie(p3, labels = labels , colors = cola)
plt.ylabel('Old Bitches')
plt.title("Bag of Bones \n Check It Out")
plt.legend()
plt.show()