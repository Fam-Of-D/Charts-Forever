import matplotlib.pyplot as plt

x = [ 23,45,34,45,47,59,71]

#y = [x for x in range(len(x))]
bins = [10,20,30,40,50,60,70]

plt.scatter(x,bins, label= 'skitscat', color='k', s=500)
#plt.bar(x2,y2,label = 'Second Bar', color='c')


#important
plt.xlabel('Plot Number')
plt.ylabel('Important Var')

plt.title('Interesting Graph \nCheck it out')

plt.legend()
plt.show()