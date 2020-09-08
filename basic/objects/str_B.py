a = "1%s2%s4"
b = "\x051\x051"
print(b.split("\x05"))
a % tuple(b.split("\x05")[0:-1])

a % ("\&lt", "90")
