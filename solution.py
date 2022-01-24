from tabulate import tabulate 

table = [['Item-ID','Item-Name','Price'],
         [1,'eggs', 10000],
         [2,'potato', 12000],
         [3,'dsa', 15000],
         [4,'dsa', 19000],
         [5,'dsadsa', 20000],
         [6,'dsad', 30000],
         [7,'rew', 32000],
         [8,'rewr', 120000],
         [9,'rewr', 220000],
         [10,'rewr', 240000]]

print(tabulate(table))
t = len(table)

#print(table[5][0]," ",table[5][1])


x = input("Please enter the dolar value of yesterday:\n")
y = input("Please enter the dolar value of today:\n")

x = int(x)
y = int(y)

d = 0
d = ((y-x)/x)*100



for x in range(t-1):
        #print(table[x][1])
	table[x+1][2] = table[x+1][2]+ table[x+1][2]*(d/100)

print(tabulate(table))
a = 0
f = 0
try:
	while True:
		f = input("Please enter Item ID:\n")
		f = int(f)
		a = a + table[f][2] 

	
except KeyboardInterrupt:
	print("press ")
	pass
 
print("The total ammount is:\n",a," L.L")

	
