A = 1200
B = 5000
horas = 0
while A < B and horas < 10000:
 A = A + (A * 0.08)
 B = B + (B * 0.05)
 horas = horas + 1
print("Após", horas, "horas:")
print("População A =", int(A))
print("População B =", int(B))