import matplotlib.pyplot as plt

a = [1, 2, 3, 4, 5, 6,7]
plt.xlabel('Wind Power Class')
b = [0, 100, 150, 200 , 250, 300, 400]
plt.ylabel('Wind Power Density \n W/(m^2)')
x3 = [0, 4.4, 5.1, 5.6, 6.0, 6.4, 7.0]
#plt.x3label('Speed (m/s2) mph')
plt.plot(a , b , label = 'Wind Line')
plt.plot(a , x3 , label = 'Density Line')
plt.plot(x3 , b , label = 'Speed Line')


"""plt.alabel('Is ball life')
plt.blabel('Is ball life')

1	0	0	0	 
100	4.4 (9.8)	200	5.6 (12.5)
2
150	5.1 (11.5)	300	6.4 (14.3)
3
200	5.6 (12.5)	400	7.0 (15.7)
4
250	6.0 (13.4)	500	7.5 (16.8)
5
300	6.4 (14.3)	600	8.0 (17.9)
6
400	7.0 (15.7)	800	8.8 (19.7)
7
1000	9.4 (21.1)	2000	11.9 (26.6)


"""







plt.title('Air in Air \n Tonight')
plt.legend()
plt.show()
