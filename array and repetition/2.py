x = [0] * 10 # Initialize list 'x' with 10 elements (or you can start with an empty list `x = []`)

for i in range(10):
    while True:
            try:
                x[i] = int(input(f"Masukkan angka ke-{i+1}: "))
                break
            except:
                print("\033[91mAngka woy!!!\033[0m")
p = 0
nol = 0
n = 0

for i in range(10):
    if x[i] > 0:
        p += 1
    elif x[i] == 0:
        nol += 1
    else:
        n += 1

print(f"\nBilangan positif ada {p}")
print(f"Bilangan negatif ada {n}")
print(f"Bilangan nol ada {nol}")
