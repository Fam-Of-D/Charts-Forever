import matplotlib.pyplot as plt

x = [44,2,6,7,4,5,66]
y = [76,8,7,45,7,6,34]

x2 = [0 ,2, 4, 16, 256 , 144 ,34 ]
y2 = [14 , 12, 36 , 46, 23, 6 , 34]


plt.plot(x , y , label = 'First Line')
plt.plot(x2 , y2 , label = 'Anal Line')
plt.xlabel('Is ball life')
plt.ylabel('Being Black')


plt.title('Scientist Average \n Fucks Given')
plt.legend()
plt.show()
