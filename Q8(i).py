import matplotlib.pyplot as plt
u = int(input("Enter initial velocity : "))
a = int(input("Enter acceleration : "))
v=[]
t=[1,2,3,4,5,6,7,8,9,10]

for i in t:
    v.append(u+(a*i))
plt.plot(t,v)
plt.axis([0,max(t)+2,0,max(v)+2])
plt.xlabel("Time")
plt.ylabel("Velocity")
plt.title("Velocity vs Time")
plt.show()
s=[]
for i in t:
    s.append(u*i+(0.5)*a*i*i)
plt.plot(t,s)
plt.axis([0,max(t)+2,0,max(s)+2])
plt.xlabel("Time")
plt.ylabel("Distance")
plt.title("Distance vs Time")
plt.show()
s=[]
for i in v:
    s.append((i*i-u*u)/(2*a))
plt.plot(v,s)
plt.axis([0,max(v)+2,0,max(s)+2])
plt.xlabel("Velocity")
plt.ylabel("Distance")
plt.title("Distance vs Velocity")
plt.show()
