def numEdges(a, b, c, d, e, f, g) :
	return a + b + c + d + a * e + b * e + c * e + c * f + d * f + e * g + f + g
def numPaths(a, b, c, d, e, f, g) :
	return (a + b + c) * (e * g) + (c + d) * f
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
x = numEdges(a, b, c, d, e, f, g)
y = numPaths(a, b, c, d, e, f, g)
print(x)
print(y)
