def f(x,y,z):
	print(3*x*x-z*z-9)

x = 2
y = 0
z = sqrt(3)

print("Origen")
f((-1)*x,(-1)*y,(-1)*z)

print("Eje X")
f(x,(-1)*y,(-1)*z)

print("Eje Y")
f((-1)*x,y,(-1)*z)

print("Eje Z")
f((-1)*x,(-1)*y,z)

print("Plano xy")
f(x,y,(-1)*z)

print("Plano yz")
f((-1)*x,y,z)

print("Plano xz")
f(x,(-1)*y,z)
