# 5. Conversión de tipos (string a int, float a int, etc.).

# De string a int:

s="123"
i=int(s)
print(i, type(i))

# De string a float:

s = "3.1416"
f = float(s)
print(f, type(f))

# De float a int:

f = 9.99
i = int(f)
print(i, type(i))

# De int a float:

i = 7
f = float(i)
print(f, type(f))

# De int a str

i = 42
s = str(i)
print(s, type(s))

# De float a str

f = 1.5
s = str(f)
print(s, type(s))

# De bool a int y str

b1 = True
b2 = False

print(int(b1))
print(int(b2))
print(str(b1))
