print(" *** Distance *** ")
u,a,t=input("Enter Velocity Acceleration Time: ").split(',')
u = float(u)
a = float(a)
t = float(t)
#print(f"u={u}, a={a}, t={t}")
v = u + (a*t)
s = ((u+v)/2)*t
print(f"Your Distance = {s:.02f}")
